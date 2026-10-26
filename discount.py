# 1.) First it starts from the top and makes its way down. It does this because the number isn't
# sufficient for the 500 total discount. However, it stops at the 200 and applies a 10% discount.
# 2.) It would have to be an 'and' statement because if it wasn't, then the if would automatically apply something to it.
# If you wanted it to apply something for the next variable then it may cause the code to error.
# 3.) One I can think about would be the when at checkout of a store & you put in your phone number/
# use a rewards card. This is because it applies a discount or even needs to add points into your account. 
# Now that I know more about python, I can see how certain steps can be overwritten with the introduction of new code and how it exactly 
# functions.



#Starter Code from Lab 5

total = float(input("Enter cart total: $"))

# --- Exercise 1 ---
#Add your if/elif/else here
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

#discount = 0 #replace with correct logic
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

# --- Exercise 2 ---

if final > 1000: # strictly greater than
    status = "manager_approval_required"
else:
    status = "auto_approved" 

# print(status)

# --- Exercise 3 ---

region = "South" # S is capitalized

extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else:
    extra_discount = 0

final = total * (1 - (discount + extra_discount))
print(final)

# --- Exercise 4 ---


customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03


# --- Exercise 5 ---

amount = 0
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 1000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

# --- Exercise 6 ---

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False #bool/caps it

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 10:
    vip_upgrade = True
else:
    vip_upgrade = False 

if (total_spent_this_year > 2000 or orders_this_year > 10) and has_outstanding_balance == False:
    vip_upgrade = False