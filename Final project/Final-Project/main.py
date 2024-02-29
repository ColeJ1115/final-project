import booksclass

def check_out(book_list):
    for index, book in enumerate(book_list, start=1):
        if book.is_available:
            print(
                f"{index}. {book.title}, by {book.author}, Available: {book.is_available}, Condition: {book.condition_status()} ")
    checkout_num = int(input('Which book would you like to check out? '))
    if 1 <= checkout_num < len(book_list) + 1:
        checkout_index = checkout_num - 1
        checkout_name = book_list[checkout_index]
        checkout_name.check_out()
def return_books(book_list):
    for index, book in enumerate(book_list, start=1):
        if book.is_available == False:
            print(
                f"{index}. {book.title}, by {book.author}, Available: {book.is_available}, Condition: {book.condition_status()} ")
    return_num = int(input('Which book would you like to return? '))
    if 1 <= return_num < len(book_list) + 1:
        return_index = return_num- 1
        return_name = book_list[return_index]
        return_name.book_return()

def display_books(book_list):
    for index, book in enumerate(book_list, start=1):
        condition_status = book.condition_status()
        print(
            f"{index}. {book.title}, by {book.author}, Available: {book.is_available}, Condition: {condition_status} ")


def search_books_by_title(book_list, title_query):
    found_books = [book for book in book_list if title_query.lower() in book.title.lower().split()]
    if found_books:
        print("Found Books:")
        for index, book in enumerate(found_books, start=1):
            condition_status = book.condition_status()
            print(
                f"{index}. {book.title}, by {book.author}, Available: {book.is_available}, Condition: {condition_status} ")
    else:
        print("No books found matching your title search.")

def search_books_by_author(book_list, author_query):
    found_books = [book for book in book_list if author_query.lower() in book.author.lower().split()]
    if found_books:
        print("Found Books:")
        for index, book in enumerate(found_books, start=1):
            condition_status = book.condition_status()
            print(
                f"{index}. {book.title}, by {book.author}, Available: {book.is_available}, Condition: {condition_status} ")
    else:
        print("No books found matching your author search.")

def add_book():
    n_condition = int(input('On a scale of 1 - 5 what is the condition of the book? '))
    if n_condition < 2:
        print('That book is to damaged to donate')
    else:
        n_authors = []
        n_title = input('What is the title of the book? ').title()
        author_amount = int(input('How many authors are there?'))
        for _ in range(0, author_amount):
            n_author = input('What is the name of the author').title()
            n_authors.append(n_author)
        return booksclass.Books(n_title, n_authors, True, n_condition)

def main():
    book_list = [
        booksclass.Books('To Kill a Mocking Bird', 'Harper Lee', True, 5),
        booksclass.Books('1984', 'George Orwell', True, 5),
        booksclass.Books('Pride and Prejudice', 'Jane Austen', True, 5),
        booksclass.Books('The Great Gatsby', 'F. Scott Fitzgerald', True, 5),
        booksclass.Books("To Kill a Mockingbird", "Harper Lee", True, 5),
        booksclass.Books("The Catcher in the Rye", "J.D. Salinger", True, 5),
        booksclass.Books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", True, 5),
        booksclass.Books("The Lord of the Rings", "J.R.R. Tolkien", True, 5),
        booksclass.Books("The Hunger Games", "Suzanne Collins", True, 5),
        booksclass.Books("The Da Vinci Code", "Dan Brown", True, 5),
        booksclass.Books("The Alchemist", "Paulo Coelho", True, 5),
        booksclass.Books("The Picture of Dorian Gray", "Oscar Wilde", True, 5),
        booksclass.Books("The Scarlet Letter", "Nathaniel Hawthorne", True, 5)
    ]
    while True:



        choice = input('What would you like to do with the books? (Return, Check out, Display, Search, Donate book, or Exit Program)').lower()
        if choice == 'display':
            display_books(book_list)
        elif choice == 'return':
            return_books(book_list)
        elif choice == 'check out':
            check_out(book_list)
        elif choice == 'search':
            search_criteria = input("Do you want to search by title or author? ").lower()
            search_query = input("Enter your search: ").lower()
            if search_criteria == 'title':
                search_books_by_title(book_list, search_query)
            elif search_criteria == 'author':
                search_books_by_author(book_list, search_query)
            else:
                print("Invalid search criteria. Please enter 'title' or 'author'.")
        elif choice == 'donate book' or 'donate':
            donated_book = add_book()
            book_list.append(donated_book)
        elif choice == 'exit program':
            print('Thanks for visiting the library')
            break
        else:
            print('That is not a valid option.')



if __name__ == '__main__':
    main()