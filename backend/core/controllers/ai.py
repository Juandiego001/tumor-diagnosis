import os
import numpy as np
from flask import abort
import onnxruntime as rt
from apiflask import APIBlueprint
from core.schemas.ai import PredictionOutSchema, TumorInSchema


bp = APIBlueprint('ai', __name__)
current_dir = os.getcwd()
log_reg_model_path = os.path.abspath(os.path.join(current_dir, 'models', 'log_reg_model.onnx'))
perceptron_model_path = os.path.abspath(os.path.join(current_dir, 'models', 'perceptron_model.onnx'))
knn_model_path = os.path.abspath(os.path.join(current_dir, 'models', 'knn_model.onnx'))


@bp.post('/<string:model>')
@bp.input(TumorInSchema)
@bp.output(PredictionOutSchema)
def get_tumor_data(model, json_data):
  try:
    values = [float(value) for value in json_data.values()]
    np_values = np.array(values, dtype=np.float32)

    if model == 'LOG':
      sess = rt.InferenceSession(log_reg_model_path, providers=['CPUExecutionProvider'])
      input_name = sess.get_inputs()[0].name
      label_name = sess.get_outputs()[0].name
      pred_onx = sess.run([label_name], {input_name: np_values})[0][0]
    elif model == 'PERCEPTRON':
      sess = rt.InferenceSession(perceptron_model_path, providers=['CPUExecutionProvider'])
      input_name = sess.get_inputs()[0].name
      label_name = sess.get_outputs()[0].name
      reshaped_input = np_values.reshape(1, -1)
      pred_onx = sess.run([label_name], {input_name: reshaped_input})[0][0]
    else:
      sess = rt.InferenceSession(knn_model_path, providers=['CPUExecutionProvider'])
      input_name = sess.get_inputs()[0].name
      label_name = sess.get_outputs()[0].name
      reshaped_input = np_values.reshape(1, -1)
      pred_onx = sess.run([label_name], {input_name: reshaped_input})[0][0]

    return {'prediction': int(pred_onx)}
  except Exception as ex:
    return abort(str(ex))
