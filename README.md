# LEARNING OBJECTIVES

-   Design ERP system with postgres backend
-   Production grade security
-   Company authentication/sign in


# DB setup commands
CREATE DATABASE imperial_city_beef;
CREATE USER imperial_user WITH PASSWORD 'imperial_user';
ALTER ROLE imperial_user SET client_encoding TO 'utf8';
ALTER ROLE imperial_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE imperial_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE imperial_city_beef TO imperial_user;
