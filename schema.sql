--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Ubuntu 13.3-1.pgdg20.10+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.10+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;


-- CREATE USER fastapi;
-- CREATE DATABASE fastapi;
-- GRANT ALL PRIVILEGES ON DATABASE fastapi TO fastapi;

--
-- Name: comments; Type: TABLE; Schema: public; Owner: fastapi
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    user_id integer,
    post_id integer,
    body text NOT NULL,
    created_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL
);


ALTER TABLE public.comments OWNER TO fastapi;

--
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: fastapi
--

CREATE SEQUENCE public.comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comments_id_seq OWNER TO fastapi;

--
-- Name: comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fastapi
--

ALTER SEQUENCE public.comments_id_seq OWNED BY public.comments.id;


--
-- Name: migrations; Type: TABLE; Schema: public; Owner: fastapi
--

CREATE TABLE public.migrations (
    migration character varying(255) NOT NULL,
    batch integer NOT NULL
);


ALTER TABLE public.migrations OWNER TO fastapi;

--
-- Name: posts; Type: TABLE; Schema: public; Owner: fastapi
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    created_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL,
    user_id integer NOT NULL,
    title character varying(255) NOT NULL,
    body text NOT NULL
);


ALTER TABLE public.posts OWNER TO fastapi;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: fastapi
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_id_seq OWNER TO fastapi;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fastapi
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: fastapi
--

CREATE TABLE public.users (
    id integer NOT NULL,
    created_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT CURRENT_TIMESTAMP(6) NOT NULL,
    name character varying(255) NOT NULL,
    address text NOT NULL,
    phone_number character varying(11) NOT NULL,
    sex character varying(255) NOT NULL,
    CONSTRAINT users_sex_check CHECK (((sex)::text = ANY ((ARRAY['male'::character varying, 'female'::character varying])::text[])))
);


ALTER TABLE public.users OWNER TO fastapi;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: fastapi
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO fastapi;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fastapi
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: comments id; Type: DEFAULT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.comments ALTER COLUMN id SET DEFAULT nextval('public.comments_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: comments comments_post_id_foreign; Type: FK CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_post_id_foreign FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: comments comments_user_id_foreign; Type: FK CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_user_id_foreign FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: posts posts_user_id_foreign; Type: FK CONSTRAINT; Schema: public; Owner: fastapi
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_user_id_foreign FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

