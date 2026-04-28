from datetime import datetime, timedelta

books = []
issued_books = {}

# ADD BOOK
def add_books():
    name = input("\nEnter book name: ")
    
    if name in books:
        print("Book already exists")
    else:
        books.append(name)
        print("Book added")


# SHOW BOOKS
def show_books():
    print("\nAvailable Books:")
    if not books:
        print("No books available")
    else:
        for b in books:
            print("-", b)


# ISSUE BOOK
def issue_books():
    name = input("\nEnter book name: ")

    if name in books:
        student = input("Enter student name: ")
        days = int(input("Enter days: "))

        return_date = datetime.now() + timedelta(days=days)

        issued_books[name] = {
            "student": student,
            "return_date": return_date
        }

        books.remove(name)

        print(f"{name} issued to {student}")
        print("Return by:", return_date.date())

    else:
        print("Book not available")


# SIMPLE FINE
def calculate_fine(days_late):
    if days_late <= 7:
        return days_late * 10
    elif days_late <= 14:
        return days_late * 20
    else:
        return days_late * 60


# RETURN BOOK
def return_books():
    name = input("\nEnter book name: ")

    if name in issued_books:
        record = issued_books[name]
        today = datetime.now()
        due = record["return_date"]

        if today > due:
            late_days = (today - due).days
            fine = calculate_fine(late_days)

            print(f"Late by {late_days} days")
            print(f"Fine = Rs {fine}")
        else:
            print("Returned on time")

        books.append(name)
        del issued_books[name]

        print("Book returned")

    else:
        print("Book not issued")


# MAIN
def library():
    print("\nNOTICE:")
    print("Fine for late return:")
    print("1st week: 10 Rs/day")
    print("2nd week: 20 Rs/day")
    print("3rd week: 60 Rs/day\n")

    while True:
        print("\n1.Add Book")
        print("2.Show Books")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_books()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_books()
        elif choice == "4":
            return_books()
        elif choice == "5":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice")


library()
