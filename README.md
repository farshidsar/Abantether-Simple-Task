# AbanTask Exchange

A Simple Task for Abantether Django-based cryptocurrency exchange service.

## Requirements

- Docker
- Docker Compose

## Setup

1. **Build and start the Docker containers:**

    ```bash
    docker-compose up --build
    ```

2. **Apply database migrations:**

    ```bash
    docker-compose exec web python manage.py migrate
    ```

3. **Seed the database with initial data:**

    ```bash
    docker-compose exec web python manage.py seed
    ```

4. **Run the tests:**

    ```bash
    docker-compose exec web python manage.py test
    ```

## API Endpoints

### Buy Crypto

**URL:** `/api/buy/`

**Method:** `POST`

**Payload:**

```json
{
    "crypto_name": "Bitcoin",
    "amount": 1
}
```

**Response:**
```json
{
    "success": true,
    "message": "Crypto bought successfully"
}
```


### Final Steps

1. **Apply Migrations:**

    ```bash
    docker-compose exec web python manage.py migrate
    ```

2. **Seed Data:**

    ```bash
    docker-compose exec web python manage.py seed
    ```

3. **Run Tests:**

    ```bash
    docker-compose exec web python manage.py test
    ```

With these steps, your application should be set up, seeded with initial data, and ready to run. You can also run tests to verify the functionality.

Also Django default admin is ok. 
admin/
By Farshid Sargheini.