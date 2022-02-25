from extensions import db
from datetime import datetime

#Class definitions

class User():
    """User class"""

    def __init__(self, national_id, name, surname, password):
        self.national_id = national_id
        self.name        = name
        self.surname     = surname
        self.password    = password

    def __repr__(self):
        return f"National ID: {self.national_id}\nName: {self.name}\nSurname: {self.surname}\n"

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

class Patient(User, db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.String(11), unique=True, nullable=False)
    name        = db.Column(db.String(50), nullable=False)
    surname     = db.Column(db.String(50), nullable=False)
    password    = db.Column(db.String(), nullable=False)
    age         = db.Column(db.Integer, nullable=False)
    gender      = db.Column(db.String(10), nullable=False)
    race        = db.Column(db.String(20), nullable=False)
    height      = db.Column(db.Float, nullable=False)
    weight      = db.Column(db.Float, nullable=False)
    bmi         = db.Column(db.Float, nullable=False)
    
    diagnoses   = db.relationship('Diagnosis', backref='patient', lazy=True)
    type        = "patient"

    def __init__(self, national_id, name, surname, password, age, gender, race, height, weight):
        super().__init__(national_id, name, surname, password)
        self.age = age
        self.gender = gender
        self.race = race
        self.height = height
        self.weight = weight
        self.bmi = weight * 10000 / (height * height)
    
    def get_id(self):
        return {"id" : self.id, "type" : self.type}

class Doctor(User, db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.String(11), unique=True, nullable=False)
    name        = db.Column(db.String(50), nullable=False)
    surname     = db.Column(db.String(50), nullable=False)
    password    = db.Column(db.String(), nullable=False)
    hospital_id = db.Column(db.Integer, nullable=False)
    expertise   = db.Column(db.String(50), nullable=False)
    is_active   = db.Column(db.Boolean, nullable=False)
    diagnoses   = db.relationship('Diagnosis', backref='doctor', lazy=True)
    type        = "doctor"

    def __init__(self, national_id, name, surname, password, hospital_id, expertise, is_active):
        super().__init__(national_id, name, surname, password)
        self.hospital_id = hospital_id
        self.expertise   = expertise
        self.is_active   = is_active

    def get_id(self):
        return {"id" : self.id, "type" : self.type}

class Manager(User, db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.String(11), unique=True, nullable=False)
    name        = db.Column(db.String(50), nullable=False)
    surname     = db.Column(db.String(50), nullable=False)
    password    = db.Column(db.String(), nullable=False)
    type        = "manager"

    def __init__(self, national_id, name, surname, password):
        super().__init__(national_id, name, surname, password)

    def get_id(self):
        return {"id" : self.id, "type" : self.type}
        
class PatientData(db.Model):

    id                = db.Column(db.Integer, primary_key=True)
    patient_id        = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    smoking           = db.Column(db.String(50), nullable=False)
    respiratory_rate  = db.Column(db.Integer, nullable=False)
    pain_severity     = db.Column(db.Integer, nullable=False)
    heart_rate        = db.Column(db.Integer, nullable=False)
    ldl               = db.Column(db.Float, nullable=False)
    hdl               = db.Column(db.Float, nullable=False)
    triglycerides     = db.Column(db.Float, nullable=False)
    total_cholesterol = db.Column(db.Float, nullable=False)
    hemoglobin        = db.Column(db.Float, nullable=False)
    sodium            = db.Column(db.Float, nullable=False)
    systolic_bp       = db.Column(db.Float, nullable=False)
    diastolic_bp      = db.Column(db.Float, nullable=False)
    stress            = db.Column(db.String(50), nullable=False)
    datum             = db.Column(db.DateTime, nullable=False)
    predictions       = db.relationship("Prediction", passive_deletes=True, backref="PatientData")

    def __init__(self, patient_data):
        self.patient_id        = patient_data['patient_id']
        self.smoking           = patient_data['smoking']
        self.respiratory_rate  = patient_data['respiratory_rate']
        self.pain_severity     = patient_data['pain_severity']
        self.heart_rate        = patient_data['heart_rate']
        self.ldl               = patient_data['ldl']
        self.hdl               = patient_data['hdl']
        self.triglycerides     = patient_data['triglycerides']
        self.total_cholesterol = patient_data['total_cholesterol']
        self.hemoglobin        = patient_data['hemoglobin']
        self.sodium            = patient_data['sodium']
        self.systolic_bp       = patient_data['systolic_bp']
        self.diastolic_bp      = patient_data['diastolic_bp']
        self.stress            = patient_data['stress']
        self.datum             = datetime.now()

class Diagnosis(db.Model):
    
    id         = db.Column(db.Integer, primary_key=True)
    doctor_id  = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    diagnosis  = db.Column(db.String(50), nullable=False)
    datum      = db.Column(db.DateTime, nullable=False)

    def __init__(self, diagnosis, doctor_id, patient_id):
        self.diagnosis  = diagnosis
        self.doctor_id  = doctor_id
        self.patient_id = patient_id
        self.datum      = datetime.now()


class Prediction(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    patient_data_id = db.Column(db.Integer, db.ForeignKey("patient_data.id", ondelete='CASCADE'), nullable=False)
    prediction      = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, patient_data_id, prediction):
        self.patient_data_id = patient_data_id
        self.prediction = prediction