
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 6.99,
    "Salad": 4.99,
    "Coke": 1.99,
    "Water": 0.99
}

customer_order = []

def show_menu():
    print("Menu Card")
    print("-------------------------------")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_order():
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ").capitalize()
        if item == 'Done':
            break
        elif item in menu:
            customer_order.append(item)
        else:
            print("Invalid item! Please choose from the menu.")

def calculate_total():
    total = sum(menu[item] for item in customer_order)
    return total

def generate_bill():
    print("Order Details")
    print("-------------------------------")
    for item in customer_order:
        print(f"{item}: ${menu[item]}")
    total_amount = calculate_total()
    print("-------------------------------")
    print(f"Total: ${total_amount}")

def main():
    print("Welcome to the Restaurant!")
    show_menu()
    take_order()
    generate_bill()
    print("Thank you for dining with us!")

if __name__ == "_main_":
    main()