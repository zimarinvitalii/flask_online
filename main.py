from flask import request

from flask import Flask

from datetime import datetime
from utils import generate_password as gp

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/generate-password/')
def generate_password():
    password_len = request.args.get('password-len')

    if not password_len:
        password_len = 10
    else:
        if password_len.isdigit():
            password_len = int(password_len)
        else:
            return 'Invalid parameter password-len. Should be int.\n'

    print('password_len', password_len, type(password_len))
    password = gp(password_len)
    return f'{password}\n'


@app.route('/emails/create/')
def create_email():
    import sqlite3

    con = sqlite3.connect('exampl.db')
    # http://127.0.0.1:5000/emails/create/?contactName=Vitalii&email=wow@mail.com
    contact_name = request.args['contactName']
    email_value = request.args['email']

    cur = con.cursor()
    sql_query = f'''
    INSERT INTO emails (contactName, emailValue)
    VALUES ('{contact_name}', '{email_value}');
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'create_email'


@app.route('/emails/read/')
def read_email():
    import sqlite3

    con = sqlite3.connect('exampl.db')

    cur = con.cursor()
    sql_query = f'''
       SELECT * FROM emails;
       '''
    cur.execute(sql_query)
    result = cur.fetchall()
    con.close()
    return str(result)



@app.route('/emails/delete/')
def delete_email():
    import sqlite3

    con = sqlite3.connect('exampl.db')

    cur = con.cursor()
    sql_query = f'''
           DELETE FROM emails;
           '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'delete_email'

@app.route('/emails/update/')
def update_email():
    import sqlite3

    # http://127.0.0.1:5000/emails/create/?contactName=Vitalii&email=wow@mail.com

    contact_name = request.args['contactName']
    email_value = request.args['email']

    con = sqlite3.connect('exampl.db')

    cur = con.cursor()
    sql_query = f'''
    UPDATE emails
    SET contactName = '{contact_name}'
    WHERE emailValue = '{email_value}';
           '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'update_email'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#