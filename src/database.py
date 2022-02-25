from sqlalchemy.orm import session
from classes import *
from extensions import login_manager
from exceptions import *
from ast import literal_eval


#User loader
@login_manager.user_loader
def load_user(user_info):
    user = None
    if type(user_info) == str:
        user_info = literal_eval(user_info)
    if(user_info['type'] == "patient"):
        user = Patient.query.filter_by(id=user_info['id']).first()
    elif(user_info['type'] == "doctor"):
        user = Doctor.query.filter_by(id=user_info['id']).first()
    elif(user_info['type'] == "manager"):
        user = Manager.query.filter_by(id=user_info['id']).first()
    else:
        raise InternalServerError("Invalid user type in database.load_user")
        
    if(user):
        return user
    else:
        None

#Database functions

def get_first_doctor_by_name(name):
    return Doctor.query.filter_by(name=name).first()

def get_first_doctor_by_national_id(national_id):
    return Doctor.query.filter_by(national_id=national_id).first()

def get_first_patient_by_national_id(national_id):
    return Patient.query.filter_by(national_id=national_id).first()

def get_first_manager_by_national_id(national_id):
    return Manager.query.filter_by(national_id=national_id).first()

def get_patient_by_id(id):
    return Patient.query.filter_by(id=id).first()

def get_doctor_by_id(id):
    return Doctor.query.filter_by(id=id).first()

def get_manager_by_id(id):
    return Manager.query.filter_by(id=id).first()

def get_patient_data_by_id(id):
    return PatientData.query.filter_by(id=id).first()

def get_diagnosis_by_id(id):
    return Diagnosis.query.filter_by(id=id).first()

def get_prediction_by_patient_data_id(patient_data_id):
    return Prediction.query.filter_by(patient_data_id=patient_data_id).first()

def add_patient(patient):
    try:
        db.session.add(patient)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def add_doctor(doctor):
    try:
        db.session.add(doctor)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def add_manager(manager):
    try:
        db.session.add(manager)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def deactivate_doctor_by_national_id(national_id):
    try:
        doctor = Doctor.query.filter_by(national_id=national_id).first()
        if not doctor.is_active:
            return False
        doctor.is_active = False
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def activate_doctor_by_national_id(national_id):
    try:
        doctor = Doctor.query.filter_by(national_id=national_id).first()
        if doctor.is_active:
            return False
        doctor.is_active = True
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
    
def get_all_patient_data_by_patient_id(patient_id):
    return PatientData.query.filter_by(patient_id=patient_id).all()

def get_last_patient_data_by_patient_id(patient_id):
    return PatientData.query.filter_by(patient_id=patient_id).order_by(PatientData.datum.desc()).limit(1).first()

def get_all_diagnosis_by_patient_id(patient_id):
    return Diagnosis.query.filter_by(patient_id=patient_id).all()

def get_last_diagnosis_by_patient_id(patient_id):
    return Diagnosis.query.filter_by(patient_id=patient_id).order_by(Diagnosis.datum.desc()).limit(1).first()

def add_patient_data(patient_data):
    try:
        db.session.add(patient_data)
        db.session.commit()
        return True, patient_data.id
    except:
        db.session.rollback()
        return False, None


def add_diagnosis(diagnosis):
    try:
        db.session.add(diagnosis)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def add_prediction(prediction):
    try:
        db.session.add(prediction)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def update_patient_password_by_id(id, password):
    try:
        patient = Patient.query.filter_by(id=id).first()
        patient.password = password
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def update_patient_weight_by_id(id, weight):
    try:
        patient = Patient.query.filter_by(id=id).first()
        patient.weight = weight
        patient.bmi = weight * 10000 / (patient.height * patient.height)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def update_patient_height_by_id(id, height):
    try:
        patient = Patient.query.filter_by(id=id).first()
        patient.height = height
        patient.bmi = patient.weight * 10000 / (height * height)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def update_doctor_password_by_id(id, password):
    try:
        doctor = Doctor.query.filter_by(id=id).first()
        doctor.password = password
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def update_manager_password_by_id(id, password):
    try:
        manager = Manager.query.filter_by(id=id).first()
        manager.password = password
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def delete_all_patient_data_by_patient_id(patient_id):
    try:
        PatientData.query.filter_by(patient_id=patient_id).delete()
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False