--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: choices; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE choices (
    choice_id integer NOT NULL,
    question_id integer,
    tag_name text,
    choice_text text,
    iscorrect boolean
);


ALTER TABLE public.choices OWNER TO postgres;

--
-- Name: choices_choice_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE choices_choice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.choices_choice_id_seq OWNER TO postgres;

--
-- Name: choices_choice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE choices_choice_id_seq OWNED BY choices.choice_id;


--
-- Name: classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE classes (
    class_id integer NOT NULL,
    class_name text
);


ALTER TABLE public.classes OWNER TO postgres;

--
-- Name: class_class_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE class_class_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.class_class_id_seq OWNER TO postgres;

--
-- Name: class_class_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE class_class_id_seq OWNED BY classes.class_id;


--
-- Name: instructor_classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE instructor_classes (
    instructor_id integer,
    class_id integer
);


ALTER TABLE public.instructor_classes OWNER TO postgres;

--
-- Name: metatags; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE metatags (
    metatag_id integer NOT NULL,
    tag_name text,
    question_id integer
);


ALTER TABLE public.metatags OWNER TO postgres;

--
-- Name: metatags_metatag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE metatags_metatag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.metatags_metatag_id_seq OWNER TO postgres;

--
-- Name: metatags_metatag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE metatags_metatag_id_seq OWNED BY metatags.metatag_id;


--
-- Name: question_set_list; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE question_set_list (
    set_list_id integer NOT NULL,
    set_id integer,
    question_id integer
);


ALTER TABLE public.question_set_list OWNER TO postgres;

--
-- Name: question_set_list_set_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE question_set_list_set_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_set_list_set_list_id_seq OWNER TO postgres;

--
-- Name: question_set_list_set_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE question_set_list_set_list_id_seq OWNED BY question_set_list.set_list_id;


--
-- Name: question_sets; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE question_sets (
    set_id integer NOT NULL,
    creator_id integer,
    vote_score integer,
    set_name text
);


ALTER TABLE public.question_sets OWNER TO postgres;

--
-- Name: question_sets_set_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE question_sets_set_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_sets_set_id_seq OWNER TO postgres;

--
-- Name: question_sets_set_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE question_sets_set_id_seq OWNED BY question_sets.set_id;


