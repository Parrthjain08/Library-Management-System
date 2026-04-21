#~ LIBRARY.PY

books={}
issued_books={}

 # ^ Add Books
def add_books():
    name=input("Enter the book name: ")
    books[name]=books
    print(f"{name}book added")
    

# ^ SHOW BOOKS
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books available")
        for b in books:
            print(b)   
                                                             


 # ^ ISSUE BOOKS
def issue_books():
    name=input("Enter the book name: ")
    if name in books:
         books[name]=issued_books
         issued_books[name]=books
         print(f"{name} Book Issued")    
    else:
         print(f"{name} Book not available")     


 # ^ RETURN BOOK
def return_books():
     name=input("Enter the books name: ")
     if name in issued_books:
         issued_books[name]=books
         books[name]=issued_books
         print(f"{name} books returned")
     else:
         print(f"{name} book not issued")


# ! MAIN BODY
def library():
    while True:
        print("1.add books")
        print("2.Show Books")
        print("3.Issue Books")  
        print("4.Return Books")
        print("5.Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
                print("Thank you")
                break      
        else:
            print("Invalid Choice")

     #? RUN
library()