import psycopg2, json

DB_CXN_STR = "dbname=smartesl user=appuser password=a0kroger host=localhost port=15432"

class DBAccessor:
    # select document from (select to_tsvector(q.body) || ' ' || to_tsvector(string_agg(distinct c.choice_text, ' | ')) || ' ' || to_tsvector(string_agg(distinct m.tag_name, ' | ')) as document from questions q join choices c on q.question_id = c.question_id join metatags m on m.question_id = q.question_id group by q.question_id) as doc where doc.document @@ to_tsquery('preterit');

    def __init__(self):
        self.conn = psycopg2.connect(DB_CXN_STR)
        self.cur = self.conn.cursor()

    def getUserData(self,username):
        print "searching for " + username
        self.cur.execute("""
           SELECT firstname, lastname, role from users
           WHERE username = %s;""",
           (username,))
        results = self.cur.fetchall()
        resultLength = len(results)
        if resultLength == 1:
            return [ results[0][0], results[0][1], results[0][2] ]
        else:
            return 'invalid user'

    def getQuestionById(self,id):
        # select q.body, c.choice_text from questions q left join choices c on q.question_id = c.question_id;
        q = "select * from questions where id = %"
        print q
        pass

    def getStudentListByInstructor(self,instructor):
        pass

    def addInstructor(self,firstname,lastname,email,phone):
        self.cur.execute("""
            insert into instructors ( firstname, lastname, email, phone_number )
            values ( %s, %s, %s, %s );""",
            (firstname,lastname,email,phone))
        self.conn.commit()

    def addStudent(self,firstname,lastname,email,phone):
        self.cur.execute("""
            insert into students ( firstname, lastname, email, phone_number )
            values ( %s, %s, %s, %s );""",
            (firstname,lastname,email,phone))
        self.conn.commit()

    def addQuestion(self,question_data):
        print question_data
        body = question_data['body']

        self.cur.execute("""
           insert into questions ( body )
           values ( %s ) RETURNING question_id;""",
           (body,))
        lastQuestionId = self.cur.fetchone()[0]
        print "Last question ID: " + str(lastQuestionId)
        self.conn.commit()

        choices = question_data['choices']

        for choice in choices:
            self.cur.execute("""
                insert into choices ( question_id, choice_text, iscorrect )
                values ( %s, %s, %s );""",
                (lastQuestionId, choice[0], choice[1]))
        self.conn.commit()

        metatags = question_data['metatags']
        for metatag in metatags:
            self.cur.execute("""
                insert into metatags ( tag_name, question_id )
                values ( %s, %s );""",
                (metatag, lastQuestionId))
        self.conn.commit()
        return lastQuestionId
    def searchQuestions(self,searchPhrase):
        searchSql = """
            select body from (
                select to_tsvector(q.body) || ' ' || 
                to_tsvector(string_agg(distinct c.choice_text, ' | ')) || ' ' || 
                to_tsvector(string_agg(distinct m.tag_name, ' | ')) as document, q.body as body
                from questions q 
                join choices c on q.question_id = c.question_id 
                join metatags m on m.question_id = q.question_id 
                group by q.question_id) as doc
            where doc.document @@ to_tsquery(%s);
            """
        results = ''
        try:
            self.cur.execute(searchSql,(searchPhrase,))
            results = self.cur.fetchall()
        except psycopg2.Error as e:
            self.conn.rollback()
            print e.pgcode
        return results

    def addTimeline(self, questionIdList):
        print quesitonIdList

if __name__ == '__main__':

    dba = DBAccessor()
    dba.addStudent('SomeStudent','George','somname@host.com','32 43 22222')
    # http://initd.org/psycopg/docs/usage.html

