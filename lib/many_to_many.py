class Book:
    _all_books = []

    def __init__(self, title):
        self._title = title
        Book._all_books.append(self)

    @property
    def title(self):
        return self._title

    @classmethod
    def all_books(cls):
        return cls._all_books


class Author:
    _all_authors = []

    def __init__(self, name):
        self._name = name
        self._contracts = []
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract._all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls._all_contracts if contract.date == date]
# Creating authors
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# Creating books
book1 = Book("The Art of Python")
book2 = Book("Data Science Essentials")

# Authors signing contracts for books
contract1 = author1.sign_contract(book1, "2022-03-09", 10)
contract2 = author1.sign_contract(book2, "2022-03-10", 15)
contract3 = author2.sign_contract(book1, "2022-03-11", 12)

# Retrieving all authors, books, and contracts
all_authors = Author.all_authors()
all_books = Book.all_books()
all_contracts = Contract.all_contracts()

# Retrieving contracts and books for a specific author
author1_contracts = author1.contracts()
author1_books = author1.books()

# Retrieving contracts by date
contracts_by_date = Contract.contracts_by_date("2022-03-10")

# Calculating total royalties for an author
author1_total_royalties = author1.total_royalties()

# Printing results
print("All Authors:", [author.name for author in all_authors])
print("All Books:", [book.title for book in all_books])
print("All Contracts:", [(contract.author.name, contract.book.title) for contract in all_contracts])
print(f"Contracts by Date (2022-03-10): {[(contract.author.name, contract.book.title) for contract in contracts_by_date]}")
print(f"Author1's Contracts: {[(contract.book.title, contract.royalties) for contract in author1_contracts]}")
print(f"Author1's Books: {[book.title for book in author1_books]}")
print(f"Author1's Total Royalties: {author1_total_royalties}%")
