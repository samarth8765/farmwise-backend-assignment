# Starting the Flask Application (Book Management System)

## Prerequisites

- Python 3.x installed
- PostgreSQL server running

## Running the Application

- You can either use this app or clone it from the GitHub repository.

  - To clone the app from the github repository, run the following command:

    ```bash
    git clone https://github.com/samarth8765/farmwise-backend-assignment.git
    ```

- Create a virtual environment for your project and activate it:

  For Unix or MacOS:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

  For Windows:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- Install all required Python packages using requirements.txt:

  ```bash
  pip install -r requirements.txt
  ```

- Configure the database

  - Pull the PostgreSQL docker image from Docker Hub:

    ```bash
    docker pull postgres
    ```

  - Run the PostgreSQL container:

    ```bash
    docker run --name postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
    ```

- Run the Flask application:

  ```bash
  python app.py
  ```

- Open the application at http://127.0.0.1:5000

## API Endpoints

1. Signup:

   - URL: /signup
   - Method: POST
   - Body:
   - username: String (required)
   - password: String (required)
   - Description: Registers a new user with the provided username and password.
   - Response: Confirmation message and status code.

2. Login:

   - URL: /login
   - Method: POST
   - Body:
   - username: String (required)
   - password: String (required)
   - Description: Authenticates the user. If successful, returns a JWT access token.
   - Response: JWT access token and status code.

3. Get Books:

   - URL: /books
   - Method: GET
   - Headers:
   - Authorization: Bearer <access_token>
   - Description: Retrieves a list of all books in the database. Requires JWT authentication.
   - Response: A list of books and status code.

4. Post Book:

   - URL: /books
   - Method: POST
   - Headers:
   - Authorization: Bearer <access_token>
   - Body: Book data including title, author, isbn, price, and quantity.
   - Description: Adds a new book to the database. Requires JWT authentication.
   - Response: Details of the added book and status code.

5. Get Book:

   - URL: /books/<isbn>
   - Method: GET
   - Headers:
   - Authorization: Bearer <access_token>
   - URL Parameters: isbn of the book.
   - Description: Retrieves details of a specific book by its ISBN. Requires JWT authentication.
   - Response: Book details and status code.

6. Update Book:

   - URL: /books/<isbn>
   - Method: PUT
   - Headers:
   - Authorization: Bearer <access_token>
   - URL Parameters: isbn of the book.
   - Body: Updated book data.
   - Description: Updates details of a specific book by its ISBN. Requires JWT authentication.
   - Response: Updated book details and status code.

7. Delete Book:

   - URL: /books/<isbn>
   - Method: DELETE
   - Headers:
   - Authorization: Bearer <access_token>
   - URL Parameters: isbn of the book.
   - Description: Deletes a specific book from the database using its ISBN. Requires JWT authentication.
   - Response: Confirmation message and status code.
