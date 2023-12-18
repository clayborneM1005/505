def teaspoon_to_cup(teaspoons):
    return teaspoons / 48  # 1 cup = 48 teaspoons

def cup_to_teaspoon(cups):
    return cups * 48  # 1 cup = 48 teaspoons

def tablespoon_to_cup(tablespoons):
    return tablespoons / 16  # 1 cup = 16 tablespoons

def cup_to_tablespoon(cups):
    return cups * 16  # 1 cup = 16 tablespoons

def quart_to_cup(quarts):
    return quarts * 4  # 1 quart = 4 cups

def cup_to_quart(cups):
    return cups / 4  # 1 quart = 4 cups

def main():
    print("Welcome to the Cooking Measurement Converter!")

    while True:
        print("\nChoose an option:")
        print("1. Teaspoon to Cup")
        print("2. Cup to Teaspoon")
        print("3. Tablespoon to Cup")
        print("4. Cup to Tablespoon")
        print("5. Quart to Cup")
        print("6. Cup to Quart")
        print("7. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            teaspoons = float(input("Enter the amount in teaspoons: "))
            cups = teaspoon_to_cup(teaspoons)
            print(f"{teaspoons} teaspoons is equal to {cups} cups.")
        elif choice == '2':
            cups = float(input("Enter the amount in cups: "))
            teaspoons = cup_to_teaspoon(cups)
            print(f"{cups} cups is equal to {teaspoons} teaspoons.")
        elif choice == '3':
            tablespoons = float(input("Enter the amount in tablespoons: "))
            cups = tablespoon_to_cup(tablespoons)
            print(f"{tablespoons} tablespoons is equal to {cups} cups.")
        elif choice == '4':
            cups = float(input("Enter the amount in cups: "))
            tablespoons = cup_to_tablespoon(cups)
            print(f"{cups} cups is equal to {tablespoons} tablespoons.")
        elif choice == '5':
            quarts = float(input("Enter the amount in quarts: "))
            cups = quart_to_cup(quarts)
            print(f"{quarts} quarts is equal to {cups} cups.")
        elif choice == '6':
            cups = float(input("Enter the amount in cups: "))
            quarts = cup_to_quart(cups)
            print(f"{cups} cups is equal to {quarts} quarts.")
        elif choice == '7':
            print("Exiting the Cooking Measurement Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()