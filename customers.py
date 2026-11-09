# ISM2411 Lab 11  Customer Dictionary & Lookup

# Name: Larissa Paiva

# Reflection 1:

# I would use .get() when a dictionary key could be missing since it

# lets me give a default value. I would a use bracket notation when

# I expect the key to exist.

# Reflection 2:

# This lab is similar to using SUMIF or a PivotTable in Excel because

# both organize and summarize the information by the category. Python can be

# more useful with more data since it can process records using loops

# automatically.

# Exercise 1: Create and access a customer dictionary

customer = {

    "name": "Alice Johnson",

    "email": "alice@email.com",

    "tier": "gold",

    "ytd_spend": 1250.00

}

print("Customer Name:", customer["name"])

print("Customer Email:", customer["email"])

print("Customer Tier:", customer["tier"])

print("Year-to-Date Spend:", customer["ytd_spend"])

print("Full Customer Dictionary:", customer)

# Exercise 2: Modify the customer dictionary

customer["phone"] = "813-555-0123"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)
# Exercise 3: Safe and unsafe dictionary lookups

print("Email using get():", customer.get("email", "no email on file"))

try:
    print("Email using brackets:", customer["email"])
except KeyError:
    print("Email key does not exist.")
    # Exercise 4: Loop through dictionary items

print("Customer dictionary items:")

for key, value in customer.items():
    print(f"{key}: {value}")

print("Customer dictionary keys only:")

for key in customer:
    print(key)
    # Exercise 5: Customer tier discounts

tier_discounts = {
    "bronze": 0.00,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Customer Tier:", customer["tier"])
print("Discount Rate:", discount_rate)
print("Final Price: $", final_price)
# Exercise 6: Apply discounts to multiple customers

customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "platinum"}
]

purchase_price = 300

for customer in customers:
    discount_rate = tier_discounts.get(customer["tier"], 0)
    discount_amount = purchase_price * discount_rate

    print(
        customer["name"],
        customer["tier"],
        "Discount: $",
        discount_amount
    )

    # Exercise 7: Nested dictionaries and low stock alerts

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            product,
            "LOW STOCK:",
            details["stock"],
            "units remaining"
        )

        # Exercise 8: Sales summary by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

print("Sales Summary by Region:")

for region in sorted(sales_summary):
    print(region, ":", sales_summary[region])