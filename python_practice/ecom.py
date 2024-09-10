import re

class Product:
    def __init__(self, category, name, price, brand, label):
        self.category = category
        self.name = name
        self.price = price
        self.brand = brand
        self.label = label

    def __repr__(self):
        return f"{self.category.capitalize()}: {self.name} (Brand: {self.brand}, Price: ${self.price}, Label: {self.label})"


class EcommerceStore:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def filter_products(self, query):
        conditions = query.split(",")
        filtered_products = self.products
        print()
        print(filtered_products)
        print()
        for condition in conditions:
            condition = condition.strip()
            try:
                attribute, condition_value = condition.split(":")
                attribute = attribute.strip().lower()
                condition_value = condition_value.strip()

                if attribute not in ["category", "name", "price", "brand", "label"]:
                    print(f"Unknown attribute: {attribute}")
                    return []

                if attribute == "price":
                    match = re.match(r'([<>]=?|==|!=)\s*(\d+(\.\d+)?)', condition_value)
                    if not match:
                        print(f"Invalid condition for price: {condition_value}")
                        return []
                    operator, value = match.groups()[0], float(match.groups()[1])
                    filtered_products = [p for p in filtered_products if self.compare(p.price, operator, value)]
                
                elif attribute in ["category", "name", "brand", "label"]:
                    match = re.match(r'(==|!=|contains|icontains)?\s*(.*)', condition_value, re.IGNORECASE)
                    if not match.groups()[0]:
                        operator = "icontains"
                        value = match.groups()[1].strip().lower()
                    else:
                        operator, value = match.groups()[0], match.groups()[1].strip().lower()
                    
                    filtered_products = [p for p in filtered_products if self.compare(getattr(p, attribute).lower(), operator, value)]

            except ValueError:
                print("Invalid query format. Use the format 'attribute:condition'.")
                return []

        return filtered_products

    @staticmethod
    def compare(attribute_value, operator, value):
        if operator == ">":
            return attribute_value > value
        elif operator == ">=":
            return attribute_value >= value
        elif operator == "<":
            return attribute_value < value
        elif operator == "<=":
            return attribute_value <= value
        elif operator == "==":
            return attribute_value == value
        elif operator == "!=":
            return attribute_value != value
        elif operator == "contains":
            return value in attribute_value
        elif operator == "icontains":
            return value.lower() in attribute_value.lower()
        else:
            return False


# Initialize the store
store = EcommerceStore()

# Add products to the store
store.add_product(Product("phone", "iPhone 13", 999, "Apple", "Latest model"))
store.add_product(Product("phone", "Galaxy S21", 799, "Samsung", "Best seller"))
store.add_product(Product("laptop", "MacBook Pro", 1299, "Apple", "High performance"))
store.add_product(Product("laptop", "XPS 13", 999, "Dell", "Ultra portable"))
store.add_product(Product("groceries", "Bananas", 1.5, "Dole", "Fresh"))
store.add_product(Product("groceries", "Apples", 2.0, "Generic", "Organic"))

def user_search():
    print("Welcome to the E-commerce store search!")
    query = input("Enter your search query (e.g., price:>100, category:phone, brand:apple): ").strip()
    
    results = store.filter_products(query)
    
    if results:
        print("\nSearch results:")
        for product in results:
            print(product)
    else:
        print("\nNo products found matching your criteria.")

# Run the user search function
user_search()
