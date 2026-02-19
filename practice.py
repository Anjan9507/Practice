expenses = []

def add_greeting():
    print("Hello from new feature branch!!!")


def print_menu():
    print("1. Add Expense")
    print("2. View all Expences")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")


def get_input():
    choices = ['1','2','3','4','5']
    while True:
        choice = input("Enter Choice: ")
        if choice not in choices:
            print("Invalid Choice")
            continue
        else:
            return choice


def add_expense():
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = (input("Enter Date: "))

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("Expense Added Sucessfully!")


def view_expenses():
    if expenses:
        for exp in expenses:
            print(f"Amount: {exp['amount']}, Category: {exp['category']}, Date: {exp['date']}")
    else:
        print("No Expenses to View")


def total_spending():
    if expenses:
        total = 0
        for exp in expenses:
            total += exp['amount']
        print(f"Total Amount Spent: {total}")
    else:
        print("No Amount to View")


def spending_by_category():
    if expenses:
        category = input("Enter Category to see the amount Spent: ")
        total = 0
        for exp in expenses:
            if exp['category'].lower() == category.lower():
                total += exp['amount']
        print(f"Total Amount spent on {category} is {total}")
    else:
        print("No Categories To View the Amount")


def execution(choice):
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_spending()
    elif choice == '4':
        spending_by_category()
    elif choice == '5':
        print("Exiting....")
        return False


def main():
    while True:
        add_greeting()
        print_menu()
        choice = get_input()
        result = execution(choice)
        if result is False:
            break


if __name__ == "__main__":
    main()

