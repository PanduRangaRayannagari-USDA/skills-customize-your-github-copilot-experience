# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining API routes, validating JSON data with Pydantic models, and returning useful HTTP status codes. You will create a book catalog API that stores data in memory while the server is running.

## 📝 Tasks

### 🛠️ Create the API Models and Starter Endpoint

#### Description
Complete the starter project by defining the data models and adding a root endpoint that confirms the API is running. Start the server with `uvicorn main:app --reload` and visit the interactive documentation at `http://127.0.0.1:8000/docs`.

#### Requirements
Completed program should:

- Define a `Book` model with an integer `id`, a non-empty `title`, a non-empty `author`, and a `year` integer
- Define a separate `BookCreate` model for data submitted when creating a book
- Return a JSON message such as `{"message": "Book API is running"}` from `GET /`
- Display the automatically generated OpenAPI documentation at `/docs`


### 🛠️ Implement Book Collection Routes

#### Description
Add routes for listing all books and creating new books. Use the Pydantic model to validate incoming request bodies and assign each new book a unique integer ID.

#### Requirements
Completed program should:

- Return all books from `GET /books` with an HTTP 200 response
- Create a book from `POST /books` and return the created book with an HTTP 201 response
- Reject requests with missing or invalid fields with a validation error response
- Assign a new ID without requiring the client to provide one
- Preserve created books in the in-memory collection until the server restarts


### 🛠️ Add Single-Book Lookup and Tests

#### Description
Add a route that retrieves one book by ID and write tests using FastAPI's `TestClient`. Test both successful requests and the error case for an ID that does not exist.

#### Requirements
Completed program should:

- Return the matching book from `GET /books/{book_id}` with an HTTP 200 response
- Return an HTTP 404 response with a helpful detail message when the ID does not exist
- Include at least one test for the root or list endpoint
- Include at least one test that creates a book and checks the response status and fields
- Include at least one test for the missing-book 404 response
