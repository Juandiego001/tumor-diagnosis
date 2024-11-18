import os
import numpy as np
from flask import abort
import onnxruntime as rt
from apiflask import APIBlueprint
from core.schemas.ai import PredictionOutSchema, TumorInSchema


bp = APIBlueprint('ai', __name__)
current_dir = os.getcwd()
model_path = os.path.abspath(os.path.join(current_dir, 'models', 'log_reg_model.onnx'))


@bp.post('/')
@bp.input(TumorInSchema)
@bp.output(PredictionOutSchema)
def get_tumor_data(json_data):
  try:
    values = [float(value) for value in json_data.values()]
    np_values = np.array(values, dtype=np.float32)
    sess = rt.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name
    pred_onx = sess.run([label_name], {input_name: np_values})[0][0]
    return {'prediction': int(pred_onx)}
  except Exception as ex:
    return abort(str(ex))
