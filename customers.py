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