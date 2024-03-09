class library:
    books = ["Harry Porter", "Jungle Book", "Dark Night"]
    noOfBooks = 3
    
    def addbook(self, book):
        if book in self.books:
            print ("Book is already available in the library")
            return
        self.books.append(book)
        self.noOfBooks +=1
        print (book + " has been added succesfully.")
    
    def borrowBook (self, book):
        if book not in self.books:
            print("The book is not available in our library.")   
            return
        self.books.remove(book)
        self.noOfBooks -=1
        print (book + " has been burrowed succesfully.")

    def returnbook(self, book):
        if book in self.books:
            print ("This book was not burrowed")
            return
        self.books.append(book)
        self.noOfBooks +=1
        print (book + " has been returned succesfully.")


fssLibrary = library()
while True:
    choice = input("Enter [0]To Exit [1]To view available Books [2]To add Book [3]To issue Book [4]To return book \n")
    if int(choice) == 0:
         break
    elif int(choice)== 1:
        print (fssLibrary.books)
    elif int(choice) == 2:
        bookname = input("Add a book name:  ")
        fssLibrary.addbook(bookname)
    elif int(choice) == 3:
        bookname = input("Add the name of book to be borrow:  ")
        fssLibrary.borrowBook(bookname)
    elif int(choice) == 4:
        bookname = input("Add a name of the book that you borrowed previously:  ")
        fssLibrary.returnbook(bookname)
    else:
         break
    print("----------------------------")