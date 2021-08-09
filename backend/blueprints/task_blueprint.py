from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('hotel_blueprint', __name__)

model = TaskModel()

@task_blueprint.route('/hotel/add_form', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_form(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_form', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_form', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_forms', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_forms())


#######################################


@task_blueprint.route('/hotel/add_guest_h1', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest1(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h1', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h1', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h1', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests1())


#######################################


@task_blueprint.route('/hotel/add_guest_h2', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest2(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h2', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest2(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h2', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest2(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h2', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests2())


#######################################


@task_blueprint.route('/hotel/add_guest_h3', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest3(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h3', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest3(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h3', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest3(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h3', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests3())


#######################################


@task_blueprint.route('/hotel/add_guest_h4', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest4(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h4', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest4(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h4', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest4(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h4', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests4())


#######################################


@task_blueprint.route('/hotel/add_guest_h5', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest5(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h5', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest5(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h5', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest5(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h5', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests5())


#######################################


@task_blueprint.route('/hotel/add_guest_h6', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_guest6(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h6', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_guest6(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h6', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_guest6(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h6', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_guests6())