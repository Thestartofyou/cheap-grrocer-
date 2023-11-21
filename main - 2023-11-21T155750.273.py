class Product:
    def __init__(self, name, price, calories, protein):
        self.name = name
        self.price = price
        self.calories = calories
        self.protein = protein

def calculate_nutritional_score(product):
    # Define a simple nutritional scoring system (this is just an example)
    return product.calories - product.price + 2 * product.protein

def find_healthiest_meal(products):
    # Calculate nutritional scores for all products
    scores = {product: calculate_nutritional_score(product) for product in products}

    # Sort products by nutritional score in descending order
    sorted_products = sorted(products, key=lambda x: scores[x], reverse=True)

    return sorted_products[0]  # Return the healthiest meal

# Hypothetical Trader Joe's product data
product1 = Product("Product A", 3.99, 200, 10)
product2 = Product("Product B", 2.99, 180, 8)
product3 = Product("Product C", 4.99, 250, 12)

# List of Trader Joe's products
trader_joes_products = [product1, product2, product3]

# Find the healthiest meal
healthiest_meal = find_healthiest_meal(trader_joes_products)

# Display the result
print(f"The healthiest meal is: {healthiest_meal.name}")
print(f"Price: ${healthiest_meal.price}")
print(f"Calories: {healthiest_meal.calories} kcal")
print(f"Protein: {healthiest_meal.protein} g")

