# Self Asssessment
# 1. The first bug I noticed was the missing colon in the for loop. I found it by reading the error message that came up.
# 2. apply_discount(price, tier) takes a price and a discount tier as inputs. It checks which tier the customer has and subtracts the correct percentage from the price. It returns the discounted price, so a colleague could usethe function without needing to read how it works.
# 3. No AI used.




# Exercise 1 

#define calclulate tax function

def calculate_tax(price, rate):
    return price * rate

# call the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85 
    elif tier == "silver":
        return price * 0.9  
    elif tier == "bronze":
        return price * 0.95  
    else:
        return price 

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    discounted_price = apply_discount(price, tier)
    print(f"{tier}: ${discounted_price:.2f}")

# Exercise 3

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

#refactor intor a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")


# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")




# Exercise 6

x = 100

def double_it():
    x = 999
    return x*2

print(x)
print(double_it())
print(x)



