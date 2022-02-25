from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt
from database import *
from exceptions import *
from extensions import model
from forms import *
from secrets import token_urlsafe

#View functions

#Common pages
def v_landing_page():
    return render_template("index.html")

def v_login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        national_id = form.national_id.data
        password = form.password.data
        remember = form.remember.data
        user_type = form.user_type.data
        if user_type == "Patient":
            patient = get_first_patient_by_national_id(national_id)
            if patient:
                if sha256_crypt.verify(password, patient.password):
                    login_user(patient, remember=remember)
                    flash("Logged in!", 'success')
                    return redirect(url_for("v_dashboard"))
                else:
                    flash("Wrong password.", 'danger')
                    return redirect(url_for("v_login"))
            else:
                flash("A patient by this national id doesn't exist. Please register first.", 'danger')
                return redirect(url_for("v_login"))

        elif user_type == "Doctor":
            doctor = get_first_doctor_by_national_id(national_id)
            if doctor:
                if sha256_crypt.verify(password, doctor.password) and doctor.is_active:
                    login_user(doctor, remember=remember)
                    return redirect(url_for("v_dashboard"))
                else:
                    if doctor.is_active:
                        flash("Wrong password.", 'danger')
                    else:
                        flash("Your account is deactivated. Please contact your manager.", 'danger')
                    return redirect(url_for("v_login"))
            else:
                flash("A doctor by this national id doesn't exist. Please contact your manager.", 'danger')
                return redirect(url_for("v_login"))

        elif user_type == "Manager":
            manager = get_first_manager_by_national_id(national_id)
            if manager:
                if sha256_crypt.verify(password, manager.password):
                    login_user(manager, remember=remember)
                    return redirect(url_for("v_dashboard"))
                else:
                    flash("Wrong password.", 'danger')
                    return redirect(url_for("v_login"))
            else:
                flash("A manager by this national id doesn't exist.", 'danger')
                return redirect(url_for("v_login"))
        else:
            raise InternalServerError("Invalid user type in views.login")

    else:
        return render_template("login.html", form=form)
    
def v_register():
    form = RegisterPatientForm(request.form)
    if request.method == "POST" and form.validate():
        national_id = form.national_id.data
        name = form.name.data
        surname = form.surname.data
        password = sha256_crypt.hash(form.password.data)
        age = int(form.age.data)
        gender = form.gender.data
        race = form.race.data
        height = float(form.height.data)
        weight = float(form.weight.data)
        if not national_id.isnumeric():
            flash("National ID field must be a number.", 'danger')
            return redirect(url_for("v_register"))

        if get_first_patient_by_national_id(national_id):
            flash("A patient by this national id already exists. Please login", 'danger')
            return redirect(url_for("v_register"))
        else:
            patient = Patient(national_id, name, surname, password, age, gender, race, height, weight)
            success = add_patient(patient)
            if success:
                flash("Patient registered. You can now log in.", 'success')
                return redirect(url_for("v_register"))
            else:
                flash("Patient could not be registered. Please try again.", 'danger')
                return redirect(url_for("v_register"))
        
    else:
        return render_template("register.html", form=form)

#TODO: Implement dynamic dashboard for all user types
@login_required
def v_dashboard():
    if current_user.type == "patient":
        patient_id = current_user.get_id()['id']
        patient = get_patient_by_id(patient_id)
        return render_template("dashboard.html", patient=patient)
    return render_template("dashboard.html")

