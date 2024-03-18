import cx_Oracle
import pandas as pd
import hello

dsn = cx_Oracle.makedsn('localhost',1521,'orcl')
db = cx_Oracle.connect('scott','tiger')

text = hello.parsetodata("C:/Users/user/Downloads/24-a-ey-765.pdf")

cursor = db.cursor()
cursor.execute("""select * from emp """ ) 

row = cursor.fetchall()
colname = cursor.description
col = []

for i in colname :
    col.append(i[0])

emp = pd.DataFrame(row, columns = col )
print (emp) 