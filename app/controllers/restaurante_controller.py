from flask import Blueprint, jsonify, request
from app.models.restaurante_model import Restaurante
from app.utils.decorators import jwt_required, roles_required
from app.views.restaurante_view import render_restaurant_detail, render_restaurant_list

restaurante_bp = Blueprint("restaurant", __name__)

@restaurante_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.get_all()
    return jsonify(render_restaurant_list(restaurants))

@restaurante_bp.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if restaurant:
        return jsonify(render_restaurant_detail(restaurant))
    return jsonify({"error": "Restaurante no encontrado"}), 404

@restaurante_bp.route("/restaurants", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_restaurant():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")

    if not all([name, address, city, phone]):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    restaurant = Restaurant(name=name, address=address, city=city, phone=phone,
                            description=description, rating=rating)
    restaurant.save()

    return jsonify(render_restaurant_detail(restaurant)), 201

@restaurante_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_restaurant(id):
    data = request.json
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "Restaurante no encontrado"}), 404

    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")

    restaurant.update(name=name, address=address, city=city, phone=phone,
                      description=description, rating=rating)

    return jsonify(render_restaurant_detail(restaurant))

@restaurante_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_restaurant(id):
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "Restaurante no encontrado"}), 404

    restaurant.delete()

    return "", 204
