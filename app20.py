from flask import Flask, render_template, request
import cx_Oracle
app = Flask(__name__)
# Set up the Oracle connection
#dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')
#connection = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

connection = cx_Oracle.connect("rqbi/rqbi@agii-oradl02.argous.com:1528/CRDEVPDB1")
@app.route('/', methods=['GET', 'POST'])
def index():
    # Fetch the dropdown list from the database
    cursor = connection.cursor()
    #cursor.execute("SELECT DISTINCT record FROM table_name")
    cursor.execute("SELECT DISTINCT business_unit_code FROM tbl_business_unit")
    dropdown_list = [row[0] for row in cursor.fetchall()]
    # Retrieve the selected record and textbox value
    selected_record = ''
    textbox_value = ''
    if request.method == 'POST':
        selected_record = request.form.get('record')
        textbox_value = request.form.get('textbox')
    # Retrieve the corresponding records from the database
                           #Form Number 
                           #Form Edition
                           #Form Title  
                           #Form Group
    records = []
    if selected_record and textbox_value:
        cursor.execute(f"""select form_number, form_edition, form_name, description 
                           from tbli_form tf, tbli_form_edition tfe, tbli_form_group tfg, tbl_business_unit tbc
                           where tf.form_id= tfe.form_id
                           and tf.form_group_id = tfg.form_group_id 
                           and tbc.business_unit_code =:record
                           and tf.form_number =:value""", record=selected_record, value=textbox_value)
        #cursor.execute("SELECT * FROM tbl_business_unit WHERE business_unit_code = :record AND name = :value",
                    #   record=selected_record, value=textbox_value)

        #cursor.execute("SELECT * FROM table_name WHERE record = :record AND column_name = :value",
        #               record=selected_record, value=textbox_value)

                        #cursor.execute(f"""select form_number as Form Number, form_edition as Form Edition, form_name as Form Title, description as Form Group 
                        #   from tbli_form tf, tbli_form_edition tfe, tbli_form_group tfg, tbl_business_unit tbc
                        #   where tf.form_id= tfe.form_id
                        #   and tf.form_group_id = tfg.form_group_id 
                        #   and value =:1 
                        #   and Text =:2""", (dropdown_value, text_value))
                        #OR
        #cursor.execute("""select business_unit_code as Business_unit_code, name as Name, last_modified_by as Last_modified_by, last_modified_date as Last modified_date from tbl_business_unit 
        #   where value =:1""", (dropdown_value))
        records = cursor.fetchall()
    return render_template('index20.html', dropdown_list=dropdown_list, selected_record=selected_record,
                           textbox_value=textbox_value, records=records)
if __name__ == '__main__':
    app.run(debug=True)