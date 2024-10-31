from datetime import datetime
from . import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class InventoryEntry(db.Model):
    __tablename__ = 'inventory_entries'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    entry_date = db.Column(db.DateTime, default=datetime.now())

class InventoryExit(db.Model):
    __tablename__ = 'inventory_exits'
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('inventory_entries.id'))
    quantity = db.Column(db.Integer, nullable=False)
    exit_date = db.Column(db.DateTime, default=datetime.now())
