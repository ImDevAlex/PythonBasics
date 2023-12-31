class Library:
    def __init__(self, books, studentIds):
        self.books = books
        self.studentIds = studentIds
    def showAvailableBooks(self):
        for i in self.books:
            print(i)
    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"You borrowed {bookName}. Enjoy reading it")
    def returnBook(self, bookName):
        if bookName in self.books:
            self.books.append(bookName)
            print(f"You returned {bookName}. Hope you enjoyed reading it")
    def logIn(self, yourId):
        if yourId in self.studentIds.keys():
            print("You are successfully logged in.")
            userName = self.studentIds[yourId]
            print(f"Name: {userName}")
        else:
            print("Invalid user! Enter a registered username or create an account first.")
            exit()
    def registerId(self, newId, name):
        if newId in self.studentIds.keys():
            print("UserId already exists, choose a different Id and try to register again.")
        else:
            self.studentIds[newId] = name
            print(f"You've registered in the library.\nName: {name}\nYour userId: {newId}.\nRemember the Id next time.")

class Student:
    def requestBook(self):
        return input("Enter the name of the book you want to borrow: ")
    def returnBook(self):
        return input("Enter the name of the book you want to return: ")
    def registerId(self):
        return input("Choose a userId: ")
    def registerName(self):
        return input("Enter your name: ")
    def logIn(self):
        return input("Enter your Id: ")

def main():
    while True:
        print("Wellcome to the library\n1. Log in\n2. Create a new account\n3. Exit")
        # books = ["book1", "book2"]
        # ids = {'12345':'Alex', '54321':'Harry'}
        library = Library(["book1", "book2"], {'12345':'Alex', '54321':'Harry'})
        student = Student()
        choice = input("Enter your choice(1/2/3): ")
        if choice == '1':
            logInId = student.logIn()
            library.logIn(logInId)
            while True:
                print ("1. Show available books\n2. Request a book\n3. Return a book\n4. Exit")
                choice1 = input("Enter your choice(1/2/3/4/5): ")
                if choice1 == '1':
                    library.showAvailableBooks()
                elif choice1 == '2':
                    bookToBorrow = student.requestBook()
                    library.borrowBook(bookToBorrow)
                elif choice1 == '3':
                    bookToReturn = student.returnBook()
                    library.returnBook(bookToReturn)
                elif choice1 == '4':
                    break
                elif choice1 == '5':
                    print(library.studentIds)
                else:
                    print("Invalid Choice. Please enter a valid choice.")
        elif choice =='2':
            newId = student.registerId()  
            name = student.registerName()                     
            library.registerId(newId, name)
        elif choice == '3':
            break
        else:
            print("Invalid Choice. Please enter a valid choice.")



if __name__ == '__main__':
    main()
