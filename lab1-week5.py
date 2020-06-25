import sqlite3


def Main():
	try:
		user = int(input("please enter a number?"))
		print(user)
		con = sqlite3.connect('student.db')
    
		cur = con.cursor() 

		cur.execute("CREATE TABLE student(Id INT, studentNumber VARCHAR, LName VARCHAR, FName VARCHAR)")
		cur.execute("INSERT INTO Pets VALUES(1, '04980074', 'Alamer', 'Ahmad')")
		cur.execute("INSERT INTO Pets VALUES(2, '040980077', 'balbaw', 'Rockey')")
		
    
		con.commit()

		cur.execute("SELECT * FROM student")
		data = cur.fetchone[0]
		
		for row in data:
			print(row)

	except sqlite3.Error:
		if con:
			con.rollback()
	finally:
		if con:
			con.close()

if __name__ == '__main__':
	Main()