#TODO: User authorization for user type specific pages, custom 403 page?
@login_required
def v_settings():
    pwform = UpdatePasswordForm(request.form)
    hform = UpdateHeightForm(request.form)
    wform = UpdateWeightForm(request.form)
    if request.method == "POST" and pwform.validate():
        old_password = pwform.old_password.data
        password = pwform.password.data
        confirm = pwform.confirm.data
        if current_user.type == "patient":
            patient_id = current_user.get_id()['id']
            patient = get_patient_by_id(patient_id)
            if patient and sha256_crypt.verify(old_password, patient.password) and password == confirm:
                success = update_patient_password_by_id(patient_id, sha256_crypt.hash(password))
                if success:
                    flash("Password Changed", 'success')
                    return redirect(url_for("v_dashboard"))
                else:
                    flash("Password could not be updated", 'danger')
                    return redirect(url_for("v_settings"))
            elif not sha256_crypt.verify(old_password, patient.password):
                flash("Old password is wrong!", 'danger')
                return redirect(url_for("v_settings"))
            else:
                flash("Passwords do not match!", 'danger')
                return redirect(url_for("v_settings"))
        elif current_user.type == "doctor":
            doctor_id = current_user.get_id()['id']
            doctor = get_doctor_by_id(doctor_id)
            if doctor and sha256_crypt.verify(old_password, doctor.password) and password == confirm:
                success = update_doctor_password_by_id(doctor_id, sha256_crypt.hash(password))
                if success:
                    flash("Password Changed", 'success')
                    return redirect(url_for("v_dashboard"))
                else:
                    flash("Password could not be updated", 'danger')
                    return redirect(url_for("v_settings"))
            elif not sha256_crypt.verify(old_password, doctor.password):
                flash("Old password is wrong!", 'danger')
                return redirect(url_for("v_settings"))
            else:
                flash("Passwords do not match!", 'danger')
                return redirect(url_for("v_settings"))
        elif current_user.type == "manager":
            manager_id = current_user.get_id()['id']
            manager = get_manager_by_id(manager_id)
            if manager and sha256_crypt.verify(old_password, manager.password) and password == confirm:
                success = update_manager_password_by_id(manager_id, sha256_crypt.hash(password))
                if success:
                    flash("Password Changed", 'success')
                    return redirect(url_for("v_dashboard"))
                else:
                    flash("Password could not be updated", 'danger')
                    return redirect(url_for("v_settings"))
            elif not sha256_crypt.verify(old_password, manager.password):
                flash("Old password is wrong!", 'danger')
                return redirect(url_for("v_settings"))
            else:
                flash("Passwords do not match!", 'danger')
                return redirect(url_for("v_settings"))
    elif request.method == "POST" and hform.validate():
        height = float(hform.height.data)
        patient_id = current_user.get_id()['id']
        success = update_patient_height_by_id(patient_id, height)
        if success:
            flash("Height Updated", 'success')
            return redirect(url_for("v_settings"))
        else:
            flash("Height could not be updated", 'danger')
            return redirect(url_for("v_settings"))
    
    elif request.method == "POST" and wform.validate():
        weight = float(wform.weight.data)
        patient_id = current_user.get_id()['id']
        success = update_patient_weight_by_id(patient_id, weight)
        if success:
            flash("Weight Updated", 'success')
            return redirect(url_for("v_settings"))
        else:
            flash("Weight could not be updated", 'danger')
            return redirect(url_for("v_settings"))
    else:
        return render_template("settings.html", pwform=pwform, hform=hform, wform=wform)

@login_required
def v_sign_out():
    logout_user()
    flash("You have signed out.", 'success')
    return redirect(url_for("v_landing_page"))

#Patient specific pages
@login_required
def v_view_data():
    patient_id = current_user.get_id()['id']
    data = get_all_patient_data_by_patient_id(patient_id)
    patient = get_patient_by_id(patient_id)
    return render_template("view_data.html", patient=patient, patient_data=data)

@login_required
def v_view_last_data():
    patient_id = current_user.get_id()['id']
    patient = get_patient_by_id(patient_id)
    patient_data = get_last_patient_data_by_patient_id(patient_id)
    
    if patient_data:
        prediction = get_prediction_by_patient_data_id(patient_data.id)
        return render_template("view_data_success.html", patient=patient, patient_data=patient_data, prediction=prediction)
    else:
        flash("Record not found!", 'danger')
        return redirect(url_for("v_dashboard"))

@login_required
def v_view_last_diagnosis():
    patient_id = current_user.get_id()['id']
    patient = get_patient_by_id(patient_id)
    diagnosis = get_last_diagnosis_by_patient_id(patient_id)
    if diagnosis:
        return render_template("view_diagnosis_success.html", patient=patient, diagnosis=diagnosis)
    else:
        flash("Diagnosis not found!", 'danger')
        return redirect(url_for("v_dashboard"))

@login_required
def v_view_data_success():
    patient_id = current_user.get_id()['id']
    patient_data_id = request.args['data_id']
    patient = get_patient_by_id(patient_id)
    patient_data = get_patient_data_by_id(patient_data_id)
    if patient_data:
        prediction = get_prediction_by_patient_data_id(patient_data_id)
        return render_template("view_data_success.html", patient=patient, patient_data=patient_data, prediction=prediction)
    else:
        flash("Record not found!", 'danger')
        return redirect(url_for("v_dashboard"))

@login_required
def v_view_diagnosis():
    patient_id = current_user.get_id()['id']
    diagnosis = get_all_diagnosis_by_patient_id(patient_id)
    patient = get_patient_by_id(patient_id)
    return render_template("view_diagnosis.html",  patient=patient, diagnosis=diagnosis)

@login_required
def v_view_diagnosis_success():
    patient_id = current_user.get_id()['id']
    diagnosis_id = request.args['diagnosis_id']
    patient = get_patient_by_id(patient_id)
    diagnosis = get_diagnosis_by_id(diagnosis_id)
    if diagnosis:
        return render_template("view_diagnosis_success.html", patient=patient, diagnosis=diagnosis)
    else:
        flash("Record not found!", 'danger')
        return redirect(url_for("v_dashboard"))

