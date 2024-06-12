from flask import Blueprint, jsonify, request
from app.models.reserva_model import Reserva
from app.utils.decorators import jwt_required, roles_required
from app.views.reserva_view import render_reserva_detail, render_reserva_list

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/reservations", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_reserves():
    reserves = Reserva.get_all()
    return jsonify(render_reserva_list(reserves))


@reserva_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
def get_reserva(id):
    reserva = Reserva.get_by_id(id)
    if reserva:
        return jsonify(render_reserva_detail(reserva))
    return jsonify({"error": "Reserva no encontrada"}), 404


@reserva_bp.route("/reservations", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_reserva():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    if not all([user_id, restaurant_id, reservation_date, num_guests, special_requests, status]):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    reserva = Reserva(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date,
                      num_guests=num_guests, special_requests=special_requests, status=status)
    reserva.save()

    return jsonify(render_reserva_detail(reserva)), 201


@reserva_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_reserva(id):
    data = request.json
    reserva = Reserva.get_by_id(id)

    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404

    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    reserva.update(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date,
                   num_guests=num_guests, special_requests=special_requests, status=status)

    return jsonify(render_reserva_detail(reserva))


@reserva_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_reserva(id):
    reserva = Reserva.get_by_id(id)

    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404

    reserva.delete()

    return "", 204
