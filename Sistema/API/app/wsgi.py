from application import init_app
from flask_cors import CORS

app = init_app()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')