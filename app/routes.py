from flask import Blueprint, jsonify, request
from .models import Product, InventoryEntry, InventoryExit
from .utils import get_status
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/api/products', methods=['POST'])
def crear_producto():
    data = request.json
    new_product = Product(name = data['name'], description = data['description'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado con exito"}), 201

@main.route('/api/inventory/entry', methods=['POST'])
def inventory_entry():
    data = request.json
    new_entry = InventoryEntry(
        product_id = data["data"]['product_id'],
        quantity = data["data"]['quantity'],
        expiration_date = datetime.strptime(data["data"]['expiration_date'], '%Y-%m-%d')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"mensaje": "Ingreso de inventario exitoso"}), 201

@main.route('/api/inventory/exit', methods=['POST'])
def inventory_exit():
    data = request.json
    new_exit = InventoryExit(
        entry_id = data["data"]['entry_id'],
        quantity = data["data"]['quantity']
    )
    db.session.add(new_exit)
    db.session.commit()
    return jsonify({"mensaje": "Salida de inventario exitosa"}), 201

@main.route('/api/products/list', methods=['GET'])
def list_products():
    products = Product.query.all()
    response = []

    for product in products:
        entries = InventoryEntry.query.filter_by(product_id = product.id).all()
        product_status = []
        if entries:
            for entry in entries:
                exits = InventoryExit.query.filter_by(entry_id = entry.id).all()
                total_exits = sum(exit.quantity for exit in exits)

                cantidad_disponible = entry.quantity - total_exits

                if cantidad_disponible > 0:
                    product_status.append({
                        'product_id': product.id,
                        'id_entry': entry.id,
                        'cantidad_disponible': cantidad_disponible,
                        'fecha_vencimiento': entry.expiration_date.strftime('%Y-%m-%d'),
                        'estado': get_status(entry.expiration_date)
                    })

            product_status = sorted(product_status, key=lambda x: x['fecha_vencimiento'])
        else:
            product_status.append({
                'product_id': product.id,
                'id_entry': None,  # O un valor que represente que no hay ID
                'cantidad_disponible': None,
                'fecha_vencimiento': 'N/A',  # O un valor que prefieras
                'estado': 'N/A'  # O un valor que prefieras
            })

        response.append({
            'name': product.name,
            'status': product_status
        })

    return jsonify(response), 200
