import sqlite3

con = sqlite3.connect('exampl.db')
cur = con.cursor()
sql_query = '''
CREATE TABLE IF NOT EXISTS emails
(contactName text, emailValue text);
'''

cur.execute(sql_query)

con.commit()

con.close()
