import os
from apiflask import APIFlask
from dotenv import load_dotenv


load_dotenv()


app = APIFlask(__name__)

app.config['HOST'] = HOST = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = PORT = os.getenv('PORT', 5000)
