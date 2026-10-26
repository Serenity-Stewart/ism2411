# 3 . ) Ai was in fact used in exercise 5 to build my understanding on holes within my code. 
# 1 . ) The first one I noticed was the missing ":". I noticed it immediately as it's something we 
# do repeatedly in class. I believe this tells me that spotting error codes will be not as difficult
# as I once thought because I've simply come to recognize issues.
# 2 . ) It will apply a discount depending on the original products price and the tier in which it lands in. 
# (example; 200>gold, 150>silver, 50>bronze, 50<none) In the end, depending on the tier in which the price lands
# then it will return the discounted price if there is one.









# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350,  0.05):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier =="bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

 # --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---
orders = [ (200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | total: ${total:.2f}")

# --- Exercise 6 ---

x = 100       #GLOBAL X

def double_it():
    x = 999         #LOCAL X
    return x * 2

print(x)
print(double_it())
print(x)

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale       #Had to add a "+" sign because if you only left =, it would overide the previous statement where count = 0
print(f"Total: ${total}")

count = 0
for sale in sales:    #was missing the ":" - fixing the to be f-string
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):      #changed "<="" to "<" because if we chose to look for <= the it would tell python to look for something that isn't there
    print(sales[i])     
    i += 1

