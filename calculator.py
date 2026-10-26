# --- Self-Assessment Questions ---
# 1.) It made a slightly wong answer. It changed the net_profit and the discounted revenue - overall altering
# certain aspects of the answer.
# 2.) We can use this when describing how many students can fit into a classroom or how many people
# can attend a business meeting at once. This way, no one is excluded due to a miscalculation.
# 3.) I believe I feel least confident in the "print" aspect because as we go on, the more complex they become.
# I just feel as if I'll fail to keep up with everything that gets added to it. However, as I get these practices in the labs 
# I feel I'm getting a better understanding as we go. 




# --- Exercise 1 ---

price = 50
quantity = 12
revenue = price * quantity

#,.2f has 2 jobs -> thousand seperator & 2 decimal places 
print(f"Revenue: ${revenue:,.2f}")


# --- Exersice 2 ---

cost = 32
price = 50
margin = (price - cost) / price #margin stays as decimal 
print(f"Margin: {margin:.1%}")

# --- Exercise 3 ---

   # Product A wins if margin_a > margin_b
       # Product A margin = 60%
       # Product B margin = (80-60)/80 = 25%
margin_a = 0.50
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# --- exercise 4 ---

is_premium = price > 100 and margin > 0.3 #remember to review basic logic operators
print(f"Is premium: {is_premium}")

# --- exercise 5 ---

print(17/5) # Shows the complete amount including decimals. ex.) how many phones can fit in a box?
print(17//5) # shows the exact amount that can fit (no decimal) ex.) 
print(17%5) # It shows how many is left over after the equation


# --- exercise 6 ---

product = input("Enter the product name")
retail_price = float(input("Enter the retail price sold: "))
quantity_sold = int(input("Enter the quantity sold: "))
discount_pct = int(input("Enter the discount percentage: "))
cost = float(input("Enter the cost: "))
print("="*50)
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1-discount_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

print(f"Product: {product}")
print(f"Revenue: {revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross margin: {gross_margin:.1%}")
print(f"net_profit: ${net_profit:,.2f}")

# --- exercise 7 ---

#all upercases are constants
BOX_SIZE = 24
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE
loose_items = items_ordered % BOX_SIZE
exact_fit = loose_items == 0
print(f"Full_boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

