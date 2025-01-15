from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
        {'title': 'Title One', 'author': 'Author One', 'category' : 'science'},
        {'title': 'Title Two', 'author': 'Author Two', 'category' : 'science'},
        {'title': 'Title Three', 'author': 'Author Three', 'category' : 'history'},
        {'title': 'Title Four', 'author': 'Author Four', 'category' : 'history'},
        {'title': 'Title Five', 'author': 'Author Two', 'category' : 'science'},
]


@app.get("/books") #--> creating an API endpoint
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#We also can mix dinamyc path parameters with query parameters as follows:
@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author : str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('author').casefold() == book_author.casefold() and
                book.get('category') == category.casefold()):
            books_to_return.append(book)
    return books_to_return

#Example of POST request
@app.post('/books/create_book')
async def create_new_book(new_book = Body()):
    BOOKS.append(new_book)

#Example of PUT request
@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

#Example of DELETE request
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
@app.get('/books/assignment/{author_name}')
async def assignment_task(author_name : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return
