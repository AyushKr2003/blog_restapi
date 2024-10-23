# Blog API

A RESTful Blog API built using **Flask**, **SQLAlchemy**, and **Flask-JWT-Extended** for authentication. This API allows users to manage blog posts, categories, comments, and user accounts, with JWT-based authentication for protected routes.

## Features

- User registration and login with JWT authentication.
- Create, update, and delete posts and categories.
- Add, modify, and remove comments on posts.
- JWT token management with blocklist and token expiration handling.
- Automated cleanup of expired tokens using APScheduler.
- Swagger documentation for API endpoints.

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd blog-api
    ```


2. **Create a Virtual Environment**

    ```bash
    
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```
4. **Set up Environment Variables**
Create a `.env` file:

    ```makefile

    DATABASE_URI=sqlite:///blog.db
    JWT_SECRET_KEY=your_secret_key_here
    ```

5. **Initialize Database**

    ```bash
    flask db upgrade
    ```
6. **Run the Application**

    ```bash
    flask run
    ```

## Configuration
- JWT Access Token Expiration: Set to 24 hours by default. Modify in `app.py` if needed.
- Database: Uses SQLAlchemy for ORM. Ensure the correct `DATABASE_URI` is configured in your `.env` file.
- Swagger Documentation: Access the API documentation at `/swagger-ui`.

## Scheduler and Token Cleanup
The application uses APScheduler to automatically clean up blocklisted tokens older than two days.

To modify the cleanup interval, adjust the following code in `app.py`:

```python
scheduler.add_job(cleanup_blocklisted_tokens, 'interval', hours=24)
```

## API Documentation
The complete API documentation, including all endpoints and details, can be found [here](api_docs\README.md).

## Swagger Documentation

- Swagger UI provides an interactive interface to explore and test the API endpoints directly from your browser.
- You can access the API documentation at:
```
http://localhost:5000/swagger-ui
```
This provides an interactive UI to test the endpoints.

## Project Structure

```/project-root
│
├── /resources                        # Blueprints for API endpoints
├── /models                           # SQLAlchemy models
├── /migrations                       # Database migrations folder
├── /schemas                          # Marshmallo Schema
├── app.py                            # Application factory and entry point
├── db.py                             # Database initialization
├── readme_script_generator.py        # Script to generate doc for api from swagger-ui
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
```

## Usage
- Register a new user and log in to receive a JWT token.
- Use the JWT token in the Authorization header for protected routes.
- Example:
```makefile
Authorization: Bearer <your-token>
```
