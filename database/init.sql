CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_number TEXT NOT NULL,
    profile_picture TEXT,
    performance TEXT
);

CREATE TABLE test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    language TEXT,
    score INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
);


CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
);CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_number TEXT,
    performance TEXT,
    profile_picture TEXT
);

-- Optional: Insert a test student
INSERT INTO students (roll_number, performance, profile_picture)
VALUES ('12345', 'A+', '/static/images/default.jpg');
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    name TEXT
);

-- Add a demo user (you can log in using this)
INSERT INTO students (username, password, name)
VALUES ('student1', 'password123', 'John Doe');
