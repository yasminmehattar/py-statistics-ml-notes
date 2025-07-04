import psycopg2

hostname='localhost'
database='postgres'
username='postgres'
pwd='Ispace@9876'
port_id= 5432
conn=None
cur=None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    cur = conn.cursor()

    create_script=''' CREATE TABLE IF NOT EXISTS EMPLOYEE(
                        id  int PRIMARY KEY,
                        name  varchar(40) NOT NULL,
                        salary int,
                        dept_id varchar(30)
                        )'''
    alter_script='''ALTER TABLE EMPLOYEE
                    ADD column email varchar(100) NOT NULL,
                    ADD COLUMN joining_date DATE
                    '''
    cur.execute(create_script)
    cur.execute(alter_script)
    conn.commit()
    
except Exception as error:

    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


