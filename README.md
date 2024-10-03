Overview of the Flask Web Application
Purpose: The application serves as a simple user input form that allows users to submit their names and email addresses. The data entered by users is stored in a SQLite database for potential later use or analysis.

Core Components:

Frontend:

Built with HTML and Jinja2 templating, the frontend provides a user-friendly interface to collect input.
It includes a form where users can enter their names and email addresses.
Backend:

The backend is built using Flask, a lightweight web framework for Python.
It handles the application's logic, including routing requests, processing form submissions, and interacting with the database.
It contains routes for rendering the main page and processing form submissions.
Database:

The application uses SQLite as its database to store user data.
A SQLAlchemy ORM is used for database interaction, allowing for easy data manipulation without writing raw SQL queries.
User inputs are stored in a database table whenever a user submits the form.
Key Features:

User Input Form:

The main page displays a form with fields for users to enter their name and email.
Upon submission, the application processes the input and stores it in the database.
Flashing Messages:

After a successful submission, a success message is displayed to the user, confirming that their information has been stored.
