# This function prepares codes for book titles stored in user file


def book_titles(user_file):
    file = open(user_file)  # select the file containing book names
    list_of_books = file.readlines()  # store the book names in LIST
    num_of_books = len(list_of_books)  # count the number of books in the list

    print(f"Books = {list_of_books}")  # Print the list of books
    print(f"Number of books = {len(list_of_books)}")  # Print the number of books

    for book in list_of_books:
        # Not last book
        if list_of_books.index(book) < (num_of_books - 1):
            num_of_char_in_book_name = len(book) - 1  # Ignore /n from count
            initial_char_in_book_name = book[0].upper()  # Take initial of book and capitalize it
            print(f"{initial_char_in_book_name}{num_of_char_in_book_name}")
        # Last book
        else:
            num_of_char_in_book_name = len(book)  # since it is last element there is no \n
            initial_char_in_book_name = book[0].upper()  # Take initial of book and capitalize it
            print(f"{initial_char_in_book_name}{num_of_char_in_book_name}")
    # Close file
    file.close()


my_file = input("Please enter the path for your file: ")
book_titles(my_file)
