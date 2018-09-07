import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



tableCreateText = """CREATE TABLE IF NOT EXISTS members(
    id integer PRIMARY KEY,
    first_Name text NOT NULL,
    last_Name text NOT NULL,
    phone1 text NOT NULL,
    email1 text,
    can_Text integer NOT NULL,
    sex NOT NULL,
    married_Status text NOT NULL,
    created_Date text,
    attended_Ids text
)"""

conn = create_connection('member.db')
if conn is not None:
    create_table(conn,tableCreateText)
else:
    print ("Error! Cannot create the DB connection")

c = conn.cursor()

#Still need to do a lot of work to actually have the member saved to the DB. Should probably also check to make sure it's not a duplicate.