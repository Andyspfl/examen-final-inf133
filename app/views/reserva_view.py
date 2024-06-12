def render_reserva_list(reservas):
    # Representa una lista de reservas como una lista de diccionarios
    return [
        {
            "id": reserva.id,
            "user_id": reserva.user_id,
            "restaurant_id": reserva.restaurant_id,
            "reservation_date": reserva.reservation_date.isoformat(),  # Formato ISO 8601
            "num_guests": reserva.num_guests,
            "special_requests": reserva.special_requests,
            "status": reserva.status,
        }
        for reserva in reservas
    ]


def render_reserva_detail(reserva):
    # Representa los detalles de una reserva como un diccionario
    return {
        "id": reserva.id,
        "user_id": reserva.user_id,
        "restaurant_id": reserva.restaurant_id,
        "reservation_date": reserva.reservation_date.isoformat(),  # Formato ISO 8601
        "num_guests": reserva.num_guests,
        "special_requests": reserva.special_requests,
        "status": reserva.status,
    }
