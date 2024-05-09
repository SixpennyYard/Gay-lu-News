# Article Generation Website

This project is a Flask-based web application that allows users to generate and manage articles. It provides functionalities for user registration, login, article creation, modification, deletion, and search.

## Features

- **User Authentication**: Users can register an account with a unique username and email. Passwords are securely hashed before storing in the database. Registered users can login to access additional features.
  
- **Article Management**: Registered users can create, edit, and delete articles. Each article includes a title, summary, content, author, and publication date.
  
- **Search Functionality**: The website offers a search functionality to find articles based on keywords present in the title or summary.

## Technologies Used

- **Flask**: The web application framework used for building the backend of the website.
  
- **Flask-Login**: Provides user session management and authentication features.
  
- **Werkzeug**: Used for password hashing and verification.
  
- **HTML/CSS**: Frontend design and layout are created using HTML and CSS. *(@Akok0 and Achille, two classmate, helped me)*

  
- **CSV Data Storage**: Article data is stored in CSV files for simplicity. That was a constraint imposed by my professor, requiring the use of CSV. However, for production use, a more scalable solution, such as implementing a database, can be considered.

## Usage

1. Clone the repository to your local machine.
  
2. Install the required dependencies using `pip install -r requirements.txt`.
  
3. Run the Flask application by executing `python app.py` in the terminal.
  
4. Access the website by navigating to `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
