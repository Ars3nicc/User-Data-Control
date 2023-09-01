# Portal Information Controller
This application uses Django framework to manage the user data management. It implements basic CRUD operations and optimized search engine.

## UPDATED Information Controller Sample
Replaced particular parameters and repositioned template views for less complexity. To implement additional features to the system such as; improved search function, complemented design, page responsiveness and data analysis with visualization.

## TODO:
1. Implement relational database using PostgreSQL.
2. Implement GraphQL.
3. Create visual representation of database.
4. Improve search engine (fix model).

**To run the system:**
```
python manage.py runserver
```

## Creating Admin Superuser Account
You will need to create an admin account in order to access the Django admin server
#### In this case, it's located in the URL
```path('accounts/', include('django.contrib.auth.urls')),```
>Follow this quick steps to create an admin account
---
Initiating create superuser
```
python manage.py createsuperuser
```
Creating Username
```
Username: admin
```
Input Email Address, though it can be OPTIONAL (hit ENTER to skip creating email address)
```
Email address: // Skip this if you want to
```
Creating Password
```
Password: admin
Password (again): admin
```
Bypassing Validation of Password
```
Bypass password validation and create user anyway? [y/n]: y // Select YES
```
>Note that this project is for practice only to understand the fundamental concepts of Django Framework

Check out my portfolio for more information