@login_required
def v_delete_data():
    form = DeleteDataForm(request.form)
    if request.method == "POST" and form.validate():
        national_id = form.national_id.data
        password = form.password.data
        patient_id = current_user.get_id()['id']
        patient = get_patient_by_id(patient_id)
        if patient.national_id == national_id and sha256_crypt.verify(password, patient.password):
            success = delete_all_patient_data_by_patient_id(patient_id)
            if success:
                flash("You have deleted your data from the database.", 'success')
                return redirect(url_for("v_dashboard"))
            else:
                flash("Data could not be deleted. Please try again.", 'danger')
                return redirect(url_for("v_delete_data"))
    else:
        return render_template("delete_data.html", form=form)

#Doctor specific pages
@login_required
def v_upload_data():
    form = SubmitNationalIDForm(request.form)
    if request.method == "POST" and form.validate():
        patient = get_first_patient_by_national_id(form.national_id.data)
        if patient:
            return redirect(url_for("v_upload_data_success", patient_id=patient.id,**request.args))
        else:
            flash("There is no patient with the submitted national ID.", 'danger')
            return render_template("upload_data.html", form=form)
    else:
        return render_template("upload_data.html", form=form)

@login_required
def v_upload_data_success():
    form = UploadPatientDataForm(request.form)
    patient_id = request.args['patient_id']
    if request.method == "POST" and form.validate():
        smoking           = form.smoking.data
        respiratory_rate  = int(form.respiratory_rate.data)
        pain_severity     = int(form.pain_severity.data)
        heart_rate        = int(form.heart_rate.data)
        ldl               = float(form.ldl.data)
        hdl               = float(form.hdl.data)
        triglycerides     = float(form.triglycerides.data)
        total_cholesterol = ldl + hdl + triglycerides / 5
        hemoglobin        = float(form.hemoglobin.data)
        sodium            = float(form.sodium.data)
        systolic_bp       = float(form.systolic_bp.data)
        diastolic_bp      = float(form.diastolic_bp.data)
        stress            = form.stress.data
        patient_data_dict = {
                        "patient_id"         : patient_id, 
                        "smoking"            : smoking,
                        "respiratory_rate"   : respiratory_rate,
                        "pain_severity"      : pain_severity,
                        "heart_rate"         : heart_rate,
                        "ldl"                : ldl,
                        "hdl"                : hdl,
                        "triglycerides"      : triglycerides,
                        "total_cholesterol"  : total_cholesterol,
                        "hemoglobin"         : hemoglobin,
                        "sodium"             : sodium,
                        "systolic_bp"        : systolic_bp,
                        "diastolic_bp"       : diastolic_bp,
                        "stress"             : stress
        }
        patient = get_patient_by_id(patient_id)
        patient_data = PatientData(patient_data_dict)
        success, patient_data_id = add_patient_data(patient_data)
        if success:
            flash("Patient Data added.", 'success')
            model_output = model.predict(patient, patient_data)
            prediction =  Prediction(patient_data_id, model_output)
            #TODO: think of a way to use the result of this operation
            success = add_prediction(prediction)
            return render_template("view_patient_data_success.html", patient=patient, patient_data=patient_data, prediction=prediction)
        else:
            flash("Data could not be added. Please try again.", 'danger')
            return redirect(url_for("v_upload_data"))
    else:
        return render_template("upload_data_success.html", form=form, patient_id=patient_id)

@login_required
def v_upload_diagnosis():
    form = SubmitNationalIDForm(request.form)
    if request.method == "POST" and form.validate():
        patient = get_first_patient_by_national_id(form.national_id.data)
        if patient:
            return redirect(url_for("v_upload_diagnosis_success", patient_id=patient.id))
        else:
            flash("There is no patient with the submitted national ID.", 'danger')
            return render_template("upload_diagnosis.html", form=form)
    else:
        return render_template("upload_diagnosis.html", form=form)

@login_required
def v_upload_diagnosis_success():
    form = UploadDiagnosisForm(request.form)
    patient_id = request.args['patient_id']
    if request.method == "POST" and form.validate():
        diagnosis = Diagnosis(form.diagnosis.data, current_user.get_id()['id'], patient_id)
        success = add_diagnosis(diagnosis)
        if success:
            flash("Diagnosis added", 'success')
            return render_template("dashboard.html")
        else:
            flash("Diagnosis could not be added. Try again.", 'danger')
            return redirect(url_for("v_upload_diagnosis"))
    else:
        return render_template("upload_diagnosis_success.html", form=form)
 
