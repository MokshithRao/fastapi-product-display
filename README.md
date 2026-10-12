# Product Display Application

A simple web application built using FastAPI, Jinja2, MySQL, and SQLAlchemy ORM to display product details stored in a MySQL database.

## Features

- Display all available products.
- View product ID, name, and price.
- Fetch product details dynamically from MySQL.
- Use SQLAlchemy ORM for database operations.
- Navigate between the home page and product list.

## Technologies Used

- Python
- FastAPI
- Jinja2
- MySQL
- SQLAlchemy ORM
- HTML

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/MokshithRao/fastapi-product-display.git
   cd fastapi-product-display
   ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Configure your MySQL database credentials in database.py.
5. Ensure your MySQL database and products table are created.

6. Run the application:
    ```bash
    uvicorn main:app --reload
    ```
Open the application in your browser:

http://127.0.0.1:8000