--
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE questions (
    question_id integer NOT NULL,
    body text,
    creator integer
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- Name: questions_question_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE questions_question_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_question_id_seq OWNER TO postgres;

--
-- Name: questions_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE questions_question_id_seq OWNED BY questions.question_id;


--
-- Name: student_classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE student_classes (
    student_id integer,
    class_id integer
);


ALTER TABLE public.student_classes OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    user_id integer NOT NULL,
    firstname text,
    lastname text,
    email text,
    phone_number text,
    "timestamp" timestamp without time zone DEFAULT now(),
    role text,
    username text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE user_id_seq OWNED BY users.user_id;


--
-- Name: choice_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY choices ALTER COLUMN choice_id SET DEFAULT nextval('choices_choice_id_seq'::regclass);


--
-- Name: class_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY classes ALTER COLUMN class_id SET DEFAULT nextval('class_class_id_seq'::regclass);


--
-- Name: metatag_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY metatags ALTER COLUMN metatag_id SET DEFAULT nextval('metatags_metatag_id_seq'::regclass);


--
-- Name: set_list_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY question_set_list ALTER COLUMN set_list_id SET DEFAULT nextval('question_set_list_set_list_id_seq'::regclass);


--
-- Name: set_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY question_sets ALTER COLUMN set_id SET DEFAULT nextval('question_sets_set_id_seq'::regclass);


--
-- Name: question_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY questions ALTER COLUMN question_id SET DEFAULT nextval('questions_question_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: choices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY choices (choice_id, question_id, tag_name, choice_text, iscorrect) FROM stdin;
217	222	\N	create	f
218	222	\N	created	t
219	222	\N	creating	\N
220	223	\N	arrive	f
221	223	\N	arrived	t
222	224	\N	choice text	f
223	225	\N	created	t
224	225	\N	creating	\N
225	225	\N	create	\N
226	226	\N	created	t
227	226	\N	creating	\N
228	226	\N	create	\N
229	227	\N	choice text	f
230	228	\N	choice text	f
231	229	\N	choice text	f
232	230	\N	choice text	f
233	231	\N	choice text	f
234	232	\N	choice text	f
235	233	\N	choice text	f
236	234	\N	choice text	f
237	235	\N	choice text	f
238	236	\N	choice text	f
239	237	\N	choice text	f
240	238	\N	choice text	f
241	239	\N	choice text	f
242	240	\N	choice text	f
243	241	\N	choice text	f
244	242	\N	choice text	f
245	243	\N	choice text	f
246	244	\N	choice text	f
247	245	\N	choice text	f
248	246	\N	choice text	f
249	247	\N	choice text	f
250	248	\N	choice text	f
251	249	\N	choice text	f
252	250	\N	choice text	f
253	251	\N	choice text	f
254	252	\N	choice text	f
255	253	\N	choice text	f
256	254	\N	choice text	f
257	255	\N	choice text	f
258	256	\N	choice text	f
259	257	\N	choice text	f
260	258	\N	choice text	f
261	259	\N	goes	f
262	259	\N	went	t
263	259	\N	did went	\N
264	260	\N	working	t
265	260	\N	worked	\N
266	260	\N		\N
267	261	\N	choice text	f
268	262	\N	choice text	f
269	263	\N	choice text	f
270	264	\N	choice text	f
271	265	\N	choice text	f
272	266	\N	choice text	f
273	267	\N	choice text	f
274	268	\N	choice text	f
275	269	\N	choice text	f
276	270	\N	choice text	f
277	271	\N		f
278	272	\N	dfd	f
279	272	\N	vdvd	\N
280	273	\N	drg	t
281	273	\N	dfg	\N
282	274	\N	drg	t
283	274	\N	dfg	\N
\.


--
-- Name: choices_choice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('choices_choice_id_seq', 283, true);


--
-- Name: class_class_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('class_class_id_seq', 1, true);


--
-- Data for Name: classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY classes (class_id, class_name) FROM stdin;
1	dummy class
\.


--
-- Data for Name: instructor_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY instructor_classes (instructor_id, class_id) FROM stdin;
5	1
\.


--
-- Data for Name: metatags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY metatags (metatag_id, tag_name, question_id) FROM stdin;
201	preterit	223
202	elided d	223
203		223
205	passive	225
206	participle	225
207		225
211	metatag	228
212	metatag	229
213	metatag	230
214	metatag	231
215	metatag	232
216	metatag	233
217	metatag	234
218	metatag	235
219	metatag	236
220	metatag	237
221	metatag	238
222	metatag	239
223	metatag	240
224	metatag	241
225	metatag	242
226	metatag	243
227	metatag	244
228	metatag	245
229	metatag	246
230	metatag	247
231	metatag	248
232	metatag	249
233	metatag	250
234	metatag	251
235	metatag	252
236	metatag	253
237	metatag	254
238	metatag	255
239	metatag	256
240	metatag	257
241	metatag	258
242	preterit	259
243	to be	259
244	third person plural	259
250	metatag	264
251	metatag	265
252	metatag	266
253	metatag	267
254	metatag	268
255	metatag	269
258		272
260	dfg	274
204	metatag	224
208	passive	226
209	participle	226
210	metatag	227
245	gerund	260
246	work	260
247	metatag	261
248	metatag	262
249	metatag	263
256	metatag	270
257		271
259	dfg	273
198	passive voice	222
199	participle	222
200	verbs	222
\.


--
-- Name: metatags_metatag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('metatags_metatag_id_seq', 260, true);


--
-- Data for Name: question_set_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY question_set_list (set_list_id, set_id, question_id) FROM stdin;
1	5	273
2	5	274
\.


--
-- Name: question_set_list_set_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('question_set_list_set_list_id_seq', 2, true);


--
-- Data for Name: question_sets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY question_sets (set_id, creator_id, vote_score, set_name) FROM stdin;
1	5	0	\N
2	5	0	\N
3	5	0	\N
4	5	0	
5	5	0	
\.


--
-- Name: question_sets_set_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('question_sets_set_id_seq', 5, true);


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY questions (question_id, body, creator) FROM stdin;
222	Twitter was ______ in 2006.	\N
223	Columbus ___ in 2492.	\N
224	Twitter was ______ in 2006.	\N
225	Twitter was ______ in 2006.	\N
226	Twitter was ______ in 2006.	\N
227	Twitter was ______ in 2006.	\N
228	mike was made	\N
229	Aliens invaded in 1681.	\N
230	Aliens invaded and created stuff on earth.	\N
231	Twitter was ______ in 2006.	\N
232	Twitter was ______ in 2006.	\N
233	Twitter was ______ in 2006.	\N
234	Twitter was ______ in 2006.	\N
235	Twitter was ______ in 2006.	\N
236	Twitter was ______ in 2006.	\N
237	Twitter was ______ in 2006.	\N
238	Twitter was ______ in 2006.	\N
239	Twitter was ______ in 2006.	\N
240	Twitter was ______ in 2006.	\N
241	Twitter was ______ in 2006.	\N
242	Twitter was ______ in 2006.	\N
243	Twitter was ______ in 2006.	\N
244	Twitter was ______ in 2006.	\N
245	Twitter was ______ in 2006.	\N
246	Twitter was ______ in 2006.	\N
247	Twitter was ______ in 2006.	\N
248	Twitter was ______ in 2006.	\N
249	Twitter was ______ in 2006.	\N
250	Twitter was ______ in 2006.	\N
251	Twitter was ______ in 2006.	\N
252	Twitter was ______ in 2006.	\N
253	Twitter was ______ in 2006.	\N
254	Twitter was ______ in 2006.	\N
255	Twitter was ______ in 2006.	\N
256	Twitter was ______ in 2006.	\N
257	Twitter was ______ in 2006.	\N
258	Twitter was ______ in 2006.	\N
259	Luciana and Gabriel ____ to school yesterday.	\N
260	Although ______ at a restaurant sounds easy, it's actually really hard.	\N
261	dfgsdgf	\N
262	Twitter was ______ in 2006.	\N
263	cbxcvbnchmfb	\N
264	adsfgadsf	\N
265	adsfgadsf	\N
266	123	\N
267	456	\N
268	Twitter was ______ in 2006.	\N
269	567	\N
270	Twitter was ______ in 2006.	\N
271		\N
272	dfd	\N
273	rgsdfg	\N
274	rgsdfg	\N
\.


--
-- Name: questions_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('questions_question_id_seq', 274, true);


--
-- Data for Name: student_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY student_classes (student_id, class_id) FROM stdin;
6	1
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('user_id_seq', 6, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users (user_id, firstname, lastname, email, phone_number, "timestamp", role, username) FROM stdin;
1	Martin	Sole	bogus.addr@somehost.cat	93 304 12 03	2015-03-25 12:44:03.744955	\N	\N
3	SomeStudent	George	somname@host.com	32 43 22222	2015-03-25 20:01:39.527831	\N	\N
4	SomeStudent	George	somname@host.com	32 43 22222	2015-03-26 00:02:34.558416	\N	\N
5	vincent	engelmann	\N	2222222	2015-04-09 15:13:43.914984	instructor	vengelmann
6	jose	martin	\N	2222222	2015-04-09 15:14:43.197603	student	jmartin
\.


--
-- Name: choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY choices
    ADD CONSTRAINT choices_pkey PRIMARY KEY (choice_id);


--
-- Name: class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY classes
    ADD CONSTRAINT class_pkey PRIMARY KEY (class_id);


--
-- Name: metatags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY metatags
    ADD CONSTRAINT metatags_pkey PRIMARY KEY (metatag_id);


--
-- Name: question_set_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY question_set_list
    ADD CONSTRAINT question_set_list_pkey PRIMARY KEY (set_list_id);


--
-- Name: question_sets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY question_sets
    ADD CONSTRAINT question_sets_pkey PRIMARY KEY (set_id);


--
-- Name: questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (question_id);


--
-- Name: students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT students_pkey PRIMARY KEY (user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: choices; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE choices FROM PUBLIC;
REVOKE ALL ON TABLE choices FROM postgres;
GRANT ALL ON TABLE choices TO postgres;
GRANT ALL ON TABLE choices TO appuser;


--
-- Name: choices_choice_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE choices_choice_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE choices_choice_id_seq FROM postgres;
GRANT ALL ON SEQUENCE choices_choice_id_seq TO postgres;
GRANT ALL ON SEQUENCE choices_choice_id_seq TO appuser;


--
-- Name: classes; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE classes FROM PUBLIC;
REVOKE ALL ON TABLE classes FROM postgres;
GRANT ALL ON TABLE classes TO postgres;
GRANT ALL ON TABLE classes TO appuser;


--
-- Name: instructor_classes; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE instructor_classes FROM PUBLIC;
REVOKE ALL ON TABLE instructor_classes FROM postgres;
GRANT ALL ON TABLE instructor_classes TO postgres;
GRANT ALL ON TABLE instructor_classes TO appuser;


--
-- Name: metatags; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE metatags FROM PUBLIC;
REVOKE ALL ON TABLE metatags FROM postgres;
GRANT ALL ON TABLE metatags TO postgres;
GRANT ALL ON TABLE metatags TO appuser;


--
-- Name: metatags_metatag_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE metatags_metatag_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE metatags_metatag_id_seq FROM postgres;
GRANT ALL ON SEQUENCE metatags_metatag_id_seq TO postgres;
GRANT ALL ON SEQUENCE metatags_metatag_id_seq TO appuser;


--
-- Name: question_set_list; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE question_set_list FROM PUBLIC;
REVOKE ALL ON TABLE question_set_list FROM postgres;
GRANT ALL ON TABLE question_set_list TO postgres;
GRANT ALL ON TABLE question_set_list TO appuser;


--
-- Name: question_set_list_set_list_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE question_set_list_set_list_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE question_set_list_set_list_id_seq FROM postgres;
GRANT ALL ON SEQUENCE question_set_list_set_list_id_seq TO postgres;
GRANT ALL ON SEQUENCE question_set_list_set_list_id_seq TO appuser;


--
-- Name: question_sets; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE question_sets FROM PUBLIC;
REVOKE ALL ON TABLE question_sets FROM postgres;
GRANT ALL ON TABLE question_sets TO postgres;
GRANT ALL ON TABLE question_sets TO appuser;


--
-- Name: question_sets_set_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE question_sets_set_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE question_sets_set_id_seq FROM postgres;
GRANT ALL ON SEQUENCE question_sets_set_id_seq TO postgres;
GRANT ALL ON SEQUENCE question_sets_set_id_seq TO appuser;


--
-- Name: questions; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE questions FROM PUBLIC;
REVOKE ALL ON TABLE questions FROM postgres;
GRANT ALL ON TABLE questions TO postgres;
GRANT ALL ON TABLE questions TO appuser;


--
-- Name: questions_question_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE questions_question_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE questions_question_id_seq FROM postgres;
GRANT ALL ON SEQUENCE questions_question_id_seq TO postgres;
GRANT ALL ON SEQUENCE questions_question_id_seq TO appuser;


--
-- Name: student_classes; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE student_classes FROM PUBLIC;
REVOKE ALL ON TABLE student_classes FROM postgres;
GRANT ALL ON TABLE student_classes TO postgres;
GRANT ALL ON TABLE student_classes TO appuser;


--
-- Name: users; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE users FROM PUBLIC;
REVOKE ALL ON TABLE users FROM postgres;
GRANT ALL ON TABLE users TO postgres;
GRANT ALL ON TABLE users TO appuser;


--
-- Name: user_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE user_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE user_id_seq FROM postgres;
GRANT ALL ON SEQUENCE user_id_seq TO postgres;
GRANT ALL ON SEQUENCE user_id_seq TO appuser;


--
-- PostgreSQL database dump complete
--

