# # 1. Honestly nothing much about lists was really surprising except for the fact that
# capitalizing words in a list will put them at the front of the list compared to lowercase
# words.

# 2. A real life example of using a list in python would be for managing inventory where instead
# of writing in each cell for each parcel or number of items a list can compile them and utilize it
# for easy functions and math.




print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])


print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")
inventory.append("tape")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# inventory.append("Zoo")
# inventory.append("zoo")
# inventory.append("Apple")
# inventory.append("1")
# inventory.append("11")
# inventory.append("4")
# inventory.append("%")
# inventory.append("-")

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

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2)) # 10 % discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter Above Threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")