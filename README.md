# Book Review API Backend

This repository contains the Django REST API backend for the Book Review application. It provides RESTful endpoints for user registration, authentication via JWT, book management, and reviews.

---

## Features

- User registration and JWT-based authentication
- CRUD operations for books and reviews
- Pagination, filtering, and ordering support
- Secure API endpoints with permissions
- CORS support for frontend connectivity

---

## Tech Stack

- Python 3.10
- Django 5.2.4
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (default, for development)
- Docker for containerization

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (for containerized deployment)
- AWS CLI (if deploying to AWS ECR/EC2)

### Environment Setup

1. Clone this repository:

    ```
    git clone https://github.com/yourusername/book-review-api-backend.git
    cd book-review-api-backend
    ```

2. Create and activate a virtual environment (optional if using Docker):

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Configure Django settings as needed (`settings.py`):

   - Set `ALLOWED_HOSTS` to include your deployment domain or IP (e.g., `'13.201.227.154'`)
   - Configure CORS (if needed)
   - Update database settings if using production DB

5. Run database migrations:

    ```
    python manage.py migrate
    ```

6. Run the development server (for local testing):

    ```
    python manage.py runserver
    ```

---

## Docker Deployment

### Build Docker Image

```
docker build -t book-review-api .
```

### Tag and Push to AWS ECR (replace placeholders)

```
docker tag book-review-api:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/book-review-api:latest
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/book-review-api:latest
```

### Run on EC2

```
sudo docker run -d -p 80:8000 <aws_account_id>.dkr.ecr.<region>.amazonaws.com/book-review-api:latest
```

---

## API Endpoints

| Path                 | Method | Description               |
|----------------------|--------|---------------------------|
| `/api/register/`      | POST   | Register new user          |
| `/api/token/`         | POST   | Obtain JWT token (login)   |
| `/api/token/refresh/` | POST   | Refresh JWT token          |
| `/api/books/`         | GET/POST | List/Create books         |
| `/api/books/<id>/`    | GET/PUT/DELETE | Retrieve/Update/Delete a book |
| `/api/reviews/`       | GET/POST | List/Create reviews       |
| `/api/reviews/<id>/`  | GET/PUT/DELETE | Retrieve/Update/Delete a review |

---

## Notes

- Make sure to whitelist frontend origins in CORS configuration if applicable.
- Use environment variables or secret management for sensitive data, keys, and credentials.
- For production, run the backend using Gunicorn (already set in Dockerfile).

---

## License

MIT License

---

## Contact

For questions or collaboration, please contact [kuldeep.mca2024@gmail.com]

