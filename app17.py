import cx_Oracle
from flask import Flask, render_template, request
app = Flask(__name__)
connection = cx_Oracle.connect("rqbi/rqbi@agii-oradl02.argous.com:1528/CRDEVPDB1")
@app.route('/', methods=['GET','POST'])
def index():
    print("version is: "+ connection.version)
    cursor = connection.cursor()
    cursor.execute("select business_unit_code from TBL_BUSINESS_UNIT") 
    #print(w)    
    dropdown_values = [row[0] for row in cursor.fetchall()]
    if request.method == 'POST':
        dropdown_value = request.form['dropdown']
        #text_value = request.form['Text']
        #cursor.execute(f"""select form_number as Form Number, form_edition as Form Edition, form_name as Form Title, description as Form Group 
        #                   from tbli_form tf, tbli_form_edition tfe, tbli_form_group tfg, tbl_business_unit tbc
        #                   where tf.form_id = tfe.form_id
        #                   and tf.form_group_id = tfg.form_group_id 
        #                   and value =:1 
        #                   and Text =:2""", (dropdown_value, text_value))
        cursor.execute("""select business_unit_code as Business_unit_code, name as Name, last_modified_by as Last_modified_by, last_modified_date as Last modified_date from tbl_business_unit 
                           where value =:1""", (dropdown_value))
                           #Form Number 
                           #Form Edition
                           #Form Title  
                           #Form Group  
                          
        results = cursor.fetchall()
        return render_template('index15.html', results = results)
    return render_template('index15.html', dropdown_values=dropdown_values)
    
if __name__ == '__main__':
    app.run(debug=True)