# inventory.py
# Author: Logan Milancewich
# Module 10 Lab: Inventory List Manager

# Reflection questions:
# 1. I was surprised by how the sorting works with capital letters and lowercase letters.
# 2. Making a list of prices would have made it easier for me to work the register at my job where I had to manually input prices from a sheet of paper everytime.

print("--- Exercise 1: Build the List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #first item
print(inventory[-1]) #last item
middle = len(inventory) // 2 # calculate middle index
print(inventory[middle]) #middle item


print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) #first three items
print(inventory[-2:]) #last two items
print(inventory[::2]) #every 2nd item

print("--- Exercise 4: Modifying the List ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: ${total:.2f}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
print(f"Best: ${max(sales):.2f}")
print(f"Worst: ${min(sales):.2f}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2)) # apply 10% discount and round to 2 decimal places

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print("Count of high sales:", len(high_sales))
print("Average of high sales days:", sum(high_sales) / len(high_sales) if high_sales else 0)