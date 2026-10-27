
import json

with open("products.json", "r") as file:
    products = json.load(file)


def search_product(query):
    """Search the product catalogue by ID, name, or description."""
    query = query.lower()

    results = [
        product
        for product in products
        if query in product["id"].lower()
        or query in product["name"].lower()
        or query in product["description"].lower()
    ]

    if not results:
        return "Product not found."

    return results


def check_price(product_id):
    """Return the price of a product using its ID."""
    for product in products:
        if product["id"] == product_id:
            return f'{product["name"]}: {product["price"]:,} RWF'

    return f"Product {product_id} not found."
