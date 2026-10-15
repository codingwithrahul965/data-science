menu= {
    'pizza': 40,
    'pasta': 50,
    'burger': 30,
    'fries': 20,
    'coffee': 10,
}

print("welcome to the restaurant ")
print("pizza: Rs 40")
print("pasta: Rs 50")
print("burger: Rs 30")
print("fries: Rs 20")
print("coffee: Rs 10")


order_total = 0
item1 = input("what would you like to order? ")
if item1 in menu:
    order_total += menu[item1]   #0 + item price
    print(f"{item1} added to your order. Total: Rs {order_total}")
else:
    print("Sorry, we don't have that item.")
   
another_order= input("Would you like to order another item? (yes/no) ")
if another_order == 'yes':
    item2 = input("what would you like to order? ")
    if item2 in menu:
        order_total += menu[item2]   #0 + item price
        print(f"{item2} added to your order. Total: Rs {order_total}")
    else:
        print("Sorry, we don't have that item.")

print(f"Your final order total is: Rs {order_total}")        