from wtforms import Form, StringField, PasswordField, SelectField, BooleanField, IntegerField, DecimalField, validators

# Form Classes
class LoginForm(Form):
    national_id = StringField('National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long."),validators.Regexp('[0-9]{11}')])
    password = PasswordField('Password', [validators.DataRequired()])
    user_type = SelectField('Login As', choices=["Patient", "Doctor", "Manager"], validators=[validators.DataRequired()])
    remember = BooleanField('Remember Me')

class RegisterPatientForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    surname = StringField('Surname', [validators.Length(min=1, max=50)])
    national_id = StringField('National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long."),validators.Regexp('[0-9]{11}')])
    age = IntegerField('Age', validators=[validators.NumberRange(min = 12, message='You must be older than 12 years old to use this site.'), validators.DataRequired()])
    gender = SelectField('Gender', choices=['Male', 'Female'], validators=[validators.DataRequired()])
    race = SelectField('Race', choices=['White', 'Black', 'Asian', 'Hawaiian', 'Native', 'Other'], validators=[validators.DataRequired()])
    height = DecimalField('Height (cm)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    weight = DecimalField('Weight (kg)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match.')
    ])
    confirm = PasswordField('Confirm Password')

class RegisterDoctorForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    surname = StringField('Surname', [validators.Length(min=1, max=50)])
    national_id = StringField('National ID', [
        validators.Length(min=11, max=11, message="National ID is 11 digits long."),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='National IDs do not match.'),
        validators.Regexp('[0-9]{11}')
        ])
    confirm = StringField('Confirm National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long.")])
    hospital_id = IntegerField('Hospital ID')
    expertise = StringField('Expertise', [validators.Length(min=1, max=50)])

class DeactivateDoctorForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    surname = StringField('Surname', [validators.Length(min=1, max=50)])
    national_id = StringField('National ID', [
        validators.Length(min=11, max=11, message="National ID is 11 digits long."),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='National IDs do not match.'),
        validators.Regexp('[0-9]{11}')
        ])
    confirm = StringField('Confirm National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long.")])
    hospital_id = IntegerField('Hospital ID')

class ActivateDoctorForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    surname = StringField('Surname', [validators.Length(min=1, max=50)])
    national_id = StringField('National ID', [
        validators.Length(min=11, max=11, message="National ID is 11 digits long."),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='National IDs do not match.'),
        validators.Regexp('[0-9]{11}')
        ])
    confirm = StringField('Confirm National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long.")])
    hospital_id = IntegerField('Hospital ID')

class SubmitNationalIDForm(Form):
    national_id = StringField('National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long."),validators.Regexp('[0-9]{11}')])

class UploadPatientDataForm(Form):
    smoking = SelectField('Smoking', choices=['Never smoker', 'Former smoker', 'Current every day smoker'], validators=[validators.DataRequired()])
    respiratory_rate = IntegerField('Respiratory Rate (/min)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    pain_severity = IntegerField('Pain Severity (1-10)', validators=[validators.NumberRange(min=1, max=10), validators.DataRequired()])
    heart_rate = IntegerField('Heart Rate (/min)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    ldl = DecimalField('LDL cholesterol (mg/dL)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    hdl = DecimalField('HDL cholesterol (mg/dL)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    triglycerides = DecimalField('Triglyceride Level (mg/dL)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    hemoglobin = DecimalField('Hemoglobin [Mass/volume] in Blood (g/dL)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    sodium = DecimalField('Sodium (mmol/L)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    systolic_bp = DecimalField('Systolic Blood Pressure (mm[Hg])', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    diastolic_bp = DecimalField('Diastolic Blood Pressure (mm[Hg])', validators=[validators.NumberRange(min = 0), validators.DataRequired()])
    stress = SelectField('Stress', choices=['I choose not to answer this question', 'A little bit', 'Not at all', 'Somewhat', 'Quite a bit', 'Very much'], 
        validators=[validators.DataRequired()])

class UploadDiagnosisForm(Form):
    diagnosis = StringField('Diagnosis', validators=[validators.Length(min=1, max=50), validators.DataRequired()])

class UpdateWeightForm(Form):
    weight = DecimalField('Weight (kg)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])

class UpdateHeightForm(Form):
    height = DecimalField('Height (cm)', validators=[validators.NumberRange(min = 0), validators.DataRequired()])

class UpdatePasswordForm(Form):
    old_password = PasswordField('Old Password', [validators.DataRequired()])
    password = PasswordField('Password',validators=[validators.DataRequired()])
    confirm = PasswordField('Confirm Password',validators=[validators.DataRequired()])

class DeleteDataForm(Form):
    national_id = StringField('National ID', [validators.Length(min=11, max=11, message="National ID is 11 digits long.")])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match.')
    ])
    confirm = PasswordField('Confirm Password')