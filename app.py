from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data: a list of students
students = []

@app.route('/')
def hello():
    return "Hello! Student API is Live!"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'student': student})

@app.route('/students', methods=['POST'])
def add_student():
    new_student = {
        'id': len(students) + 1,
        'name': request.json['name'],
        'grade': request.json['grade']
    }
    students.append(new_student)
    return jsonify({'student': new_student}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    return jsonify({'student': student})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    students.remove(student)
    return jsonify({'result': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
