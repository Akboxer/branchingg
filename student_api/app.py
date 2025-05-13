from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
students = {
    1: {"name": "Alice", "age": 20},
    2: {"name": "Bob", "age": 22}
}

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get one student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_id = max(students.keys(), default=0) + 1
    students[new_id] = data
    return jsonify({"id": new_id, "student": data}), 201

# Update a student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    students[student_id] = data
    return jsonify({"message": "Student updated", "student": data})

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id in students:
        deleted = students.pop(student_id)
        return jsonify({"message": "Student deleted", "student": deleted})
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

