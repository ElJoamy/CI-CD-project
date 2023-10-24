from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 5.99},
    {"id": 3, "nombre": "Producto 3", "precio": 3.99}
]

@app.route('/', methods=['GET'])
def index():
    return jsonify({"mensaje": "Bienvenido a mi API de productos, puedes ver lo siguiente, /productos, /productos/<id>, /productos (POST), /productos/<id> (DELETE)"})

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = {
        "id": request.json["id"],
        "nombre": request.json["nombre"],
        "precio": request.json["precio"]
    }
    productos.append(nuevo_producto)
    return jsonify({"mensaje": "Producto agregado exitosamente"})

# Ruta para eliminar un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        productos.remove(producto)
        return jsonify({"mensaje": "Producto eliminado exitosamente"})
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
