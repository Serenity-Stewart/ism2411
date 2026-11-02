# 1.)  I would describe it as a path/loop that sorts through data. The three steps is the initializor where 
# the machine is given what it needs, then the update where everything that must
# be added/changed/stopped is done, and then the read when you review it all 
#
# 2.)  When ran, we can see that the while loop is longer/has more lines of code than the loop
# version. However, while the for loop runs cleanly, it isn't very flexible. And on the other hand,
# while the while loop is longer and more cluttered, it is highly flexible when it comes to looking for something specific. 
#
# 3.) One example I will use was when I worked in retail and I watched my manager have to analyze/create the
# average daily sales revenue and what all went into it. the list has floats (of numbers) of each day.
# The accumulator added the sales revenue for each day, and then the final print was the average daily sales revenue. 




# --- Exercise 1 ---

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total +=sale
    print(f"Total: ${total}")

# --- Exercise 2 ---

total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total/ count
print(f"Total: ${total}")
print(f"Count: ${count}")
print(f"Average: ${average:.2f}")

# --- Exercise 3 ---

current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# --- Exercise 4 ---

count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${count_over_100}")

# --- Exercise 5 ---

for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

# --- Exercise 6 ---

total = 0
i = 0
while i <len(sales):
    total +=sales[i]
    i += 1

print(f"Total(while loop): ${total}")

# --- Exercise 7 ---

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0

disocunted_price = sale * (1 - discount)
print(
    f"${sale} -> {discount*100:.0f}% discount-> "
    f"${disocunted_price:.2f}"
)