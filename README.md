# Connect to database
PGUSER=myapp PGPASSWORD=dbpass psql -h localhost -p 15432 myapp

# Setup Database
vagrant@precise64:~$ sudo su - postgres
vagrant@precise64:~$ psql

## Run statements
```sql
create user appuser with password 'hidden';

create database smartesl;

\c smartesl;

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
	question_id integer,
	tag_name text);

create table choices (
	choice_id serial PRIMARY KEY, question_id integer,
	tag_name text,
	choice_text text,
    iscorrect boolean);

create table questions (
	question_id serial primary key,
	body text);

create table question_sets (
	set_id serial PRIMARY KEY,
	instructor_id integer,
	vote_score integer);

create table question_set_list (
	set_list_id serial PRIMARY KEY,
	set_id integer,
	question_id integer);
```

# give appuser permission to all these tables, for ex:
smartesl=# grant all privileges on table instructors to appuser;
and also the sequences..
grant all privileges on SEQUENCE instructors_instructor_id_seq to appuser;


# starting appserver
$ . venv/bin/activate
$ python appserver.py

# Definitions
## Class
A class is a group of sessions over time. A class has many sessions. A class has a schedule.

## Session
A session has students in it. A session has an instructor.


