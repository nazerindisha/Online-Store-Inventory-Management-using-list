item_names=['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities=[10, 20, 15, 30]
item_prices=[50000,1000,1300,500]
cart=[]
def view_inventory():
    print("Inventory:")
    for i in range(len(item_names)):
        print(f"{i+1}. {item_names[i]} (Quantity: {item_quantities[i]},Prices:{item_prices[i]})")
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price=float(input("enter the price:"))
    item_names.append(name)
    item_quantities.append(quantity)
    item_prices.append(price)

    print("Item added successfully!")
    
def remove_item():
    name = input("Enter item name to remove: ")
    if name in item_names:
        index = item_names.index(name)
        item_names.pop(index)
        item_quantities.pop(index)
        item_prices.pop(index)
        print("Item removed successfully!")
    else:
        print("Item not found.")
def update_item():
    name = input("Enter item name to update: ")
    if name in item_names:
        index = item_names.index(name)
        new_quantity = int(input("Enter new quantity: "))
        item_quantities[index] = new_quantity
        new_prices=float(input("Enter new price:"))
        item_prices[index]=new_prices
        print("Item updated successfully!")
    else:
        print("Item not found.")

def add_to_cart():
    index = int(input("Enter item index to add to cart: "))
    quantity = int(input("Enter quantity: "))
    if 1 <= index <= len(item_names) and item_quantities[index-1] >= quantity:
        cart.append({
            "name": item_names[index-1],
            "price": item_prices[index-1],  
            "quantity": quantity
        })
        item_quantities[index-1] -= quantity
        print(f"{quantity} {item_names[index-1]} added to cart successfully!")
    else:
        print("Invalid item index or insufficient quantity.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Your Cart:")
    total_price = 0
    for item in cart:
        price = item["price"] * item["quantity"]  
        print(f"- {item['name']} (Quantity: {item['quantity']}, Price: {price:.2f})")
        total_price += price
    print(f"Total Price: {total_price:.2f}")
def checkout():
    global cart
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
        return
    
    print("Processing payment...")
    
    cart = []
    print("Checkout successful! Thank you for your purchase.")

     
    
while True:
    print("\nInventory Management Menu:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Checkout")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        add_to_cart()
    elif choice == "6":
        view_cart()
    elif choice == "7":
        checkout()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")   
