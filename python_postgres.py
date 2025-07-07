import psycopg2

hostname='localhost'
database='postgres'
username='postgres'
pwd='Ispace@9876'
port_id= 5432
conn=None
cur=None
# try:
#     conn = psycopg2.connect(
#         host=hostname,
#         dbname=database,
#         user=username,
#         password=pwd,
#         port=port_id)
#     cur = conn.cursor()

    # create_script=''' CREATE TABLE IF NOT EXISTS EMPLOYEE(
    #                     id  int PRIMARY KEY,
    #                     name  varchar(40) NOT NULL,
    #                     salary int,
    #                     dept_id varchar(30)
    #                     )'''
    cur.execute(create_script)
    # alter_script='''ALTER TABLE EMPLOYEE
    #                 ADD column email varchar(100) NOT NULL,
    #                 ADD COLUMN joining_date DATE
    #                 '''
    # cur.execute(alter_script)
    # insert_script= 'INSERT INTO EMPLOYEE(id,name,salary,dept_id,email,joining_date) values(%s,%s,%s,%s,%s,%s)'
    # insert_values=[(1,"yasmin",100000,"IT","yasmin@gmail.com",'2022-01-20'),(2,"yasin",50000,"IT","yasin@gmail.com",'2021-02-22'),(3,"mehattar",70000,"IT","yasmi@gmail.com",'2023-09-24')]
   
    # cur.executemany(insert_script,insert_values)
    # conn.commit()
    
except Exception as error:

    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


