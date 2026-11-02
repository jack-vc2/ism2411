# 1. The first bug I spotted was a missing colon on line 10. I noticed it immediately as 
# there was a red squiggly line under the for the loop showing that there was something missing.
# After the traceback I confirmed that the colon was the problem. I think this tells me that my 
# current debugging instincts are decent as I can recognize whats wrong with a code before running it.

# 2. apply_discount(price, tier) is a defined function that means it shows the price of an item after
# an applied discount based off that persons tier/membership. Its inputs are the price of the item and
# the tier which could be none, bronze, silver, or gold which determines the level of discount. A colleague
# could definetly use this without reading the body because its a simple if/else statement.

# 3. Disclosure: I used AI just to help with the debugging explanation for exercise 5.and

# - The ai helped my understanding because I understand more about indexes and the true purpose of colons.


# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on 250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold") #used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

#refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Order: ${price:.2f}, Tier: {tier}, Final Price: ${total:.2f}")

# Exercise 6

x = 100 #apple # global

def double_it():
    global x 
    # x = 999  # local another apple (not the same as before)
    return x * 2


print(x)
print(double_it())
print(x)