# Library Management System (Console Based)

library = {}

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # 1. Add Book
    if choice == "1":
        book_id = input("Enter Book ID: ").strip()

        if book_id in library:
            print("Book already exists.")
        else:
            name = input("Enter Book Name: ").strip()
            author = input("Enter Author Name: ").strip()

            try:
                quantity = int(input("Enter Quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                else:
                    library[book_id] = {
                        "name": name,
                        "author": author,
                        "quantity": quantity
                    }
                    print("Book added successfully.")
            except ValueError:
                print("Please enter a valid number for quantity.")

    # 2. View All Books
    elif choice == "2":
        if not library:
            print("No books available in library.")
        else:
            print("\n--- Available Books ---")
            for bid, data in library.items():
                print(f"ID: {bid} | Name: {data['name']} | Author: {data['author']} | Copies: {data['quantity']}")

    # 3. Issue Book
    elif choice == "3":
        book_id = input("Enter Book ID to issue: ").strip()

        if book_id not in library:
            print("Book not found.")
        else:
            if library[book_id]["quantity"] > 0:
                library[book_id]["quantity"] -= 1
                print("Book issued successfully.")
            else:
                print("Book not available (out of stock).")

    # 4. Return Book
    elif choice == "4":
        book_id = input("Enter Book ID to return: ").strip()

        if book_id not in library:
            print("Book not found.")
        else:
            library[book_id]["quantity"] += 1
            print("Book returned successfully.")

    # 5. Exit
    elif choice == "5":
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 to 5.")
