# Student API using Tornado

This is a simple RESTful API for managing a collection of students. It is built using the Tornado web framework in Python.

## Features

- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on student records.
- **RESTful Endpoints:** Well-defined endpoints for interacting with the API.
- **In-Memory Data:** For simplicity, the student data is stored in-memory. In a production setting, consider connecting to a database.
- **JSON Format:** Data is exchanged in JSON format.

## Getting Started

### Prerequisites

- Python 3.x
- Tornado (install using `pip install tornado`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amro-alasri/RESTFul_API_with_Tornado_Framework.git
   cd RESTFul_API_with_Tornado_Framework
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python student_API.py
   ```

   The server will start on `http://localhost:8888`.

## API Endpoints

### Get all students

```bash
curl http://localhost:8888/students
```

### To create a new student

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Student", "age": 25}' http://localhost:8888/students
```

### To update a student

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Student", "age": 30}' http://localhost:8888/students/1
```

### To delete a student

```bash
curl -X DELETE http://localhost:8888/students/1
```
