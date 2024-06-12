def render_restaurant_list(restaurants):
    # Representa una lista de restaurantes como una lista de diccionarios
    return [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "description": restaurant.description,
            "rating": float(restaurant.rating) if restaurant.rating is not None else None,
        }
        for restaurant in restaurants
    ]


def render_restaurant_detail(restaurant):
    # Representa los detalles de un restaurante como un diccionario
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "city": restaurant.city,
        "phone": restaurant.phone,
        "description": restaurant.description,
        "rating": float(restaurant.rating) if restaurant.rating is not None else None,
    }
