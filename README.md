# Description
This repository contains the final assignment for the Backend Developer Capstone Course of the Meta Backend Developer Professional Certificate on Coursera. It's a restaurant management system that provides a collection of API endpoints and a frontend for managing restaurant operations.

# Project Structure
The project is structured into two primary Django applications:

1. api: This app serves as the main API provider of the project.
2. restaurant: This app is responsible for the frontend and user-facing aspects of the system.

The littlelemon directory contains the main configuration and settings for the Django project.

# Install Dependencies
Use the following pipenv command to install the necessary dependencies:
```jsx
pipenv install
```
# Activate the Virtual Environment
```jsx
pipenv shell
```

<br>


# Database Configuration

The project uses MySQL as the default database. Below are the default database settings. You need to replace the placeholders with your MySQL database details:

```jsx
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',  # replace with your database name
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'admin',  # replace with your MySQL username
        'PASSWORD': '',   # replace with your MySQL password
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

```

"don't forget to change the  settings according to your local dataase setups"
<br>
<br>
# NOTE
The default username and password for the Django admin are provided inside the .env file for security, rather than directly in the README.
# Apply Database Migrations
Run the following commands to apply the database migrations:
```jsx
python manage.py makemigrations
python manage.py migrate

```
then run the server
```jsx
python manage.py runserver
```

# Setting Up Environment Variables

The restaurant app requires a username and password for authenticated API requests. Follow these steps to create a .env file in the restaurant app directory and add the following entries:

Inside the restaurant app folder, create a file called .env and place the following code inside it:

```jsx
USERNAME=your_username
PASSWORD=your_password
```
Replace "your_username" and "your_password" with a valid username and password, respectively.


Be aware that django-environ must be installed for this to work. Install this dependency by running pipenv install

# API Endpoints

The api app provides four main endpoints. Additional endpoints are available via the Djoser and SimpleJWT packages.

Each API request requires a SimpleJWT token for authorization. Pass the token in the header of the request as follows:
```jsx
{'Authorization': 'JWT <token>'}
```
# Testing API Endpoints
You can test the API endpoints using a tool like Insomnia. Follow these steps:


1. Add your username and password to the Form section in Insomnia to create a JWT token.
2. Add the following URL to create your access token:
```jsx
http://127.0.0.1:8000/api/token/login/
```
3. Post your request and get the access token.
4. Copy the access token and add it to the Auth section in Insomnia. Enter "JWT" in the PREFIX field and paste the access token in the TOKEN field.
5. Use the following API endpoints to test their respective functionality:

### Endpoints for `api` app
```jsx
http:127.0.0.1:8000/api/menu-items
http:127.0.0.1:8000/api/menu-items/{menu-itemId}
http:127.0.0.1:8000/api/bookings
http:127.0.0.1:8000/api/bookings/{bookingId}
```

<br>

http:127.0.0.1:8000/api/menu-items
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves all menu items | Yes | 200 |
| POST | Creates a menu item | Yes | 201 |
<br>

http:127.0.0.1:8000/api/menu-items/{menu-itemId}
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves the menu item details | Yes | 200 |
| PUT | Update the menu item | Yes | 200 |
| PATCH | Partially update the menu item | Yes | 200 |
| DELETE | Delete the menu item | Yes | 200 |
<br>

http:127.0.0.1:8000/api/bookings
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves all bookings | Yes | 200 |
| POST | Creates a booking | Yes | 201 |
<br>

http:127.0.0.1:8000/api/bookings/{bookingId}
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| GET | Retrieves the booking details | Yes | 200 |
| PUT | Update the booking | Yes | 200 |
| PATCH | Partially update the booking | Yes | 200 |
| DELETE | Delete the booking | Yes | 200 |
<br>

### Endpoints for `djoser` app
```jsx
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/
```
<br>

http://127.0.0.1:8000/auth/users/
| Method | Action | STATUS CODE | TOKEN AUTH |
| --- | --- | --- | --- |
| GET | Retrieves all users | 200 | No |
| POST | Creates a user | 201 | No |

💡 Please refer to the [Djoser documentation](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints) for further usage on these endpoints.
<br> <br>

### Endpoints for `simplejwt` app
```jsx
http:127.0.0.1:8000/api/token/login/
http:127.0.0.1:8000/api/token/refresh/
```
<br>

http://127.0.0.1:8000/api/token/login/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| POST | Generates access token and refresh token | Yes | 201 |
<br>

http://127.0.0.1:8000/api/token/refresh/
| Method | Action | TOKEN AUTH | STATUS CODE |
| --- | --- | --- | --- |
| POST | Generates a new access token | Yes | 201 |
<br>

# Testing
The project includes a suite of 12 tests to ensure the proper functioning of each API endpoint and HTTP method.


To run the tests, use the following command:

Run the tests
```jsx
python manage.py test
```
<br>

It should output something similar to this
```jsx
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 12 tests in 6.024s

OK
Destroying test database for alias 'default'...
```
<br>

<aside> The tests also indirectly test the restaurant models by creating entries in its database through the Django ORM..</aside>
