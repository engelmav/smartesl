get_user_data = """
SELECT userName, firstname, lastname, role FROM users
WHERE username = %s;
"""

get_question_by_id = """
SELECT
  q.body
  , c.choice_text
FROM questions q
LEFT JOIN choices c 
ON q.question_id = c.question_id;
WHERE q.id = %s;
"""

add_instructor = """
INSERT INTO instructors ( firstname, lastname, email, phone_number )
values ( %s, %s, %s, %s );
"""

add_student = """
insert into students ( firstname, lastname, email, phone_number )
values ( %s, %s, %s, %s );"""

add_question = """
insert into questions ( body )
values ( %s ) returning question_id;
"""

add_choice = """
insert into choices ( question_id, choice_text, iscorrect )
values ( %s, %s, %s );
"""

add_metatag = """
insert into metatags ( tag_name, question_id )
values ( %s, %s );
"""

keyword_question_search = """
select qid,body from (
    select
      to_tsvector(q.body) || ' ' ||
      to_tsvector(string_agg(distinct c.choice_text, ' | ')) || ' ' ||
      to_tsvector(string_agg(distinct m.tag_name, ' | ')) as document,
      q.question_id as qid,
      q.body as body
    from questions q
    join choices c on q.question_id = c.question_id
    join metatags m on m.question_id = q.question_id
    group by q.question_id) as doc
where doc.document @@ to_tsquery(%s);
"""

keyword_timeline_search = """
select sid, document from
    ( select
        qs.set_id as sid,
        to_tsvector(qs.set_name) || ' ' ||
        to_tsvector(u.username) as document
      from question_sets qs join users u on qs.creator_id = u.user_id ) as doc
where doc.document @@ to_tsquery(%s);
"""

insert_timeline_questions = """
insert into question_sets
    (creator_id, set_name,vote_score)
    values ((select user_id from users where username = %s), %s, 0)
returning set_id;
"""

insert_question_set_list = """
insert into question_set_list
    (set_id, question_id)
    values (%s, %s);
"""

get_instructor_classes = """
select class_name from classes where class_id in
    (select class_id from instructor_classes where instructor_id =
        (select user_id from users where username = %s))
"""

get_question_content = """
select body, creator from questions
where question_id = %s
"""

get_choices_of_question = """
select choice_text, iscorrect from choices where question_id = %s;
"""

get_metatags_of_question = """
select tag_name from metatags where question_id = %s;
"""

get_groups_for_user = """
select gv.view_name from group_views gv
left join user_groups ug
on gv.group_id = ug.group_id
left join users u
on u.group_id = ug.group_id where username = %s;
"""