from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis',port=6379)


@app('/',methods=['GET'])
def obtener(): 
    redis.incr('rainbow_database')
    counter = str(redis.get('rainbow_database','utf-8'))

    return "Conexion Exitosa"+counter+"times"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
