# // --- exercise 5 --- 
#  I found that after running all of the type(), depending on what you put withing the brackets, 
# it determined what the outcome would be. type("12") = <class 'string'>, type(12) = <class 'integer'>, type(12.0) = <class 'float'>, 
# type(True) = <class 'bool'. Then, when I ran "5" + "3" it read it as a string and connected them into 53. However,
# when I typed it as 5 + 3 it read then as integers and added them to 8 as a regular calculator would. 

# // --- 3 Self-Assessment Questions ---
# 1.) It says that a "TpyeError" occurs as they cannot be merged until they are labeled as the same. More specifically, 
# the "" number was simply trying to attach to the other number, while the other number was attempting the merge completely with the string. 
# What the "TypeError" was trying to convay was that since they are of different labels, nothing can be done with the variables. 
# Therefore, it must be altered. 

# 2.) This is because putting the numbers into "" made them strings rather than integers/floats. Therefore, the computer
# simply connected them to be 53 instead of adding them arithmetically. By ensuring we use input(), we can always
# be certain that the numbers are corresponding and of the right label before going forward.

# 3.) I personally would use it for checkouts. When someone has a multiple of something in their cart then they can simply scan 
# and add the quantity amount. Or, to take it a step further they can search for that item before entering the store to ensure we
# are currently in holding of what they need. This is incredibly time effective and will help those in the log run.



# --- Exercise 1 ---

product = "apple"
unit_price = 2.99
quantity = 8
in_stock = True

print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(quantity))
print(type(in_stock))

# --- Exercise 2 ---

print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity:.2f})")

# --- Exercise 3 ---

product_in = input("product name: ")
price_in = float(input("Unit Price: "))
quantity_in = int(input("quantity: "))

print(f"{quantity_in} units of {product_in} at ${price_in:.2f} each = ${unit_price * quantity:.2f})")

# --- Exercise 4 ---

unit_cost = 0.50
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

print(f"product: {product}")
print(f"revenue: {margin: .2f}")
print(f"cost: ${unit_cost: .2f}")
print(f"margin: {margin: .2f}%")
