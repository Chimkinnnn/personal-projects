import sqlite3 as sql


# Insert the following data into its corresponding tables
# authors table data
authors_data = [
    ('Joanne Rowling', 'Rowling', 'J.K. Rowling'),
    ('George Raymond Richard Martin', 'Martin', 'George R.R. Martin'),
    ('John Ronald Reuel Tolkien', 'Tolkien', 'J.R.R. Tolkien'),
    ('Stephen Edwin King', 'King', 'Stephen King'),
    ('Agatha Mary Clarissa Christie', 'Christie', 'Agatha Christie')
]

# genres table data
genres_data = ['Fantasy', 'Mystery', 'Horror', 'Thriller', 'Adventure']

# students table data
students_data = [
    ('John Dela Cruz', 'BS in Computer Science', 'john.cruz@email.com'),
    ('Jane Smith', 'BS in Information Technology', 'jane.smith@email.com'),
    ('Peter Jones', 'BS in Biology', 'peter.jones@email.com'),
    ('Maria Santos', 'BS in Psychology', 'maria.santos@email.com'),
    ('David Lee', 'BS in Computer Science', 'david.lee@email.com')
]

# books table data
books_data = [
    ('Harry Potter and the Sorcerer\'s Stone', '9780747532743', 1997, '1st Edition'),
    ('A Game of Thrones', '9780553103540', 1996, '1st Edition'),
    ('The Hobbit', '9780395071221', 1937, 'Original'),
    ('The Shining', '9780385121675', 1977, '1st Edition'),
    ('And Then There Were None', '9780007136834', 1939, 'Reprint'),
    ('It', '9780670813025', 1986, '1st Edition'),
    ('The Fellowship of the Ring', '9780618640157', 1954, '2nd Edition')
]


conn = connect() #Input your database filename here
cursor = conn.cursor()

cursor.execute()
