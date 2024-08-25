
# Django Appium Automated Testing

This project demonstrates automated testing for a Django application using Appium and MySQL as the database. The setup uses Docker and Docker Compose for containerization.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Configuration](#configuration)
- [Running Tests](#running-tests)
- [Stopping the Application](#stopping-the-application)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.x](https://www.python.org/downloads/)
- [Appium](http://appium.io/docs/en/about-appium/intro/) (for mobile testing)


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/PydevAzmi/django-appium.git
    cd django-appium
    ```

2. **Set up the virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Build and run Docker containers**:

    ```bash
    docker-compose up --build
    ```

## Managing Database Migrations

If you need to apply migrations manually:

```bash
docker-compose exec web python manage.py migrate
```
## Configuration
You need to configure the environment variables before running the application.
modify the `docker-compose.yaml` and `.env` files for configuring the database, and more.

The setup uses MySQL. The connection details are managed in the `docker-compose.yaml` file. Update these settings as needed:
```yaml
  environment:
    MYSQL_ROOT_PASSWORD: your_password
    MYSQL_DATABASE: django_db
    MYSQL_USER: user
    MYSQL_PASSWORD: password
```

Create a `.env` file in the root directory of your project with the following variables:

```env
# Database settings
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=db
DB_PORT=3306

# Django settings
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
```




## Running Tests

To run the automated Appium tests:

1. Ensure the requirements is running inside the your computer (Appium, Android Emulator, adb server).

2. Run the test script using: `Will run local for now`
    ```bash
    python automated_test.py 
    ```



## Stopping the Application

To stop and remove all containers:

```bash
docker-compose down
```


## Troubleshooting
- MySQL Connection Issues: Ensure that the MySQL server is running and the credentials in settings.py are correct.
- Appium Issues: Use appium-doctor to diagnose and fix issues with your Appium setup.
- Virtual Environment Issues: If you encounter problems with package installations, make sure your virtual environment is activated.

## Contributing
- If you want to contribute to this project, please create a new branch and submit a pull request.

## License
- This project is licensed under the MIT License. See the LICENSE file for more details.

