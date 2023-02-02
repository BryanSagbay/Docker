from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis',port=6379)


@app('/',methods=['GET'])
def obtener(): 
    redis.incr('hits')
    counter = str(redis.get('hits','utf-8'))

    return "Conexion Exitosa"+counter+"times"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
