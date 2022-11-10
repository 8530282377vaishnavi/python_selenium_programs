import mysql.connector
con=mysql.connector.connect(host="localhost", port="3306",database="blog")
curs=con.cursor()
curs.execute("insert into student values(123,'kim')")
con.commit()
con.close()

print("finish.........")
