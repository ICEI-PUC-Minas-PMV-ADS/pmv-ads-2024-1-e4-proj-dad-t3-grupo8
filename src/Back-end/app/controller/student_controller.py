from flask import jsonify
from bson import ObjectId

from app.model import Student, Class
from app.controller import student_collection, classes_collection
from app.services import verify_request_data, get_items_data, verify_user_email, update_time_data, verify_update_sent_data_request, get_data_by_id

def get_available_students():

    student_list = get_items_data(student_collection.find({}))

    return jsonify(student_list), 200


def insert_new_student(data: dict):

    is_wrong_data = Student.verify_student_data(data)

    if is_wrong_data: 
        return is_wrong_data, 400
    
    classes_data = classes_collection.find({})
    is_existent_class = Class.verify_if_exist_class_data(data.get('class_number'), classes_data)

    if not is_existent_class: 
        return "Turma inexistente", 400  
    
    new_student = Student(**data)
    is_same_email = verify_user_email(data["email"], student_collection.find({}))

    if is_same_email: 
        return is_same_email, 409
    
    student_collection.insert_one(new_student.__dict__)
    
    return 'Novo aluno cadastrado com sucesso!', 201


def update_student_profile(data):
    
    wrong_data_request = verify_request_data(data, student_collection, 'PATCH')
    if wrong_data_request: 
        return wrong_data_request, 400

    user_id = data.get('id')
    available_student_keys = ['name', 'email', 'class_number', 'id', 'password']

    wrong_properties = verify_update_sent_data_request(data, available_student_keys)
    if wrong_properties:
        return wrong_properties, 400

    for key in data.keys():

        if key != 'id':
            new_values = {"$set": {key: data[key]} }
            student_collection.update_one({'_id' : ObjectId(user_id)}, new_values)
    
    student_collection.update_one({'_id' : ObjectId(user_id)}, update_time_data())

    return 'Perfil de Estudante atualizado com sucesso!', 200


def delete_student_profile(data):

    wrong_data_request = verify_request_data(data, student_collection)
    if wrong_data_request: 
        return wrong_data_request, 400
    
    user_id = data.get('id')
    student_collection.delete_one({"_id": ObjectId(user_id) })

    return 'Perfil de Estudante deletado com sucesso!', 200


def get_student_profile(user_id):

    wrong_request_data = verify_request_data({'id': user_id}, student_collection, 'GET')
    if wrong_request_data:
        return wrong_request_data, 400
    
    teacher_profile = get_data_by_id(user_id, student_collection)

    return jsonify(teacher_profile), 200
