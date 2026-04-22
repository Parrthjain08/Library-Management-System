 # ^ ISSUE BOOKS
def issue_books():
    name=input("Enter the book name: ")
    if name in books:
         books[name]=issued_books
         issued_books[name]=books
         print(f"{name} Book Issued")    
    else:
         print(f"{name} Book not available")     
