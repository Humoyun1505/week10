products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}
cart = ["101", "105", "105", "999", "103", "105"]

total = 0.0

for barcode in cart:
    if barcode in products:
        name, price = products[barcode]
        print(f"{name}: ${price:.2f}")
        total += price
    else:
        print(f"Item {barcode} not found.")

print("-" * 20)
print(f"Grand Total: ${total:.2f}")
