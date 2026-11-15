
from __future__ import print_function

try:
    read_input = raw_input
except NameError:
    read_input = input

# Store all books
books = []


# Add a new book
def add_book():
    title = read_input("Enter book title: ")
    author = read_input("Enter author name: ")

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully!")


# Display all books
def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    print("\n===== BOOK LIST =====")

    for book in books:
        if book["available"]:
            status = "Available"
        else:
            status = "Borrowed"

        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)
        print("--------------------")


# Search for a book
def search_book():
    keyword = read_input("Enter book title to search: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower():
            print("Book found:", book["title"])
            print("Author:", book["author"])
            found = True

    if not found:
        print("Book not found.")


# Borrow a book
def borrow_book():
    try:
        book_id = int(read_input("Enter book ID: "))
    except ValueError:
        print("Enter a valid book ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed.")
            return

    print("Book ID not found.")


# Return a book
def return_book():
    try:
        book_id = int(read_input("Enter book ID: "))
    except ValueError:
        print("Enter a valid book ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book was not borrowed.")
            return

    print("Book ID not found.")


# Main menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = read_input("Enter your choice: ").strip()

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice!")
