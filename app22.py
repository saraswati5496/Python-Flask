import cx_Oracle
from flask import Flask, render_template, request

app = Flask(__name__)

#set up the oracle database connection
#dsn = cx_Oracle.makedsn(host='',port='', service_name='')
conn = cx_Oracle.connect("rqbi/rqbi@agii-oradl02.argous.com:1528/CRDEVPDB1")

@app.route('/same', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        dropdown_value = request.form.get('dropdown_name')
        textbox_value = request.form['textbox_name']
        cursor = conn.cursor()
        #cursor.execute(f"select tf.form_number, tbu.tbl_business_code 
        #                 from tbli_form tf
        #                 inner join tbl_business_unit tbu
        #                 ON business_unit_code ='{dropdown_value}' AND form_number = '{textbox_value}' ")
        
        #cursor.execute(f"select form_number, form_name, form_edition, description
        #from tbli_form tf, tbli_form_edition,tbli_form_group
        #join tbl_business_unit tbu
        #on business_unit_code='103';")
        
        #cursor.execute("""select form_number, form_name, form_edition, description, business_unit_code
        #                  from tbli_form tf, tbli_form_edition tfe,tbli_form_group tfg, tbl_business_unit tbc
        #                  where tf.form_id= tfe.form_id
        #                  and tf.form_group_id = tfg.form_group_id 
        #                  and tbc.business_unit_code='107' 
        #                  and tf.form_name = 'SCHEDULE OF VEHICLES (RQ303-0201)' """;)
              
        cursor.execute(f"""select form_number, form_name, form_edition, description, business_unit_code
                          from tbli_form tf, tbli_form_edition tfe,tbli_form_group tfg, tbl_business_unit tbc
                          where tf.form_id= tfe.form_id
                          and tf.form_group_id = tfg.form_group_id 
                          and tbc.business_unit_code='107' 
                          and tf.form_name = 'SCHEDULE OF VEHICLES (RQ303-0201)';""")

        result = cursor.fetchone()
        cursor.close()
        #return f'Result: {result}'
        #return render_template('index22.html')
        return render_template('index22.html', result=result)
    else:
        print("hello world")

if __name__ == '__main__':
    app.run(debug=True)