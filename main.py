def main():
    choice = 0
    books = []
    while 0 <= choice < 4:
        print()
        print("Library Manager")
        print("=" * 9)
        print("1. Add a Book")
        print("2. Find a Book")
        print("3. Show all Books")
        print("4. Exit \n")

        choice = int(input())

        if choice == 1:
            print("Adding a Book")
            print("=" * 18)
            title = input("Enter the book's title: ")
            gender = input("Enter the book's gender: ")
            author = input("Enter the book's author: ")
            books.append([title, gender, author])

        elif choice == 2:
            print("Find a Book")
            print("=" * 18)
            search_word = input("Enter search word: ")
            for book in books:
                if search_word in book:
                    print(f"{book} \n")

        elif choice == 3: 
            print()
            print("Showing all Books")
            print("=" * 18)
            for book in books:
                print(f"{book} \n")

        else:
            choice == 4
            print("Exiting program")


if __name__ == "__main__":
    main()