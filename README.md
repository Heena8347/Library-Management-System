# Library-Management-System

This repository hosts a simple command-line based Library Management System built with Python. It demonstrates fundamental programming concepts, including functions and basic file I/O operations, to manage a collection of books.

Features
- Add Books: Easily add new books to the library's inventory.
- View Books: See all books currently available in the library.
- Borrow Books: Simulate borrowing a book, moving it from available stock to borrowed status.
- Return Books: Simulate returning a book, moving it back from borrowed status to available stock.
How it Works (Core Concepts)
- This system operates by interacting with two plain text files, which serve as its "database":

- totalbooks.txt: Stores a list of all books currently available in the library. Each book title is on a new line.
- rent.txt: Stores a list of all books currently borrowed out. Each borrowed book title is on a new line.
  
The Python functions read from and write to these files to update the library's status.
