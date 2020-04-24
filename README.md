# Imperial City Beef

ERP system and online store for hot dogs. This is a development project for learning purposes. Imperial City Beef is not a real company.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

[Python 3.6](https://www.python.org/downloads/release/python-360/)
[Postgres](https://www.postgresql.org/)

### Installing

Clone this repository

```
git clone https://github.com/abcmer/imperial-city-beef.git
```

Create and activate a virtual environment

```
cd imperial-city-beef
python3 -m venv venv
source venv/bin/activate
```

Install python dependencies

```
pip install -r requirements.txt
```

Create application db and user in postgres. Connect to your Postgres db server and run the following commands:

```CREATE DATABASE imperial_city_beef;
CREATE USER imperial_user WITH PASSWORD 'imperial_user';
ALTER ROLE imperial_user SET client_encoding TO 'utf8';
ALTER ROLE imperial_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE imperial_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE imperial_city_beef TO imperial_user;
```

Migrate and seed database. Change to the imperial_city_beef sub directory.

```
cd imperial_city_beef
python manage.py migrate
python manage.py loaddata ./erp/fixtures/initial_data.json
```

Start the development server

```
python manage.py runserver
```

Navigate to http://localhost:8000/erp in your web browser of choice. Enjoy!

## Built With

-   [Django](https://www.djangoproject.com/)
-   [Bootstrap](https://getbootstrap.com/)

## Learning Goals

-   Design E-commerce site for hot dogs
-   Google user authentication

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
