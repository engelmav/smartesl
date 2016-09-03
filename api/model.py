import psycopg2, json
import sql_lib as sql

DB_CXN_STR = "dbname=smartesl user=appuser password=a0kroger host=localhost port=15432"


class DBAccessor:

    def __init__(self):
        self.conn = psycopg2.connect(DB_CXN_STR)
        self.cur = self.conn.cursor()


    def get_question_by_id(self, id):
        pass

    def get_student_list_by_instructor(self, instructor):
        pass

    def add_instructor(self, firstname, lastname, email, phone):
        self.cur.execute(sql.add_instructor,
            (firstname,lastname,email,phone))
        self.conn.commit()

    def add_student(self, firstname, lastname, email, phone):
        self.cur.execute(sql.add_student
            (firstname,lastname,email,phone))
        self.conn.commit()

    def add_question(self, question_data):
        print question_data
        body = question_data['body']

        self.cur.execute( sql.add_question,(body,) )
        lastQuestionId = self.cur.fetchone()[0]
        print "Last question ID: " + str(lastQuestionId)
        self.conn.commit()

        choices = question_data['choices']

        for choice in choices:
            self.cur.execute(sql.add_choice,
                (lastQuestionId, choice[0], choice[1]))
        self.conn.commit()

        metatags = question_data['metatags']
        for metatag in metatags:
            self.cur.execute(sql.add_metatag, (metatag, lastQuestionId))
        self.conn.commit()
        return lastQuestionId

    def search_questions(self, searchPhrase):
        results = ''
        try:
            self.cur.execute(sql.keyword_question_search,(searchPhrase,))
            results = self.cur.fetchall()
        except psycopg2.Error as e:
            self.conn.rollback()
            print e.pgcode
        return results

    def search_timelines(self, searchPhrase):
        results = ''
        try:
            self.cur.execute(searchSql,(searchPhrase,))
            results = self.cur.fetchall()
        except psycopg2.Error as e:
            self.conn.rollback()
            print e.pgcode
        return results

    def set_current_question(self, qid):
        #         smartesl=# \d current_questions
        #  Table "public.current_questions"
        #    Column    |  Type   | Modifiers
        # -------------+---------+-----------
        #  question_id | integer |
        #  class_id    | integer |
        pass

    def add_timeline(self, timelineData):
        qIds =     timelineData['questionIds']
        tlName =   timelineData['timelineName']
        userName = timelineData['userId']
        self.cur.execute(sql.insert_timeline_questions,(userName, tlName))
        lastSetId = self.cur.fetchone()[0]
        print "Last setID: " + str(lastSetId)
        self.conn.commit()
        for q in qIds:
            self.cur.execute(sql.insert_question_set_list,(lastSetId, q))
        self.conn.commit()

    def get_instructor_classes(self, instructorId):
        self.cur.execute(sql.get_instructor_classes,(instructorId,))
        return self.cur.fetchall()

    def broadcast_question(self, questionId, classId):
        pass

    def get_question_content(self, questionId):
        # get the question body and creator
        self.cur.execute(sql.get_question_content,(questionId,))
        body, creator = self.cur.fetchone()
        # get the choies and their iscorrect value
        self.cur.execute(sql.get_choices_of_question,(questionId,))
        choices = self.cur.fetchall()
        # get the metatags...
        self.cur.execute(sql.get_metatags_of_question,(questionId,))
        metatags = self.cur.fetchall()
        # assemble all the things


if __name__ == '__main__':

    dba = DBAccessor()
    dba.add_student('SomeStudent', 'George', 'somname@host.com', '32 43 22222')
