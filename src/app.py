from extensions import app
from views import *

#URL rules

#Common pages
app.add_url_rule("/", view_func=v_landing_page)
app.add_url_rule("/login", view_func=v_login, methods=['GET', 'POST'])
app.add_url_rule("/register", view_func=v_register, methods=['GET', 'POST'])
app.add_url_rule("/dashboard", view_func=v_dashboard)
app.add_url_rule("/settings", view_func=v_settings, methods=['GET', 'POST'])
app.add_url_rule("/sign_out", view_func=v_sign_out)
#Patient specific pages
app.add_url_rule("/view_data", view_func=v_view_data)
app.add_url_rule("/view_data_success", view_func=v_view_data_success)
app.add_url_rule("/view_diagnosis", view_func=v_view_diagnosis)
app.add_url_rule("/view_diagnosis_success", view_func=v_view_diagnosis_success)
app.add_url_rule("/delete_data", view_func=v_delete_data, methods=['GET', 'POST'])
app.add_url_rule("/view_last_data", view_func=v_view_last_data)
app.add_url_rule("/view_last_diagnosis", view_func=v_view_last_diagnosis)

#Doctor specific pages
app.add_url_rule("/upload_data", view_func=v_upload_data, methods=['GET', 'POST'])
app.add_url_rule("/view_patient_data", view_func=v_view_patient_data, methods=['GET', 'POST'])
app.add_url_rule("/view_patient_data_success", view_func=v_view_patient_data_success)
app.add_url_rule("/view_patient_diagnosis", view_func=v_view_patient_diagnosis, methods=['GET', 'POST'])
app.add_url_rule("/view_patient_diagnosis_success", view_func=v_view_patient_diagnosis_success)
app.add_url_rule("/upload_diagnosis", view_func=v_upload_diagnosis, methods=['GET', 'POST'])
app.add_url_rule("/upload_data_success", view_func=v_upload_data_success, methods=['GET', 'POST'])
app.add_url_rule("/upload_diagnosis_success", view_func=v_upload_diagnosis_success, methods=['GET', 'POST'])

#Manager specific pages
app.add_url_rule("/add_doctor", view_func=v_add_doctor, methods=['GET', 'POST'])
app.add_url_rule("/deactivate_doctor", view_func=v_deactivate_doctor, methods=['GET', 'POST'])
app.add_url_rule("/activate_doctor", view_func=v_activate_doctor, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")