@login_required
def v_view_patient_data():
    form = SubmitNationalIDForm(request.form)
    if request.method == "POST" and form.validate():
        patient = get_first_patient_by_national_id(form.national_id.data)
        if patient:
            patient_data = get_all_patient_data_by_patient_id(patient.id)
            return render_template("view_patient_data.html", method="post", patient=patient, patient_data=patient_data, form=form)
        else:
            flash("There is no patient with the submitted national ID.", 'danger')
            return render_template("view_patient_data.html", method="get", patient=None, patient_data=None, form=form)
    else:
        return render_template("view_patient_data.html", form=form, method="get", patient=None, patient_data=None)

@login_required
def v_view_patient_data_success():
    patient_id = request.args['patient_id']
    patient_data_id = request.args['data_id']
    patient = get_patient_by_id(patient_id)
    patient_data = get_patient_data_by_id(patient_data_id)
    
    if patient_data:
        prediction = get_prediction_by_patient_data_id(patient_data_id)
        return render_template("view_patient_data_success.html", patient=patient, patient_data=patient_data, prediction=prediction)
    else:
        flash("Record not found!", 'danger')
        return redirect(url_for("v_dashboard"))

@login_required
def v_view_patient_diagnosis():
    form = SubmitNationalIDForm(request.form)
    if request.method == "POST" and form.validate():
        patient = get_first_patient_by_national_id(form.national_id.data)
        if patient:
            diagnosis = get_all_diagnosis_by_patient_id(patient.id)
            return render_template("view_patient_diagnosis.html", method="post", patient=patient, diagnosis=diagnosis, form=form)
        else:
            flash("There is no patient with the submitted national ID.", 'danger')
            return render_template("view_patient_diagnosis.html", method="get", patient=None, diagnosis=None, form=form)
    else:
        return render_template("view_patient_diagnosis.html", form=form, method="get", patient=None, diagnosis=None)

@login_required
def v_view_patient_diagnosis_success():
    patient_id = request.args['patient_id']
    diagnosis_id = request.args['diagnosis_id']
    patient = get_patient_by_id(patient_id)
    diagnosis = get_diagnosis_by_id(diagnosis_id)
    if diagnosis:
        return render_template("view_patient_diagnosis_success.html", patient=patient, diagnosis=diagnosis)
    else:
        flash("Record not found!", 'danger')
        return redirect(url_for("v_dashboard"))

#Manager specific pages
@login_required
def v_add_doctor():
    form = RegisterDoctorForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        national_id = form.national_id.data
        hospital_id = form.hospital_id.data
        expertise = form.expertise.data
        password = token_urlsafe(10)
        is_active = True
        if not national_id.isnumeric():
            flash("National ID field must be a number.", 'danger')
            return redirect(url_for("v_add_doctor"))

        doctor = Doctor(national_id, name,  surname, sha256_crypt.hash(password), hospital_id, expertise, is_active)
        success = add_doctor(doctor)
        if success:
            flash("Doctor registered.", 'success')
            return render_template("add_doctor_successful.html", password=password)
        else:
            flash("Doctor could not be registered. Please try again.", 'danger')
            return redirect(url_for("v_add_doctor"))
    else:
        return render_template("add_doctor.html", form=form)


@login_required
def v_deactivate_doctor():
    form = DeactivateDoctorForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        national_id = form.national_id.data
        hospital_id = form.hospital_id.data
        db_doctor = get_first_doctor_by_national_id(national_id)
        if db_doctor and name == db_doctor.name and surname == db_doctor.surname and hospital_id == db_doctor.hospital_id:
            success = deactivate_doctor_by_national_id(national_id)
            if success:
                flash("Doctor successfully deactivated.", 'success')
                return redirect(url_for("v_deactivate_doctor"))
            else:
                flash("Doctor could not be deactivated. This can be caused by a server error or the doctor might be already deactivated. Please try again.", 'danger')
                return redirect(url_for("v_deactivate_doctor"))
        else:
            flash("Doctor could not be deactivated. Please make sure that the submitted information is correct.", 'danger')
            return redirect(url_for("v_deactivate_doctor"))
    else:
        return render_template("deactivate_doctor.html", form=form)

@login_required
def v_activate_doctor():
    form = ActivateDoctorForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        national_id = form.national_id.data
        hospital_id = form.hospital_id.data
        db_doctor = get_first_doctor_by_national_id(national_id)
        if db_doctor and name == db_doctor.name and surname == db_doctor.surname and hospital_id == db_doctor.hospital_id:
            success = activate_doctor_by_national_id(national_id)
            if success:
                flash("Doctor successfully activated.", 'success')
                return redirect(url_for("v_activate_doctor"))
            else:
                flash("Doctor could not be activated. This can be caused by a server error or the doctor might be already active. Please try again.", 'danger')
                return redirect(url_for("v_activate_doctor"))
        else:
            flash("Doctor could not be activated. Please make sure that the submitted information is correct.", 'danger')
            return redirect(url_for("v_activate_doctor"))
    else:
        return render_template("activate_doctor.html", form=form)