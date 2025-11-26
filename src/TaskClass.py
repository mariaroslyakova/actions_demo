class Book:


    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__avalieble = True

    def setAuthor(self):
        return self.__author

    def setTitle(self):
        return self.__title

    def setYear(self):
        return self.__year

    def isAvalieble(self):
        return self.__avalieble

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getYear(self):
        return self.__year

    def isAvalieble(self):
        return self.__avalieble

    def mark_as_taken(self):
        self.__avalieble = False
        return self.__avalieble

    def mark_as_returned(self):
        self.__avalieble = True
        return self.__avalieble

    def __str__(self):
        if self.isAvalieble():
            self.__description = self.__title + ": " + self.__author + ", " + str(self.__year) + ", " + "Доступна"
        else:
            self.__description = self.__title + ": " + self.__author + ", " + str(self.__year) + ", " + "Недоступна"
        return self.__description


class PrintedBook(Book):
    def __init__(self,__title, __author, __year, pages, condition):
        super().__init__(__title, __author, __year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition=="плохая":
            self.condition="хорошая"
        elif self.condition=="хорошая":
            self.condition="новая"
        else:
            self.condition="новая"

    def __str__(self):
        return super().__str__() + ", " + str(self.pages) +" стр., "+ self.condition


class EBook(Book):
    def __init__(self,__title, __author, __year, file_size, format):
        super().__init__(__title, __author, __year)
        self.file_size = file_size
        self.format = format

    def download(self):
        print("Книга " + self.getTitle() + " загружается")

    def __str__(self):
        return super().__str__() + self.file_size +"Мб"+ self.format

class User:

    def __init__(self, name, __borrowed_books = []):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book: Book):
        if Book.isAvalieble:
            Book.mark_as_taken(self)
            self.__borrowed_books.append(book)

    def return_book(self, book: Book):
        if Book.isAvalieble == False:
            Book.mark_is_returned(self)
            self.__borrowed_books.remove(self,book.getTitle())

    def show_books(self):
        for book in self.__borrowed_books:
            print(book, end=" ")

    def _get__borrowed_books(self, __borrowed_books):
        __borrowed_books.sort()
        return __borrowed_books


class Librarian(User):

    def register_user(self, library: Library, user:User):
        library.add_user(user)

    def add_book(self, library: Library, book: Book):
        library.add_book(book)

    def return_book(self, book: Book):
        Library.return_book(book)



class Library:

    def __init__(self, __users=[], __books=[]):
         self.__users = __users
         self.__books = __books

    def add_book(self, book: Book):
        book = Book(book.getTitle(), book.getAuthor(), book.getYear())
        book.setTitle()
        book.setAuthor()
        book.setYear()
        self.__books.append(book)

    def remove_book(self, title):
        book1 = self.find_book(title)
        self.__books.remove(book1)

    def add_user(self, user: User):
        user= User(user.name)
        self.__users.append(user)

    def find_book(self, title):
        for book in self.__books:
            if book.getTitle() == title:
                return book

    def find_user(self, name):
        for user in self.__users:
            if user == name:
                return user

    def show_all_books(self):
        for book in self.__books:
            print(self.__books,end=", ")

    def show_avalible_books(self):
        for book in self.__books:
            if book.isAvalieble():
                print(book.getTitle(),end=", ")

    def lend_book(self, title, user_name):
        user1: User
        book1: Book
        for user in self.__users:
            if user_name == user.name:
                user1 = user
        for book in self.__books:
            if book.getTitle() == title:
                book1 = book
        user1.borrow(book1)

    def return_book(self, title, name):
        book = self.find_book(title)
        user = self.find_user(name)
        if book.isAvalieble()==False:
            user.return_books(self)

# --- создаём библиотеку ---
lib = Library()
# --- создаём книги ---
b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480,
"плохая")
# --- создаём пользователей ---
user1 = User("Анна")
librarian = Librarian("Мария")
# --- библиотекарь добавляет книги ---
librarian.add_book(lib, b1)
librarian.add_book(lib, b2)
librarian.add_book(lib, b3)
# --- библиотекарь регистрирует пользователя ---
librarian.register_user(lib, user1)
# --- пользователь берёт книгу ---
lib.lend_book("Война и мир", "Анна")
# --- пользователь смотрит свои книги ---
user1.show_books()
# --- возвращает книгу ---
lib.return_book("Война и мир", "Анна")
# --- электронная книга ---
b2.download()
# --- ремонт книги ---
b3.repair()
print(b3)

