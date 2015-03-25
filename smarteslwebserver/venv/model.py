import psycopg2

DB_CXN_STR = "dbname=smartesl user=appuser password=a0kroger host=localhost port=15432"

class DBAccessor:
	def __init__(self):
		conn = psycopg2.connect(DB_CXN_STR)
		self.curr = conn.cursor()

	def getQuestionById(self,id):
		q = "select * from questions where id = %"
		print q
		pass
	def getStudentListByInstructor(self,instructor):
		pass

	def addInstructor(firstname,lastname,email,phone):
		# insert into instructors ( firstname, lastname, email, phone_number ) values ('Vincent','Engelmann', 'bogus.addr@somehost.com','555-555-5555');
		pass

	def addStudent(self,firstname,lastname,email,phone):
		# insert into students ( firstname, lastname, email, phone_number ) values ('Martin','Sole', 'bogus.addr@somehost.cat','93 304 12 03');

	def addQuestion():
		pass


if __name__ == '__main__':

	dba = DBAccessor()
	dba.addInstructor

	