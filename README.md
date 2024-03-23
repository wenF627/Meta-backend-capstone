# Meta-backend-capstone
This is a capstone project for the Meta Back-End Development course

# Commands

``` bash
pipenv shell
pipenv install django
# create a django project
django-admin startproject littlelemon
# run development server
cd littlelemon
python manage.py runserver
# create a django app 
python manage.py startapp restaurant
# install client
pipenv install mysqlclient
```

```sql
create database littlelemon;
use littlelemon;
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
#user:super
#email: super@gmail.com
#password: super@123!
pip3 install djangorestframework
```

GET in 
http://localhost:8000/api/menu/1

```json
{
    "id": 1,
    "title": "Menu 1",
    "price": "123.00",
    "inventory": 4
}
```
GET in 
http://localhost:8000/api/menu

- Get all menus

POST http://localhost:8000/api/menu/

BODY
```json
{
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
}
```
RESULT
```json
{
    "id": 2,
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
}
```


GET in 
http://localhost:8000/api/booking/tables

```json
[
    {
        "id": 1,
        "name": "Booking 1",
        "number_of_guests": 6,
        "booking_date": "2023-06-06T17:41:53Z"
    }
]
```
POST http://localhost:8000/api/api-token-auth/
```json
{
    "token": "5f1a86694126b4550f59a09adeaf34e03675281f"
}
```

Add authorization to the endpoints, so you have to send a header in the request with the Authorization title: Token [VALUE]

```bash
pip install djoser
```

navigate to http://127.0.0.1:8000/auth/token/login/ to get the token  
```
user: "super  
password: "super@123!"
```

use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header

## Testing
```sql
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
```

```bash
python manage.py test
```

To run the available unit tests, open the Visual Studio terminal and use the following command: `python manage.py test tests/`. Make sure your virtual environment is activated, and you're in the 'littlelemon' directory before running this command.

You can check if the web application serves static HTML content, including images and styles, by visiting the '/restaurant' path.

For testing purposes, you can interact with the following API endpoints using tools like Insomnia or Postman, or simply use your web browser:

1. DJOSER endpoint for registering a new user via a POST request:
   `/auth/users/`

2. Logging in and getting an authentication token:
   `/api-token-auth/`

3. Logging in using the DJOSER endpoint:
   `/auth/token/login`

4. Menu items:
   - List of menu items: `/api/menu/`
   - Details of a specific menu item: `/api/menu/{menuItemId}`

5. Table reservations:
   - List of available tables: `/api/booking/tables/`
   - Details of a specific table reservation: `/api/booking/tables/{bookingId}`