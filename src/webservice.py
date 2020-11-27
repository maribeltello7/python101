from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido ={"id": 1, "nombre":"juan"}
    contenido2 = {"id": 2, "nombre": "pepe"}
    lista = [contenido, contenido2]
    return jsonify(lista)

@app.route('/', methods=['GET'])
def saludo():
    return 'hola mundo'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")