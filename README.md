# smartesl
PGUSER=myapp PGPASSWORD=dbpass psql -h localhost -p 15432 myapp

# database setup
vagrant@precise64:~$ sudo su - postgres
vagrant@precise64:~$ psql

postgres=# create user appuser with password 'hidden';

postgres=# create database smartesl;

postgres=# \c smartesl;

create table students (student_id serial primary key,
firstname text,
lastname text,
email text,
phone_number text, timestamp timestamp default current_timestamp);

create table instructors (
instructor_id serial PRIMARY KEY,
firstname text,
lastname text,
email text,
phone_number text,
timestamp timestamp default current_timestamp);

create table metatags (
metatag_id serial PRIMARY KEY,
tag_name text
);

 alter table metatags add column question_id integer;

l=# create table choices (
choice_id serial PRIMARY KEY, question_id integer,
tag_name text
);
alter table choices add column choice_text text;


create table questions (
question_id serial primary key,
body text);

# give appuser permission to all these tables, for ex:
smartesl=# grant all privileges on table instructors to appuser;
and also the sequences..
grant all privileges on SEQUENCE instructors_instructor_id_seq to appuser;


# starting appserver
$ . venv/bin/activate
$ python appserver.py


