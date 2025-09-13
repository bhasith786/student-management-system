from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

class Student:
    def __init__(self, name, roll_no, age, marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks
    
    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "age": self.age,
            "marks": self.marks
        }

class StudentManagement:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, roll_no, age, marks):
        self.students.append(Student(name, roll_no, age, marks))
    
    def get_all_students(self):
        return [s.to_dict() for s in self.students]

    def search_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s.to_dict()
        return None
    
    def update_student(self, name, roll_no, age, marks):
        for s in self.students:
            if s.roll_no == roll_no:
                s.name, s.age, s.marks = name, age, marks
                return True
        return False
    
    def delete_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                return True
        return False

sm = StudentManagement()

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(sm.get_all_students())

@app.route("/student", methods=["POST"])
def add_student():
    data = request.json
    sm.add_student(data["name"], data["roll_no"], data["age"], data["marks"])
    return jsonify({"message": "Student added successfully"})

@app.route("/student/<int:roll_no>", methods=["GET"])
def get_student(roll_no):
    student = sm.search_student(roll_no)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route("/student/<int:roll_no>", methods=["PUT"])
def update_student(roll_no):
    data = request.json
    updated = sm.update_student(data["name"], roll_no, data["age"], data["marks"])
    if updated:
        return jsonify({"message": "Student updated successfully"})
    return jsonify({"error": "Student not found"}), 404

@app.route("/student/<int:roll_no>", methods=["DELETE"])
def delete_student(roll_no):
    deleted = sm.delete_student(roll_no)
    if deleted:
        return jsonify({"message": "Student deleted successfully"})
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
