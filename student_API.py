import tornado.ioloop
import tornado.web
import json

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

class StudentHandler(tornado.web.RequestHandler):
    students = [
        Student(1, 'John Doe', 20),
        Student(2, 'Jane Doe', 22),
    ]

    def get(self, student_id=None):
        if student_id:
            student = next((student for student in self.students if student.student_id == int(student_id)), None)
            if student:
                self.write({'student_id': student.student_id, 'name': student.name, 'age': student.age})
            else:
                self.set_status(404)
                self.write({'error': 'Student not found'})
        else:
            students_list = [{'student_id': student.student_id, 'name': student.name, 'age': student.age} for student in self.students]
            self.write({'students': students_list})

    def post(self):
        student_data = json.loads(self.request.body.decode('utf-8'))
        new_student = Student(len(self.students) + 1, student_data['name'], student_data['age'])
        self.students.append(new_student)
        self.write({'student_id': new_student.student_id, 'name': new_student.name, 'age': new_student.age})

    def put(self, student_id):
        student = next((student for student in self.students if student.student_id == int(student_id)), None)
        if student:
            student_data = json.loads(self.request.body.decode('utf-8'))
            student.name = student_data['name']
            student.age = student_data['age']
            self.write({'student_id': student.student_id, 'name': student.name, 'age': student.age})
        else:
            self.set_status(404)
            self.write({'error': 'Student not found'})

    def delete(self, student_id):
        student = next((student for student in self.students if student.student_id == int(student_id)), None)
        if student:
            self.students.remove(student)
            self.write({'message': 'Student deleted successfully'})
        else:
            self.set_status(404)
            self.write({'error': 'Student not found'})

def make_app():
    return tornado.web.Application([
        (r'/students', StudentHandler),
        (r'/students/([0-9]+)', StudentHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
