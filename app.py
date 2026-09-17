from flask import Flask,jsonify,request
from database import Database
from student import Student

app=Flask(__name__)
database=Database()


@app.route("/students",methods=["GET"])
def get_students():
    students=database.get_student()
    student_data=[]
    department=request.args.get("department")
    age=request.args.get("age")
    for student in students:
        if department and student.department!= department:
            continue
        if age and student.age<int(age):
            continue
        student_dict={
            "student_id":student.student_id,
            "name":student.name,
            "age":student.age,
            "gender":student.gender,
            "department":student.department,
            "email":student.email,
            "cgpa":student.cgpa
        }
        student_data.append(student_dict)
    return jsonify(student_data),200

@app.route("/students/<student_id>",methods=["GET"])
def get_student(student_id):
    students=database.get_student()
    for student in students:
        if student.student_id==student_id:
            student_dict={
                "student_id":student.student_id,
                "name":student.name,
                "age":student.age,
                "gender":student.gender,
                "department":student.department,
                "email":student.email,
                "cgpa":float(student.cgpa)
            }

            return jsonify(student_dict),200
    return jsonify({
        "error":"Student not found"
    }),404

@app.route("/students",methods=["POST"])
def add_student():
    data=request.get_json(silent=True)
    if data is None:
        return jsonify({
            "error":"JSON data is required"
        }),400
    required_fields=[
        "student_id",
        "name",
        "age",
        "gender",
        "department",
        "email",
        "cgpa"
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error":f"{field } is required."
            }),400
    student=Student(
        data["student_id"],
        data["name"],
        data["age"],
        data["gender"],
        data["department"],
        data["email"],
        data["cgpa"]
    )
    print(student)
    result=database.save_student(student)
    if result:
        return jsonify({
            "message":"Student successfully added"
        }),201
    return jsonify({
        "message":"Student could not be added"
    }),400

@app.route("/students/<student_id>",methods=["PUT"])
def update_student(student_id):
    data=request.get_json(silent=True)
    if data is None:
        return jsonify({
            "error":"Json data is required"
        }),400
    students=database.get_student()
    for student in students:
        if student.student_id==student_id:
            student.name=data["name"]
            student.age=data["age"]
            student.gender=data["gender"]
            student.department=data["department"]
            student.email=data["email"]
            student.cgpa=data["cgpa"]
            database.update_student(student,student_id)
            return jsonify({
                "message":"Student update successfully"
            }),200

    return jsonify({
        "error":"Student not found"
    }),404


@app.route("/students/<student_id>",methods=["DELETE"])
def delete_student(student_id):
    students=database.get_student()
    for student in students:
        if student.student_id==student_id:
            database.delete_student(student_id)
            return "",204
    return jsonify({
        "error":"Student not found"
    }),404

@app.route("/students/<student_id>",methods=["PATCH"])
def patch_student(student_id):
    data=request.get_json(silent=True)
    if data is None:
        return jsonify({
            "error":"Json data is required"
        }),400
    
    students=database.get_student()
    for student in students:
        if student.student_id==student_id:
            for key,value in data.items():
                if hasattr(student,key):
                    setattr(student,key,value)

            database.update_student(student,student_id)
            return jsonify({
                "message":"Student successfully updated"
            }),200
    return jsonify({
        "error":"Student not found"
    }),404



if __name__=="__main__":
    app.run()