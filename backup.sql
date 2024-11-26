--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Ubuntu 15.4-2.pgdg22.04+1)
-- Dumped by pg_dump version 15.10 (Ubuntu 15.10-1.pgdg22.04+1)

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

--
-- Name: btree_gin; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS btree_gin WITH SCHEMA public;


--
-- Name: EXTENSION btree_gin; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gin IS 'support for indexing common datatypes in GIN';


--
-- Name: btree_gist; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS btree_gist WITH SCHEMA public;


--
-- Name: EXTENSION btree_gist; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gist IS 'support for indexing common datatypes in GiST';


--
-- Name: citext; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


--
-- Name: cube; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;


--
-- Name: EXTENSION cube; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION cube IS 'data type for multidimensional cubes';


--
-- Name: dblink; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS dblink WITH SCHEMA public;


--
-- Name: EXTENSION dblink; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dblink IS 'connect to other PostgreSQL databases from within a database';


--
-- Name: dict_int; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS dict_int WITH SCHEMA public;


--
-- Name: EXTENSION dict_int; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_int IS 'text search dictionary template for integers';


--
-- Name: dict_xsyn; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS dict_xsyn WITH SCHEMA public;


--
-- Name: EXTENSION dict_xsyn; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_xsyn IS 'text search dictionary template for extended synonym processing';


--
-- Name: earthdistance; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS earthdistance WITH SCHEMA public;


--
-- Name: EXTENSION earthdistance; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION earthdistance IS 'calculate great-circle distances on the surface of the Earth';


--
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- Name: hstore; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS hstore WITH SCHEMA public;


--
-- Name: EXTENSION hstore; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION hstore IS 'data type for storing sets of (key, value) pairs';


--
-- Name: intarray; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS intarray WITH SCHEMA public;


--
-- Name: EXTENSION intarray; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION intarray IS 'functions, operators, and index support for 1-D arrays of integers';


--
-- Name: ltree; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS ltree WITH SCHEMA public;


--
-- Name: EXTENSION ltree; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION ltree IS 'data type for hierarchical tree-like structures';


--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track planning and execution statistics of all SQL statements executed';


--
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: pgrowlocks; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgrowlocks WITH SCHEMA public;


--
-- Name: EXTENSION pgrowlocks; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgrowlocks IS 'show row-level locking information';


--
-- Name: pgstattuple; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgstattuple WITH SCHEMA public;


--
-- Name: EXTENSION pgstattuple; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgstattuple IS 'show tuple-level statistics';


--
-- Name: tablefunc; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;


--
-- Name: EXTENSION tablefunc; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';


--
-- Name: unaccent; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;


--
-- Name: EXTENSION unaccent; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION unaccent IS 'text search dictionary that removes accents';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- Name: xml2; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS xml2 WITH SCHEMA public;


--
-- Name: EXTENSION xml2; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION xml2 IS 'XPath querying and XSLT';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_profile; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.account_profile (
    id bigint NOT NULL,
    date_of_birth date,
    photo character varying(100) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.account_profile OWNER TO qcjurrgz;

--
-- Name: account_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.account_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_profile_id_seq OWNER TO qcjurrgz;

--
-- Name: account_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.account_profile_id_seq OWNED BY public.account_profile.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO qcjurrgz;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO qcjurrgz;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO qcjurrgz;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO qcjurrgz;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO qcjurrgz;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO qcjurrgz;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO qcjurrgz;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO qcjurrgz;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO qcjurrgz;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO qcjurrgz;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO qcjurrgz;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO qcjurrgz;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO qcjurrgz;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO qcjurrgz;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO qcjurrgz;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO qcjurrgz;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: easy_thumbnails_source; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.easy_thumbnails_source (
    id integer NOT NULL,
    storage_hash character varying(40) NOT NULL,
    name character varying(255) NOT NULL,
    modified timestamp with time zone NOT NULL
);


ALTER TABLE public.easy_thumbnails_source OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_source_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.easy_thumbnails_source_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.easy_thumbnails_source_id_seq OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_source_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.easy_thumbnails_source_id_seq OWNED BY public.easy_thumbnails_source.id;


--
-- Name: easy_thumbnails_thumbnail; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.easy_thumbnails_thumbnail (
    id integer NOT NULL,
    storage_hash character varying(40) NOT NULL,
    name character varying(255) NOT NULL,
    modified timestamp with time zone NOT NULL,
    source_id integer NOT NULL
);


ALTER TABLE public.easy_thumbnails_thumbnail OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_thumbnail_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.easy_thumbnails_thumbnail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.easy_thumbnails_thumbnail_id_seq OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_thumbnail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.easy_thumbnails_thumbnail_id_seq OWNED BY public.easy_thumbnails_thumbnail.id;


--
-- Name: easy_thumbnails_thumbnaildimensions; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.easy_thumbnails_thumbnaildimensions (
    id integer NOT NULL,
    thumbnail_id integer NOT NULL,
    width integer,
    height integer,
    CONSTRAINT easy_thumbnails_thumbnaildimensions_height_check CHECK ((height >= 0)),
    CONSTRAINT easy_thumbnails_thumbnaildimensions_width_check CHECK ((width >= 0))
);


ALTER TABLE public.easy_thumbnails_thumbnaildimensions OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_thumbnaildimensions_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.easy_thumbnails_thumbnaildimensions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.easy_thumbnails_thumbnaildimensions_id_seq OWNER TO qcjurrgz;

--
-- Name: easy_thumbnails_thumbnaildimensions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.easy_thumbnails_thumbnaildimensions_id_seq OWNED BY public.easy_thumbnails_thumbnaildimensions.id;


--
-- Name: locations_comment; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.locations_comment (
    id bigint NOT NULL,
    text text NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    location_id bigint NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.locations_comment OWNER TO qcjurrgz;

--
-- Name: locations_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.locations_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_comment_id_seq OWNER TO qcjurrgz;

--
-- Name: locations_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.locations_comment_id_seq OWNED BY public.locations_comment.id;


--
-- Name: locations_location; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.locations_location (
    id bigint NOT NULL,
    title character varying(300) NOT NULL,
    description character varying(500) NOT NULL,
    image character varying(255) NOT NULL,
    image_alt character varying(100) NOT NULL,
    location_types character varying(50) NOT NULL,
    posted_date timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    slug character varying(200) NOT NULL
);


ALTER TABLE public.locations_location OWNER TO qcjurrgz;

--
-- Name: locations_location_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.locations_location_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_location_id_seq OWNER TO qcjurrgz;

--
-- Name: locations_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.locations_location_id_seq OWNED BY public.locations_location.id;


--
-- Name: locations_location_likes; Type: TABLE; Schema: public; Owner: qcjurrgz
--

CREATE TABLE public.locations_location_likes (
    id bigint NOT NULL,
    location_id bigint NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.locations_location_likes OWNER TO qcjurrgz;

--
-- Name: locations_location_likes_id_seq; Type: SEQUENCE; Schema: public; Owner: qcjurrgz
--

CREATE SEQUENCE public.locations_location_likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_location_likes_id_seq OWNER TO qcjurrgz;

--
-- Name: locations_location_likes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qcjurrgz
--

ALTER SEQUENCE public.locations_location_likes_id_seq OWNED BY public.locations_location_likes.id;


--
-- Name: account_profile id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.account_profile ALTER COLUMN id SET DEFAULT nextval('public.account_profile_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: easy_thumbnails_source id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_source ALTER COLUMN id SET DEFAULT nextval('public.easy_thumbnails_source_id_seq'::regclass);


--
-- Name: easy_thumbnails_thumbnail id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnail ALTER COLUMN id SET DEFAULT nextval('public.easy_thumbnails_thumbnail_id_seq'::regclass);


--
-- Name: easy_thumbnails_thumbnaildimensions id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnaildimensions ALTER COLUMN id SET DEFAULT nextval('public.easy_thumbnails_thumbnaildimensions_id_seq'::regclass);


--
-- Name: locations_comment id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_comment ALTER COLUMN id SET DEFAULT nextval('public.locations_comment_id_seq'::regclass);


--
-- Name: locations_location id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location ALTER COLUMN id SET DEFAULT nextval('public.locations_location_id_seq'::regclass);


--
-- Name: locations_location_likes id; Type: DEFAULT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location_likes ALTER COLUMN id SET DEFAULT nextval('public.locations_location_likes_id_seq'::regclass);


--
-- Data for Name: account_profile; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.account_profile (id, date_of_birth, photo, user_id) FROM stdin;
1	\N	media/account/eva-ourspot_zbqaxy	2
2	\N	media/account/PXL_20230526_075856108.MP_1_tkuazb	1
4	\N	media/account/bpitt_pgogbn	4
3	\N	media/account/travelguy_kmesmk	3
5	\N	media/account/guy-image2_ib6f0i	5
6	\N	media/account/self-confidence-women-smile_tum2e2	6
11	\N	media/account/marcus-blair_u9empa	11
12	\N	media/account/bobbi-brown_mdzvna	12
13	1979-11-02	media/account/matilda-callaghan_wwi5vk	13
15	1998-08-11	media/account/IMG_4194_fxil7i	15
16	\N		16
17	\N		17
18	\N	media/account/d751c-adult-afro-blur-1181519_pdrpnv	18
7	\N	media/account/ronald_q2ej2q	7
10	\N	media/account/sues_cwbvyh	10
20	\N	media/account/1000006361_y5dup4	20
14	\N	media/account/mollywear_shdghw	14
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add site	7	add_site
26	Can change site	7	change_site
27	Can delete site	7	delete_site
28	Can view site	7	view_site
29	Can add location	8	add_location
30	Can change location	8	change_location
31	Can delete location	8	delete_location
32	Can view location	8	view_location
33	Can add like	9	add_like
34	Can change like	9	change_like
35	Can delete like	9	delete_like
36	Can view like	9	view_like
37	Can add profile	10	add_profile
38	Can change profile	10	change_profile
39	Can delete profile	10	delete_profile
40	Can view profile	10	view_profile
41	Can add contact	11	add_contact
42	Can change contact	11	change_contact
43	Can delete contact	11	delete_contact
44	Can view contact	11	view_contact
45	Can add source	12	add_source
46	Can change source	12	change_source
47	Can delete source	12	delete_source
48	Can view source	12	view_source
49	Can add thumbnail	13	add_thumbnail
50	Can change thumbnail	13	change_thumbnail
51	Can delete thumbnail	13	delete_thumbnail
52	Can view thumbnail	13	view_thumbnail
53	Can add thumbnail dimensions	14	add_thumbnaildimensions
54	Can change thumbnail dimensions	14	change_thumbnaildimensions
55	Can delete thumbnail dimensions	14	delete_thumbnaildimensions
56	Can view thumbnail dimensions	14	view_thumbnaildimensions
57	Can add tag	15	add_tag
58	Can change tag	15	change_tag
59	Can delete tag	15	delete_tag
60	Can view tag	15	view_tag
61	Can add comment	16	add_comment
62	Can change comment	16	change_comment
63	Can delete comment	16	delete_comment
64	Can view comment	16	view_comment
65	Can add followers count	17	add_followerscount
66	Can change followers count	17	change_followerscount
67	Can delete followers count	17	delete_followerscount
68	Can view followers count	17	view_followerscount
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
14	pbkdf2_sha256$260000$M5AWjLSizuf0euZlOCqp4U$4jEgiDpUrbe2pEpHxkhNVKM5dZnCAV30zopl+zHlUBg=	2023-11-11 17:37:48.479119+00	f	Mymumsdabest	Molly	Wear	emersedcrown@outlook.com	f	t	2023-11-11 17:37:32.526094+00
10	pbkdf2_sha256$260000$Qi6l2TlbVdd5U4l1VKjPa6$QV8g10T59wjTM/tFFs+OfVXXc8d83koEFJ4cttt8mnQ=	2023-11-17 09:12:02.678318+00	f	a-truss	Angela	Truss	atruss@madeupmyemail.com	f	t	2023-11-02 12:13:25.566347+00
12	pbkdf2_sha256$260000$uKD1SqLF8GA7yfDcSnx4U0$h2gGCN12//9sOk9vfh1DLO2wwv6gkX7BFTGlhgHn73w=	2023-11-02 18:13:51.85913+00	f	bobbrown	Bobbi	Brown	bbrown@madeup.com	f	t	2023-11-02 14:01:53+00
4	pbkdf2_sha256$260000$xCk022Df5GQHBRSZcdn7A5$QpPnMJgdHqWOmKWzaTmJq0OxGTQiqM5M34xLnlbTx6A=	2023-11-01 14:17:23.437635+00	f	bpitt	Bradley	Pitt	bradley@madeup.com	f	t	2023-10-24 16:39:55.424567+00
13	pbkdf2_sha256$260000$pJtDcvN9nEoYyPnvYIgz6K$bhYrg80majhB47n/affEkZnc3IR4MRTalj4GtkF4DSo=	2023-11-02 18:26:40.539248+00	f	tillyc	Matilda	Callaghan	mc@madeup.com	f	t	2023-11-02 14:04:55+00
11	pbkdf2_sha256$260000$7qjGmNWqu36NLWwlM5O68k$Jvv3ADlFSxP3xBhqatKNou26ZE8LP4fFnN5bt77l4Fk=	2023-11-10 11:20:52.623808+00	f	blairites	Marcus	Blair	mblair@madeup.com	f	t	2023-11-02 12:21:43.613313+00
6	pbkdf2_sha256$260000$4pAvfsJPWHI2m12roXe8zt$aOcJwDIR4nXyuvtkVsmxF7WBI8qdaE24+EBpny6lzIQ=	2023-11-02 18:29:28.793918+00	f	HAURESKI	Susan	May	shaureski@hotmail.com	f	t	2023-10-28 11:33:19+00
20	pbkdf2_sha256$260000$oT10YFs9t57y67BCSfgUh4$7EI9uRW2GgDC5OS3hg2DcnKEQDlkjy0zzEp8+yniMjQ=	2023-11-17 09:31:10.917379+00	f	travelgirl87	Amanda	Thatcher	athat@noemail.com	f	t	2023-11-17 09:18:34.034891+00
3	pbkdf2_sha256$260000$mEukJJruxcXfsJZLGn5XWw$WzjX7j90/XJ0K1B5fiWlua2gwM1BP3v+kkBvqKrUdMw=	2023-10-31 14:52:40+00	f	travelguy	Mark	Johnson	travelguy@madeupemail.com	f	t	2023-10-24 16:36:09+00
15	pbkdf2_sha256$260000$8O0rWkEtiQ66kovANPWvPO$CYqMGsQC50hc+ganwHJL6NX8Hi0zydFDjIJYw0ev8x0=	2023-11-12 09:23:25.234961+00	f	mikeyjwill98	James	Smith	james_smith@gmail.com	f	t	2023-11-11 17:46:56.347418+00
7	pbkdf2_sha256$260000$lyjqcGplofYeRjX2gG6sAc$RFQdylvf991zdkG6i2FQlrZf+XceFcaGZmCwonCZXTA=	2023-10-30 23:42:46+00	f	rock	Ronald	Churchill	rock1978@madeupemail.com	f	t	2023-10-30 23:42:29+00
5	pbkdf2_sha256$260000$WNyIZ2XoBXwe3YZ3uuV1tw$DQT5WzbMx29ZllhsNxdZEJvU3ueWS7Si7cRDep1ZNdk=	2023-10-29 09:16:51+00	f	awilson	Antonio	Wilson	awilson@madeup.com	f	t	2023-10-28 11:30:02+00
16	pbkdf2_sha256$260000$4M5hTg9PrAFc7680pJwCvA$eSGcpGx4Aa/Z+Rr4iLIHrSo/0G5EZW6CdS2xhVPUjis=	2023-11-12 16:45:46.574359+00	f	Thefavouritechild	Ryan	Williamson	ryanwilliamson206@gmail.com	f	t	2023-11-11 19:02:37.331565+00
17	pbkdf2_sha256$260000$Q39WLfu3qhxdAXQw8STb2m$m4iG7saVmZt7PStuavLGtAi93mUFIASGLXZ3ZGy32jM=	2023-11-14 14:30:52.089124+00	f	DaisyM	Daisy	McGirr	mcgirr.daisy@gmail.com	f	t	2023-11-14 14:30:28.102681+00
18	pbkdf2_sha256$260000$60C9VVgf0RIXO0RFHQhbwS$8YIPqr9W9m3V+mc5rfWWnX+3w3HHD3IFuwpjw4zg3mU=	2023-11-14 15:38:40.605506+00	f	sallysmith	Sally	Smith	sally@madeupmy.com	f	t	2023-11-14 15:38:12.58172+00
2	pbkdf2_sha256$720000$VtzLSWMuJuvZj6A6tNgUwA$Kq6o2pqGSswYdTWUTgGaze9VTt7qpp2UKGS1aw4bssE=	2024-04-05 15:32:09.810304+00	t	ourspot	Eva	Mandy	evamandy2012@gmail.com	t	t	2023-10-23 12:39:52+00
1	pbkdf2_sha256$720000$Klk462L2YNpRLOdpMFVApm$UvA6tsoiHLDsyVkugZ8lPvQjolgU7KUqaqHLqv75vJY=	2024-04-05 15:34:51.732624+00	t	manager	Diane	Corriette	dcorriette@gmail.com	t	t	2023-10-23 12:38:55+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-10-23 12:47:44.102662+00	1	manager	2	[{"changed": {"fields": ["First name", "Last name"]}}]	4	1
2	2023-10-23 12:48:10.503416+00	2	ourspot	2	[{"changed": {"fields": ["First name", "Last name"]}}]	4	1
3	2023-10-23 12:51:13.931081+00	1	Profile of ourspot	1	[{"added": {}}]	10	1
4	2023-10-23 13:00:52.607914+00	1	Relaxing Walk	1	[{"added": {}}]	8	1
5	2023-10-23 13:03:20.79393+00	2	Profile of manager	1	[{"added": {}}]	10	1
6	2023-10-23 13:05:50.275101+00	2	Our Spot Social Network	1	[{"added": {}}]	8	1
7	2023-10-23 18:55:14.578103+00	3	Comment object (3)	3		16	1
8	2023-10-23 18:55:14.699916+00	2	Comment object (2)	3		16	1
9	2023-10-23 18:55:14.821818+00	1	Comment object (1)	3		16	1
10	2023-10-24 17:27:06.689793+00	4	Profile of bpitt	2	[{"changed": {"fields": ["Photo"]}}]	10	1
11	2023-10-24 17:31:55.036609+00	3	Profile of travelguy	2	[{"changed": {"fields": ["Photo"]}}]	10	1
12	2023-10-28 15:05:36.037542+00	9	Comment object (9)	1	[{"added": {}}]	16	1
13	2023-10-28 17:35:53.87601+00	9	Comment object (9)	2	[{"changed": {"fields": ["Text"]}}]	16	1
14	2023-11-01 13:02:37.032928+00	9	Harry_P	3		4	1
15	2023-11-01 13:13:50.915443+00	6	HAURESKI	2	[{"changed": {"fields": ["Email address"]}}]	4	1
16	2023-11-01 13:14:14.31145+00	3	travelguy	2	[{"changed": {"fields": ["Email address"]}}]	4	1
17	2023-11-01 13:15:13.233385+00	7	rock	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	4	1
18	2023-11-01 13:16:29.398548+00	8	Michael	3		4	1
19	2023-11-01 13:18:40.844531+00	6	HAURESKI	2	[{"changed": {"fields": ["First name", "Last name"]}}]	4	1
20	2023-11-01 18:32:22.134238+00	2	bpitt - Lovely walk all day	3		16	1
21	2023-11-02 11:58:31.226313+00	3	travelguy	2	[{"changed": {"fields": ["Last name"]}}]	4	1
22	2023-11-02 11:58:55.058035+00	6	HAURESKI	2	[{"changed": {"fields": ["Last name"]}}]	4	1
23	2023-11-02 11:59:15.736462+00	7	rock	2	[{"changed": {"fields": ["Last name"]}}]	4	1
24	2023-11-02 12:01:33.649078+00	5	awilson	2	[{"changed": {"fields": ["Username", "Last name", "Email address"]}}]	4	1
25	2023-11-02 14:01:53.188374+00	12	bobbrown	1	[{"added": {}}]	4	1
26	2023-11-02 14:02:22.540715+00	12	bobbrown	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	4	1
27	2023-11-02 14:03:45.121726+00	12	bobbrown	1	[{"added": {}}]	10	1
28	2023-11-02 14:04:55.500129+00	13	tillyc	1	[{"added": {}}]	4	1
29	2023-11-02 14:05:25.256447+00	13	tillyc	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	4	1
30	2023-11-02 14:06:45.632906+00	13	tillyc	1	[{"added": {}}]	10	1
31	2023-11-05 12:05:01.499796+00	26	Cold and foggy Worcestershire	1	[{"added": {}}]	8	1
32	2023-11-05 12:07:38.32863+00	27	Wyre Forest	1	[{"added": {}}]	8	1
33	2023-11-05 12:22:02.503316+00	7	ourspot - Absolutely beautiful. Love it	1	[{"added": {}}]	16	1
34	2023-11-05 12:30:08.335617+00	9	bobbrown - One of our favourite spots to visit when	1	[{"added": {}}]	16	1
35	2023-11-11 15:31:50.203022+00	1	manager	2	[{"changed": {"fields": ["password"]}}]	4	2
36	2023-11-12 10:56:11.575627+00	36	Dubai Home	1	[{"added": {}}]	8	1
37	2023-11-12 10:58:18.853856+00	37	New York New York	1	[{"added": {}}]	8	1
38	2023-11-12 10:59:29.786925+00	32	London views	2	[{"changed": {"fields": ["Description", "Likes"]}}]	8	1
39	2023-11-12 11:00:08.557786+00	14	Wightwick Manor Staffordshire	2	[{"changed": {"fields": ["Description"]}}]	8	1
40	2023-11-12 11:01:48.047861+00	2	Our Spot Photo Sharing Platform	2	[{"changed": {"fields": ["Title", "Description"]}}]	8	1
41	2023-11-12 11:03:53.872153+00	31	Walking the forests of Latvia	2	[{"changed": {"fields": ["Likes"]}}]	8	1
42	2023-11-12 11:04:15.976723+00	32	London views	2	[{"changed": {"fields": ["Likes"]}}]	8	1
43	2023-11-12 11:05:15.827784+00	2	Our Spot Photo Sharing Platform	2	[{"changed": {"fields": ["Likes"]}}]	8	1
44	2023-11-14 15:42:23.864905+00	46	Is this working	3		8	1
45	2023-11-14 15:42:23.889701+00	45	What happens	3		8	1
46	2023-11-14 15:44:01.82536+00	18	sallysmith	2	[{"changed": {"fields": ["Photo"]}}]	10	1
47	2023-11-14 15:46:17.220244+00	7	rock	2	[{"changed": {"fields": ["Photo"]}}]	10	1
48	2023-11-17 09:42:36.877138+00	14	Mymumsdabest	2	[{"changed": {"fields": ["Photo"]}}]	10	1
49	2024-04-05 14:46:05.465733+00	27	Abby	3		4	2
50	2024-04-05 14:46:05.475916+00	23	ABC	3		4	2
51	2024-04-05 14:46:05.479861+00	22	ahb	3		4	2
52	2024-04-05 14:46:05.482967+00	29	Ahmed	3		4	2
53	2024-04-05 14:46:05.486064+00	19	Anwar	3		4	2
54	2024-04-05 14:46:52.952836+00	28	Michael	3		4	2
55	2024-04-05 14:48:39.697068+00	26	eval	3		4	2
56	2024-04-05 14:49:06.985781+00	24	demouser	3		4	2
57	2024-04-05 14:49:06.997263+00	21	ferchapombo	3		4	2
58	2024-04-05 14:49:07.000761+00	25	testUser123	3		4	2
59	2024-04-05 15:34:19.202961+00	1	manager	2	[{"changed": {"fields": ["password"]}}]	4	2
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	sites	site
8	locations	location
9	locations	like
10	account	profile
11	account	contact
12	easy_thumbnails	source
13	easy_thumbnails	thumbnail
14	easy_thumbnails	thumbnaildimensions
15	locations	tag
16	locations	comment
17	account	followerscount
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-10-23 11:22:30.169422+00
2	auth	0001_initial	2023-10-23 11:22:30.904459+00
3	account	0001_initial	2023-10-23 11:22:31.055978+00
4	account	0002_auto_20231016_2044	2023-10-23 11:22:31.369355+00
5	account	0003_auto_20231017_1017	2023-10-23 11:22:31.463236+00
6	account	0004_alter_profile_photo	2023-10-23 11:22:31.570566+00
7	account	0005_alter_profile_photo	2023-10-23 11:22:31.702205+00
8	admin	0001_initial	2023-10-23 11:22:31.936633+00
9	admin	0002_logentry_remove_auto_add	2023-10-23 11:22:32.004832+00
10	admin	0003_logentry_add_action_flag_choices	2023-10-23 11:22:32.088893+00
11	contenttypes	0002_remove_content_type_name	2023-10-23 11:22:32.221475+00
12	auth	0002_alter_permission_name_max_length	2023-10-23 11:22:32.326213+00
13	auth	0003_alter_user_email_max_length	2023-10-23 11:22:32.4303+00
14	auth	0004_alter_user_username_opts	2023-10-23 11:22:32.515373+00
15	auth	0005_alter_user_last_login_null	2023-10-23 11:22:32.618891+00
16	auth	0006_require_contenttypes_0002	2023-10-23 11:22:32.697686+00
17	auth	0007_alter_validators_add_error_messages	2023-10-23 11:22:32.786577+00
18	auth	0008_alter_user_username_max_length	2023-10-23 11:22:32.902381+00
19	auth	0009_alter_user_last_name_max_length	2023-10-23 11:22:33.007398+00
20	auth	0010_alter_group_name_max_length	2023-10-23 11:22:33.120473+00
21	auth	0011_update_proxy_permissions	2023-10-23 11:22:33.206565+00
22	auth	0012_alter_user_first_name_max_length	2023-10-23 11:22:33.314728+00
23	easy_thumbnails	0001_initial	2023-10-23 11:22:33.763435+00
24	easy_thumbnails	0002_thumbnaildimensions	2023-10-23 11:22:33.900001+00
25	locations	0001_initial	2023-10-23 11:22:34.071557+00
26	locations	0002_likelocation	2023-10-23 11:22:34.167019+00
27	locations	0003_auto_20231018_2014	2023-10-23 11:22:34.462813+00
28	locations	0004_auto_20231018_2031	2023-10-23 11:22:34.739534+00
29	locations	0005_auto_20231019_1125	2023-10-23 11:22:34.916769+00
30	locations	0006_alter_location_slug	2023-10-23 11:22:35.003805+00
31	sessions	0001_initial	2023-10-23 11:22:35.19313+00
32	sites	0001_initial	2023-10-23 11:22:35.280136+00
33	sites	0002_alter_domain_unique	2023-10-23 11:22:35.413782+00
34	auth	0013_user_following	2023-10-23 11:22:45.832552+00
35	locations	0007_comment_tag	2023-10-23 11:27:15.825442+00
36	account	0002_alter_profile_photo	2023-10-23 13:27:30.577816+00
37	locations	0002_comment_photo	2023-10-23 13:27:31.312067+00
38	account	0003_alter_profile_photo	2023-10-24 17:21:10.58754+00
39	locations	0003_alter_comment_photo	2023-10-25 12:09:30.385424+00
40	locations	0004_alter_comment_photo	2023-10-28 11:40:59.225517+00
41	locations	0005_alter_comment_photo	2023-10-28 16:51:10.883353+00
42	locations	0006_remove_comment_photo	2023-10-28 17:22:47.475785+00
43	locations	0006_auto_20231028_2054	2023-10-28 20:59:19.787313+00
44	auth	0014_remove_user_following	2023-10-28 23:03:31.897199+00
45	account	0004_auto_20231028_2303	2023-10-28 23:03:32.261262+00
46	account	0005_auto_20231029_1330	2023-10-29 13:31:02.648917+00
47	account	0006_auto_20231031_1011	2023-10-31 10:12:04.020383+00
48	locations	0007_comment	2023-11-01 17:26:56.039823+00
49	account	0007_remove_profile_following	2023-11-02 14:07:55.981607+00
50	locations	0008_alter_location_image	2023-11-09 16:06:22.057485+00
51	locations	0009_alter_like_location	2023-11-09 17:43:09.1021+00
52	locations	0010_auto_20231109_1841	2023-11-09 18:41:44.690051+00
53	locations	0011_auto_20231109_1910	2023-11-09 19:11:02.301805+00
54	locations	0009_auto_20231110_1117	2023-11-10 11:18:07.174092+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
nkhejze28u1awdtpnoac7x36yiu57q9m	.eJxVjLEOwjAMRP8lM4pSqw41IzvfEMWxQwoolZp2Qvw7rdQBttO9d_c2Ia5LCWvTOYxiLgZ6c_otOaan1p3II9b7ZNNUl3lkuyv2oM3eJtHX9XD_DkpsZVsz5EQugUPwLqGwqBJloDNE8kKZtzQAonIv6Mh79owIrovdgKDm8wUNYzez:1r7zdC:YsyiV3tna769SA6LNbBqkQKiz2VRM7oQArvrnT0l-Ts	2023-12-12 15:04:10.099185+00
w008u5glm5m41p15cp06asho80n0axwl	.eJxVjEEOwiAQRe_C2pAyyAAu3XsGMsBUqgaS0q6Md7dNutDtf-_9twi0LiWsnecwZXERIE6_W6T05LqD_KB6bzK1usxTlLsiD9rlrWV-XQ_376BQL1s9eE_OsANmoxJqM4wJbWYNaFROgOCT8RSdBWCLipg1jsraTcOzY_H5AtQvN5E:1quwWd:SRtOV7c_ay9Y1KNB0naM51BoRbDGjSS2fpVIWouhNsQ	2023-11-06 15:07:27.476303+00
ffv1b8xqmbpkppelezu6q9jyeje3obog	.eJxVjMsOwiAQRf-FtSHADI-6dO83kGGgUjU0Ke3K-O_apAvd3nPOfYlI21rj1ssSpyzOQovT75aIH6XtIN-p3WbJc1uXKcldkQft8jrn8rwc7t9BpV6_tXNJ6xBKGA0ysrLowaKBAVxWJRjSwKCY2Rtbkh40crCZMuLoFVAQ7w-49DcI:1rD0f3:eDXeYX0UL_IMIW8sgoO5IeyJMzWuvRiLM-2KP8VjCYM	2023-12-26 11:10:49.085383+00
t1uhkyow2re332tylk1twsygapu38v5c	.eJxVjEEOwiAQRe_C2pAyyAAu3XsGMsBUqgaS0q6Md7dNutDtf-_9twi0LiWsnecwZXERIE6_W6T05LqD_KB6bzK1usxTlLsiD9rlrWV-XQ_376BQL1s9eE_OsANmoxJqM4wJbWYNaFROgOCT8RSdBWCLipg1jsraTcOzY_H5AtQvN5E:1quxJt:BeDNf4pKeJc4SBSLP-yk_uRQ6uwvaVb4U9TQvWFfZxk	2023-11-06 15:58:21.554541+00
lkvto9qt97pwdx99v2d1ud8xb8np34y9	.eJxVjDsOwjAQBe_iGlne9S-hpOcM1q69JgEUS_lUiLtDpBTQvpl5L5VoW4e0LTKnsaizQnX63ZjyQ6YdlDtNt6Zzm9Z5ZL0r-qCLvrYiz8vh_h0MtAzfOsTAHMg73wFW8tEagWrRRKwW2HlBzn0lZMksBpytHrsc-oAeoAf1_gDQ6zcx:1rMBra:nQcISe4DYxL-J3pJaRozsQ3XdkJxHe0IvTx-51snF-g	2024-01-20 18:57:42.000076+00
a4g7as9jj22f60mzaior1gdmh19eur3y	.eJxVjMsOwiAQRf-FtSE8pjxcuvcbyMCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CTOzMlGGn3zFieuS2E7pju3WeeluXOfJd4Qcd_NopPy-H-3dQcdRvrScQ0pH03nmPFoUFQIwmSwlktUhFu6ysg5IUZG1RYZRlcqRQYzGFvT_meTfY:1rMdgQ:UmsCDloEa31nXZyZocOUwLkYREhZloeB3bOBANf-e3Q	2024-01-22 00:40:02.728264+00
ni6u6fej6vpfre565rn37exp9hyfvpoz	.eJxVjEEOwiAQRe_C2hAGaCku3XsGMsNMpWpoUtqV8e7apAvd_vfef6mE21rS1mRJE6uzAnX63QjzQ-oO-I71Nus813WZSO-KPmjT15nleTncv4OCrXzrvgeSgGiZIIuPwtkg4EA2GB8zsbfQmezIQBzJRWes9dINTsbg2Il6fwD4-TgT:1r0NuA:7khdYu0-QMUSnC3LhZf7-1-oPfqVAzFGPgTQaZ2rZTg	2023-11-21 15:22:14.146764+00
vndbgnj736hl6ehsg2bkscn4dv83vdaq	.eJxVjMsOwiAQRf-FtSHDlEd16b7fQAYGpGogKe3K-O_apAvd3nPOfQlP21r81tPiZxYXgaM4_Y6B4iPVnfCd6q3J2Oq6zEHuijxol1Pj9Lwe7t9BoV6-tbI2IQImIHZoo86A-pxtGEbj2AIjxAQx2GFwMbNxRrPRZIx2SoUA4v0B77Q3Yw:1rWNqt:Clgojmjfke-Rxv-faQTtstoCkvaV3F7LYO5yJG67_vQ	2024-02-17 21:47:07.948767+00
940sxwbigywmnu96g2sm0nl3wck1rxof	.eJxVjDsOwjAQBe_iGlmO4_U6lPQ5Q7T2rnEAOVI-FeLuJFIKaN_MvLcaaFvLsC0yDyOrq7KduvyOkdJT6kH4QfU-6TTVdR6jPhR90kX3E8vrdrp_B4WWstfOZhOQI4B1GRBEpEP2bJjIEmYMzko0rWnQg0vSAoB3bYiNwd016vMFBNg3sA:1rYTBA:hoqUnh5i41lkgPGp2IeVYdiREt8fIpRVOm29iJ7OPUQ	2024-02-23 15:52:40.663985+00
xccenkbor5cprz9rf0tm32dursklf3nh	.eJxVjEEOwiAQRe_C2hAGaCku3XsGMsNMpWpoUtqV8e7apAvd_vfef6mE21rS1mRJE6uzAnX63QjzQ-oO-I71Nus813WZSO-KPmjT15nleTncv4OCrXzrvgeSgGiZIIuPwtkg4EA2GB8zsbfQmezIQBzJRWes9dINTsbg2Il6fwD4-TgT:1qvMSZ:1y343k5Fc4pr3ACuC8_xucUBvVBGd0fVPb7fKQg30ho	2023-11-07 18:48:59.019041+00
4sik2rdm9la25tf5m6cxra6sfyjjdjm8	.eJxVjEEOwiAQRe_C2pBpC8K4dO8ZyAyDUjWQlHZlvLuSdKHb_977LxVoW3PYWlrCLOqkBnX43ZjiI5UO5E7lVnWsZV1m1l3RO236UiU9z7v7d5Cp5V6zh4jWCI4ujRM4g-I8Q4TIYDlJMg6vLOgmMGKPRPK1LPrBCSNF9f4A4z84CA:1qvdWW:BItaL1KtXjHRuHrKzLvEga9tGQj1r4hJ4zcNFC2AhBM	2023-11-08 13:02:12.487164+00
ztmkkpkjqhhgjm67kvx0gy9r0lv7xsut	.eJxVjMsOwiAQRf-FtSG8hMGle7-BDDBI1UBS2pXx322TLnR7zzn3zQKuSw3roDlMmV2YNOz0O0ZMT2o7yQ9s985Tb8s8Rb4r_KCD33qm1_Vw_w4qjrrVCF4Z8sqZBIpEJMCzS6SNJy2clhaysMWAB1e0icl7aa11cZMLCnDs8wXuvjdE:1r1rvY:2dIBBZa7Mb1Cvg2qhRMaJB6ix-bqlx90rXU3LfneQCo	2023-11-25 17:37:48.484065+00
z6ry8urlfjtk8bhyhvri72i6v642oe3c	.eJxVi0sOwiAQQO_C2jQM0FLcaeI5yMwwTYlKkxZWxrvbJi50-z4vFbHVObZN1piTOitQp19GyHcph0DmpZXaHU5KzYw1L6W7PTE_Lju7fsu_fcZt3t9hABKPaBIBiwuSWCPgSMZrF5iSM9BrtqQhTGSD1cY46Ucrk7fJinp_AKiJN7w:1qwiFY:EyBTQ5K6LNwmYS_nagjp2lNZSySnIn0QcYj29X5_wyY	2023-11-11 12:17:08.376161+00
ww3vmxc8p4de695g662kmpp0tj2y9oz5	.eJxVjEEOwiAQRe_C2hAGaCku3XsGMsNMpWpoUtqV8e7apAvd_vfef6mE21rS1mRJE6uzAnX63QjzQ-oO-I71Nus813WZSO-KPmjT15nleTncv4OCrXzrvgeSgGiZIIuPwtkg4EA2GB8zsbfQmezIQBzJRWes9dINTsbg2Il6fwD4-TgT:1qwkrg:KTVH9ToulXQfbrkkFTztPVH5IAMkIGc1v0r9RoQZRZs	2023-11-11 15:04:40.596194+00
9catju62aqcw4s8wjxau15s1sp7h1k3u	.eJxVjEEOwiAQRe_C2pAyyAAu3XsGMsBUqgaS0q6Md7dNutDtf-_9twi0LiWsnecwZXERIE6_W6T05LqD_KB6bzK1usxTlLsiD9rlrWV-XQ_376BQL1s9eE_OsANmoxJqM4wJbWYNaFROgOCT8RSdBWCLipg1jsraTcOzY_H5AtQvN5E:1r19R9:1Mr8f0hDqNnsrmsqdGYk-USJCDS739WBjxeobu56Ccg	2023-11-23 18:07:27.149472+00
fulk31bzi33dh1a6bhts1k3xx5mlcxet	.eJxVjEEOwiAQRe_C2hAGaCku3XsGMsNMpWpoUtqV8e7apAvd_vfef6mE21rS1mRJE6uzAnX63QjzQ-oO-I71Nus813WZSO-KPmjT15nleTncv4OCrXzrvgeSgGiZIIuPwtkg4EA2GB8zsbfQmezIQBzJRWes9dINTsbg2Il6fwD4-TgT:1qwq8v:qJ_s5fYeGdTtyeei78upO2antePQFJ4o8YhZQ1FqZIQ	2023-11-11 20:42:49.175694+00
4mlb2v6tehpmlln9nww41vcbu9g2m0yf	.eJxVjDsOwjAQBe_iGlms_6akzxmstb2LAyiR4qRC3B0ipYD2zcx7iYTb2tLWaUljFRcBVpx-x4zlQdNO6h2n2yzLPK3LmOWuyIN2OcyVntfD_Tto2Nu3RsrWOgXeckXNzigbWTsfIwNDjTEoKNrHcs5UA9uiAwMaNIFCIQ3i_QEFlDgl:1r26gf:1ABl5Pe67iVJPM2OWJK-PzJ47ruzCcKkLzfAtZa2Hzs	2023-11-26 09:23:25.246568+00
68zztodg4lzwpg56gjf80yd1xgwefy96	.eJxVjEEOwiAQRe_C2pASGCku3XsGMsNMpWogKe2q8e5K0oVu_3vv7yritua4NVnizOqivDr9boTpKaUDfmC5V51qWZeZdFf0QZu-VZbX9XD_DjK23Gti5wJaa0IAGK0DJi-DmciOIP5MwbEHdIYTBUErafJfAJASDi6Ien8A5Kc4TQ:1qxbuA:QJlB91_BadNLDKuOYAChNhfgArngw2jhgdgwTrHNDSc	2023-11-13 23:42:46.091131+00
79fy9wnbe1xkt3t8q32b9wzgod6yj8se	.eJxVjEEOwiAQRe_C2hBgKCMu3fcMzdAZpGpoUtqV8e7apAvd_vfef6mBtrUMW5NlmFhdlA3q9DsmGh9Sd8J3qrdZj3NdlynpXdEHbbqfWZ7Xw_07KNTKtzaYATAlQQB3BhcpsU-E2SLnEI1hDxmx65zkkDtvURjZWRIO1kBU7w8C1jfe:1r2Dak:p4k_ft6xyIqSSGWu_N7Nv6_1thHRv17MnjgSlnYRaD8	2023-11-26 16:45:46.578323+00
90798wsrk1jaxpempg33poy0q8iwfhe6	.eJxVjEEOgjAQRe_StWmkFGFcuucM5M9MK6hpEwor492FhIVu_3vvv82AdRmHtYR5mNRcTdWa0-_IkGdIO9EH0j1byWmZJ7a7Yg9abJ81vG6H-3cwooxb3ZAXX8WaEJnPHEQZVHl06oUcLh2raAfhCIDIBd9sBHCBoqvRms8XS6U6Dg:1r2uRI:9mM51oDUNYyHbdCKoh956h820m7zKQ9Dpb42O_-cZho	2023-11-28 14:30:52.093454+00
vhp0iiwwu60jww9b5yxgiz9mxi4u1c88	.eJxVjDsOwjAQBe_iGln-4Q8lfc5g7dprHEC2FCcV4u4QKQW0b2bei0XY1hq3QUucM7swz06_G0J6UNtBvkO7dZ56W5cZ-a7wgw4-9UzP6-H-HVQY9VuXYL1QwhpIQZ0lYcoUrMo2FaOt1IpAosGE6KT3WIQh7YoXzjpZECR7fwDmGTgC:1qxw4x:TyQKYiQQA_LQSuaPdyII2qWH2GzzzGI2hRsR79rt4lU	2023-11-14 21:15:15.036126+00
9ssqtgca5c8a1ugv4oxdvpnh9493e18u	.eJxVjDsOwyAQBe9CHSEWYz4p0_sMaGEhOIlAMnYV5e4RkoukfTPz3szjsRd_9LT5ldiVOXb53QLGZ6oD0APrvfHY6r6tgQ-Fn7TzpVF63U7376BgL6N2GGzKNk9CAGqtKBtQoEkKCFJklTABWZVBGCdn7ZSybs6Tm0w0miz7fAHigjcs:1qy7RU:qEkDUXxZApFUaK79HIq84MKUulvJ0Kj39Wf0EjNIv3M	2023-11-15 09:23:16.448701+00
rvhrlsrdcgxpu64w7980u82tpwdshn1o	.eJxVjMEOwiAQRP-FsyGwgFCP3v0GsuyCVA1NSnsy_rtt0oMe5jLvzbxFxHWpce15jiOLi9BKnH7LhPTMbSf8wHafJE1tmcckd0UetMvbxPl1Pdy_g4q9buuUjcucwAANiUpWdLZOGwD21m4xTM6roK2xAQmK884PGCgFXxgBxecLDoY4MA:1r3utO:HMhvLPCUaValOaRZqTd4Ey4b32EALI8tbJQBPkfD_Q8	2023-12-01 09:12:02.687249+00
zocmqgiyivvpb3zsvgs7tl235ocmuet6	.eJxVjMsOwiAQRf-FtSGFzvBw6d5vaAYGpGogKe3K-O_apAvd3nPOfYmJtrVMW0_LNLM4C63F6XcMFB-p7oTvVG9NxlbXZQ5yV-RBu7w2Ts_L4f4dFOrlW7tgEZ23BqLlEcEGJvAGFBoLPGBUhpwakqE0AprMhANpHzOjjhlIvD_iLzex:1r5Z9O:cgkgBWIMiCDuaMAaG4cNKyVnC20va-qzPS8LtGiqwPc	2023-12-05 22:23:22.29098+00
yx41meexp9ci1a8fpr4syme7k9f0h7rf	.eJxVjMsOwiAQRf-FtSG8Cy7d-w1kmAGpGkhKuzL-uzbpQrf3nHNfLMK21riNvMSZ2JkpyU6_YwJ85LYTukO7dY69rcuc-K7wgw5-7ZSfl8P9O6gw6rcGAvSTk4JMQQhSBQzaiGK1AocZXRK6BOOE9iprmyRZ65OasGQiKI69PxGKOI8:1r6vhG:fqpFSh5U_H0m-dBS4o86jJ3QkDeaqwDXygPEqgRlOMs	2023-12-09 16:39:58.819134+00
c6yk8iwajqitk18f8g8aiz28dduyxsc4	.eJxVjDsOwjAQBe_iGlkbHMeYkp4zWPszDiBHipMKcXeIlALaNzPvZRKuS0lr0zmNYs6mM4ffjZAfWjcgd6y3yfJUl3kkuyl2p81eJ9HnZXf_Dgq28q2ZchYvIHIEH8kTeAYNOQSHOmDPfRjAKfsYOooYUaNTpXwCcQLszPsDD5847w:1rslad:O0WRUvQa0PZKM3iqio6AjfI7-dIT686G6a_0c5136_Y	2024-04-19 15:34:51.736902+00
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: easy_thumbnails_source; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.easy_thumbnails_source (id, storage_hash, name, modified) FROM stdin;
\.


--
-- Data for Name: easy_thumbnails_thumbnail; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.easy_thumbnails_thumbnail (id, storage_hash, name, modified, source_id) FROM stdin;
\.


--
-- Data for Name: easy_thumbnails_thumbnaildimensions; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.easy_thumbnails_thumbnaildimensions (id, thumbnail_id, width, height) FROM stdin;
\.


--
-- Data for Name: locations_comment; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.locations_comment (id, text, created_at, updated_at, location_id, user_id) FROM stdin;
3	Looks like a lovely place to walk during the day	2023-11-01 18:08:49.974984+00	2023-11-01 18:09:05.224243+00	12	4
4	I have family that live in this location but I have never visited. Will give it a go next time I am in Luton	2023-11-01 18:10:34.290427+00	2023-11-01 18:10:34.290459+00	12	1
5	I used to love spending time with my mum	2023-11-02 16:09:05.353812+00	2023-11-02 16:09:05.353832+00	21	12
7	Absolutely beautiful. Love it	2023-11-05 12:22:02.481418+00	2023-11-05 12:22:02.481438+00	26	2
8	You guys are always full of energy. Love to see it.	2023-11-05 12:25:14.954227+00	2023-11-05 12:25:14.954254+00	23	1
9	One of our favourite spots to visit when we are in that part of the world. Thank you for sharing. We were there for deer rutting season last September and it was actually a little scary.	2023-11-05 12:30:08.31604+00	2023-11-05 12:30:08.316065+00	27	12
10	I have a small camper and it is definitely one of my favourite spots to sleep in because it gets really dark in there.	2023-11-05 16:37:36.365259+00	2023-11-05 16:37:36.36528+00	24	1
11	Gorgeous dog	2023-11-06 11:12:10.769606+00	2023-11-06 11:12:10.769647+00	25	1
12	Lovely photo	2023-11-09 15:01:13.901727+00	2023-11-09 15:01:23.624115+00	7	1
13	So happy to be here Di.	2023-11-10 11:20:28.193938+00	2023-11-10 11:20:28.193959+00	2	2
14	I love visiting Worcestershire, especially Malvern Hills	2023-11-11 14:41:01.806208+00	2023-11-11 14:41:01.806233+00	26	1
15	Nice to be able to share on here.	2023-11-11 15:13:57.086116+00	2023-11-11 15:13:57.086137+00	2	10
16	Always worth a visit	2023-11-11 15:28:30.980782+00	2023-11-11 15:28:30.980822+00	8	2
18	Need to visit here!	2023-11-11 17:43:49.492767+00	2023-11-11 17:43:49.492779+00	27	14
19	Brilliant!!	2023-11-11 17:48:21.017659+00	2023-11-11 17:48:21.017669+00	2	15
20	Love that.	2023-11-11 17:57:33.548204+00	2023-11-11 17:57:33.548215+00	31	2
21	Looks beautiful and cold!	2023-11-11 19:14:49.771157+00	2023-11-11 19:14:49.771172+00	31	16
22	Amazing photo. Snow is definitely not my thing though!	2023-11-12 10:17:05.958451+00	2023-11-12 10:17:05.95847+00	31	1
23	Amazing view of London.	2023-11-12 10:18:06.581819+00	2023-11-12 10:18:06.581836+00	32	1
24	The sea AND  a sunrise. What could be better.	2023-11-12 10:18:51.583809+00	2023-11-12 10:18:51.583827+00	35	1
25	Wow. Great photo. I love Paris... and baguettes LOL	2023-11-14 13:16:55.986757+00	2023-11-14 13:16:55.986775+00	38	2
26	Welcome. Love your spot. Nothing better than time with great friends.	2023-11-17 09:33:17.967645+00	2023-11-17 09:33:17.96766+00	47	10
\.


--
-- Data for Name: locations_location; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.locations_location (id, title, description, image, image_alt, location_types, posted_date, user_id, slug) FROM stdin;
1	Relaxing Walk	This is one of my favourite places to take a relaxing walk when I am visiting family. It is in Albrighton, Wolverhampton. It is the Donington and Albrighton local nature reserve. A lovely park with a shallow stream and wooden bridges. It is small so don’t expect much!	image/upload/v1698066052/ikvfnbvnkk7gu9khk4jv.jpg	wolverhampton	great_britain	2023-10-23 13:00:52.490236+00	2	relaxing-walk
3	Wild Swim	There is a great place to enjoy wild swimming in Shropshire called Simpsons Pool. The pool is a very deep quarry and access is via a gate and a short walk. Please be respectful when parking and don't block cars in or disturb residents/church goers. The pool is used by a local school during the day so if you arrive and there are children present don't stay. Leave and return later. Early mornings and evenings are best.	image/upload/v1698160617/o40kjls6aonmap8hp8pe.jpg	wild swim	great_britain	2023-10-24 15:16:58.030901+00	1	wild-swim
6	Walks in the woods	This is one of my favourite spots. It is in Warwickshire and it is a great place for dog walkers. There are miles and miles of pathways that you can walk along. There aren’t many places to sit though so it is worth taking a look at the maps at the entrance and as you walk around the forest. Getting lost is an option and definitely an easy thing to do.	image/upload/v1698160881/h6r49wxjg1pg3ckyrg6l.jpg	woodlands	great_britain	2023-10-24 15:21:21.762808+00	2	walks-in-the-woods
8	New York	The place to be for food and fun. When I need to clear my mind and focus on the present moment this is my spot for sure.	image/upload/v1698166179/voigbjspyufdoa5urseu.jpg	central park	america	2023-10-24 16:49:40.095217+00	4	new-york
9	Train Travel Zagreb	London to Zagreb & Croatia  A train ride that took us from London to Croatia to visit the wife's family with a stop at Zagreb. Loved this photo because we were so relaxed and happy at the time. Our spot is Maksimir Park. Not only because it is the oldest public park in Zagreb, Croatia. It forms part of the city's cultural heritage and is a habitat for many different plant and animal species. But also because it is where I asked her to marry me.	image/upload/v1698764635/xyrbchzoqsyyxx6tzthl.webp	zagreb	europe	2023-10-31 15:03:56.004651+00	3	train-travel-zagreb
10	Newport Wales	I love Beechwood Park in Newport, Wales. There are so many great places to walk and enjoy a picnic. Watch out for the opening times though so your car doesn’t end up locked in the car park (long story!) Look out for wildlife walks if you are around Newport. There are signs for them and you can follow without getting lost. Whenever I visit Cardiff I always stop at Newport either on the way to or on the way home.	image/upload/v1698847535/gwqbewozo5x6iof27lyd.jpg	wales	great_britain	2023-11-01 14:05:35.550634+00	1	newport-wales
11	Walking in Luton	I live in Luton around Warden Hills and it is a great place to go for a walk and to get away from daily life for a bit. If you are looking for a place to take your 10 minute walk, as recommended by the NHS to improve our mental health, I recommend Walden Hills	image/upload/v1698847735/palzycucli93kvvoyogw.jpg	luton	great_britain	2023-11-01 14:08:56.235233+00	6	walking-in-luton
13	Lafayette Square	A morning walk. A chance to sit and enjoy. Relatively quiet today.	image/upload/v1698848880/bawtdoeze26oudqzxhlj.png	lafayette square	america	2023-11-01 14:28:00.973237+00	4	lafayette-square
15	Queensland Australia	The beaches in Australia are amazing and although I look moody in this photo I was actually happy.  No Really. I walk along the beaches every day and am grateful for such a blessing.	image/upload/v1698928132/gspjguxnty2aaqtkfges.jpg	queensland	oceanic	2023-11-02 12:28:53.114857+00	11	queensland-australia
21	Our eating spot	When we are hiking in the Lake District we stop at the same spot to eat. If I could tell you the exact location I would but it can be a little hard to pinpoint. We always manage to find it more by luck than anything.	image/upload/v1698934736/qhgvgcek3eimgbpsg3qk.jpg	eating lake district	great_britain	2023-11-02 14:18:56.738147+00	13	our-eating-spot
22	Matthew and our dogs	This is me and my boyfriend Matthew and our dogs Fred and Bruno. Most weekends we travel around Scotland in our van. We have so many favourite spots we can't wait to share.	image/upload/v1698938704/yhhuxuowhmqsetqiuod0.jpg	bobbi and matthew	great_britain	2023-11-02 15:25:05.039903+00	12	matthew-and-our-dogs
19	Sunset beach walk	Is there anything better than a walk along the beach at sunset. Usually I have the company of a few friends but I love it just as much when I am alone.	image/upload/v1698929278/f7unxgo6l5biizbdeptf.jpg	beach walk	oceanic	2023-11-02 12:47:58.552582+00	11	sunset-beach-walk
20	Lake District National Park	I hike with my daughter Simone. We love the Lake District and visit often. This will always be our spot. We also spend time visiting the market towns such as Kendal, Ambleside and Keswick on scenic Derwentwater.	image/upload/v1698934612/jks1zyhlscvlonvgg0qc.jpg	lake district	great_britain	2023-11-02 14:16:53.20697+00	13	lake-district-national-park
7	Hamburg Germany	This is Hamburg, Germany. A great place for water adventures. The city on the River Elbe is really popular. We (hubby and I) attended a masquerade ball but you will also find live concerts, poetry slams, book readings and more. test	image/upload/v1698160928/vwnykcb07a1p6dyevpxk.jpg	hamburg	europe	2024-01-06 18:59:33.812807+00	2	hamburg-germany
14	Wightwick Manor Staffordshire	I live on a narrowboat and usually moor in Cumbria but I have been moving around. Found myself in a peaceful part of Staffordshire and stayed for months. I love being on the water. Do you have a water boat spot?	image/upload/v1698927461/z0lcdahynudckpgcljf1.jpg	wightwick	great_britain	2023-11-12 11:00:08.515375+00	10	wightwick-manor-staffordshire
2	Our Spot Photo Sharing Platform	Welcome to Our Spot photo sharing platform/social network. A place where you can add the places around the world that you love the most. Share your Spot. Let others find, comment on and like your Spot. This is a place to share the places you love to go and search for great places to visit whether that is on your own, with a friend/partner or with your family. Your Spot. My Spot. Our Spot.The name was inspired by the Willow Smith & Tyler Cole song "Meet Me At Our Spot"	image/upload/v1698066349/jmcsbzsklx1takloxyo5.png	our spot social network	great_britain	2023-11-12 11:05:15.76119+00	1	our-spot-social-network
23	Bike riding with friends	This photo was taken on a journey into the heart of the wild Cairngorms National Park. Six of us and our bikes. The wildlife is amazing, especially the deer.	image/upload/v1698939183/hviurzn7tuevs7urnmkp.jpg	bike riding scotland	great_britain	2023-11-02 15:33:03.842985+00	12	bike-riding-with-friends
24	Our Van Spot	Even when we have no place to go Matthew and I will hang out in the van. It's our favourite place to have fun with each other and talk about past trips, plus plan future ones. We keep what we eat fairly simply when we are out.	image/upload/v1698939537/cyl7cefgwwzboxwyr0wi.jpg	van cooking	great_britain	2023-11-02 15:38:58.455209+00	12	our-van-spot
25	Bruno my best friend	The other love of my life is my dog Bruno and before I met Matthew we spent months visiting great places around Scotland and Ireland.	image/upload/v1698940562/qflpqsmbbe2dpm9h4rzh.jpg	bobbi	great_britain	2023-11-02 15:56:03.2707+00	12	bruno-my-best-friend
12	Sundon Hills	Today I headed out to Sundon Hills which is in the Chiltern Hills area. Another great place to stretch my legs. You can park in the Red Lion and I often stop and enjoy something to drink, especially if I have managed to walk for quite a while. The Smithcombe, Sharpenhoe and Sundon Hills cover 86 hectares in Bedfordshire. With thick forests, gentle slopes and wildflowers, the area is a lovely place to cycle, hike and enjoy a picnic. Lovely day.	image/upload/v1698848156/kgwwmomhmcitkryrxkiq.jpg	sundon hills	great_britain	2023-11-02 18:29:12.780244+00	6	sundon-hills
26	Cold and foggy Worcestershire	I love an early morning walk and this was 6am this morning. A cold and foggy Worcestershire morning. As I type this though the weather is sunny and its lovely walking weather so time to get out there.	image/upload/v1699185900/ehxxiklycrizb3jxl58c.jpg	worcester	great_britain	2023-11-05 12:05:01.475141+00	7	cold-and-foggy-worcestershire
27	Wyre Forest	Wyre Forest is the largest woodland National Nature Reserve in the country and can be found to the west of Birmingham. I love to visit and walk and sit. There's always someone friendly to start up a conversation with if you, like me, find yourself living alone and in need of company.	image/upload/v1699186056/l75qbnlpaehsf7a0fatw.jpg	wyre forest	great_britain	2023-11-05 12:07:38.307391+00	7	wyre-forest
30	Travelling Ireland!	We had to stop here on our trip - my husband is such a child!	image/upload/v1699724959/jakyaeamjcuq3acvayqs.jpg	Road sign for Muff in Ireland	europe	2023-11-11 17:49:19.696401+00	14	travelling-ireland
40	Magic Kingdom Disney World	Great place for a family day out. Not a massive rollercoaster person but why not when you’re in the happiest place on earth!	image/upload/v1699790103/cwkvtqmzd7vjb6uadsn6.jpg	Disney	america	2023-11-12 11:55:04.174845+00	15	magic-kingdom-disney-world
33	Old Trafford, Manchester	Recently went to one of the most famous football stadiums in the UK! Watched Manchester United vs Luton Town from the away end. Shame about the result.	image/upload/v1699781261/vumfmmglnzj5tcj12v84.jpg	Old Trafford	great_britain	2023-11-12 09:27:41.704596+00	15	old-trafford-manchester
34	Kissonerga Cyprus	Afternoon walks along the promenade in Kissonerga, Cyprus. Trying to burn off the all inclusive breakfast and drinks!	image/upload/v1699781374/m66zh5fttxyaxebh5uop.jpg	Coastal walk	europe	2023-11-12 09:29:35.421489+00	15	kissonerga-cyprus
35	Ibiza Sunrises	6:30am sunrise in San Antonio Bay, Ibiza. I’d love to say I woke up early especially for this but in reality I’d just got back to the hotel after a long night partying LOL!	image/upload/v1699781645/zmb66garoj8uiji9jwlu.jpg	Ibiza Sunrise	europe	2023-11-12 09:34:05.995396+00	15	ibiza-sunrises
36	Dubai Home	I love Dubai. It's my second home and although there isn't much green its still my favourite place to be	image/upload/v1699786571/keguwdlzkrwrvajzzjgd.jpg	dubai	africa	2023-11-12 10:56:11.517448+00	15	dubai-home
37	New York New York	What more can I say. The food is amazing. The history is worth investigating.	image/upload/v1699786698/dwwobag19v5nr13bllmy.jpg	new york	america	2023-11-12 10:58:18.792518+00	15	new-york-new-york
31	Walking the forests of Latvia	Visiting friends and we went on a walk in the forest. I forget what it was called now, but it was only a short drive from the capital, Liga.	image/upload/v1699725081/bmkvzkluwpstzvw4oq2f.jpg	Latvian forest	europe	2023-11-12 11:03:53.815886+00	14	walking-the-forests-of-latvia
32	London views	This was taken from a roof in South London giving an excellent view of the London skyline. Its a shame the sun didn't decide to make an appearance for this picture :)	image/upload/v1699729462/yajz8ybecu0y7dhfpacr.jpg	Roof top pictures	europe	2023-11-12 11:04:15.911906+00	16	london-views
38	Eiffel Tower, Paris	A boat trip on the river Seine in Paris. Great city for a weekend trip. Especially if you’re like me and love a baguette.	image/upload/v1699789193/zzdfgtw1wrldzkwocs1h.jpg	Paris	europe	2023-11-12 11:39:53.622507+00	15	eiffel-tower-paris
39	NFL Sundays	Sunday Gameday! Tampa Bay Buccaneers vs Atlanta Falcons. A good game to watch but damn was it hot.	image/upload/v1699789994/sa3dn7kgoslvmxtixkzn.jpg	Buccaneers	america	2023-11-12 11:53:14.74865+00	15	nfl-sundays
47	On the beach	I can't think of a better way to spend the weekend than on the beach with friends, food and banter. Best group of friends.	image/upload/v1700213488/zfrncgodh82nqaex4vo7.jpg	Beach	caribbean	2023-11-17 09:31:29.177917+00	20	on-the-beach
\.


--
-- Data for Name: locations_location_likes; Type: TABLE DATA; Schema: public; Owner: qcjurrgz
--

COPY public.locations_location_likes (id, location_id, user_id) FROM stdin;
1	27	1
2	2	2
3	2	11
4	26	1
5	26	2
6	27	2
7	13	2
8	12	10
9	2	10
10	8	2
11	15	1
12	9	2
13	2	1
14	7	2
17	2	15
18	30	15
19	27	15
20	26	15
21	14	15
22	11	15
23	31	2
24	30	2
27	31	15
28	33	2
29	35	2
30	25	2
31	35	1
32	31	1
33	30	1
35	36	1
36	36	2
37	36	4
38	36	6
39	36	7
40	36	12
41	36	14
42	36	15
43	36	16
44	37	3
45	37	13
46	32	11
47	32	12
48	32	4
49	37	1
50	31	11
51	31	5
52	32	1
53	32	2
54	32	3
55	32	15
56	2	3
57	2	4
58	2	5
59	2	6
60	2	7
61	2	12
62	2	13
63	2	14
64	2	16
65	37	2
66	39	1
67	38	2
69	31	10
70	47	10
71	14	10
\.


--
-- Name: account_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.account_profile_id_seq', 29, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 29, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 59, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 54, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: easy_thumbnails_source_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.easy_thumbnails_source_id_seq', 1, false);


--
-- Name: easy_thumbnails_thumbnail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.easy_thumbnails_thumbnail_id_seq', 1, false);


--
-- Name: easy_thumbnails_thumbnaildimensions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.easy_thumbnails_thumbnaildimensions_id_seq', 1, false);


--
-- Name: locations_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.locations_comment_id_seq', 26, true);


--
-- Name: locations_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.locations_location_id_seq', 48, true);


--
-- Name: locations_location_likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qcjurrgz
--

SELECT pg_catalog.setval('public.locations_location_likes_id_seq', 72, true);


--
-- Name: account_profile account_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_pkey PRIMARY KEY (id);


--
-- Name: account_profile account_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_user_id_key UNIQUE (user_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: easy_thumbnails_source easy_thumbnails_source_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_source
    ADD CONSTRAINT easy_thumbnails_source_pkey PRIMARY KEY (id);


--
-- Name: easy_thumbnails_source easy_thumbnails_source_storage_hash_name_481ce32d_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_source
    ADD CONSTRAINT easy_thumbnails_source_storage_hash_name_481ce32d_uniq UNIQUE (storage_hash, name);


--
-- Name: easy_thumbnails_thumbnail easy_thumbnails_thumbnai_storage_hash_name_source_fb375270_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnail
    ADD CONSTRAINT easy_thumbnails_thumbnai_storage_hash_name_source_fb375270_uniq UNIQUE (storage_hash, name, source_id);


--
-- Name: easy_thumbnails_thumbnail easy_thumbnails_thumbnail_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnail
    ADD CONSTRAINT easy_thumbnails_thumbnail_pkey PRIMARY KEY (id);


--
-- Name: easy_thumbnails_thumbnaildimensions easy_thumbnails_thumbnaildimensions_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnaildimensions
    ADD CONSTRAINT easy_thumbnails_thumbnaildimensions_pkey PRIMARY KEY (id);


--
-- Name: easy_thumbnails_thumbnaildimensions easy_thumbnails_thumbnaildimensions_thumbnail_id_key; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnaildimensions
    ADD CONSTRAINT easy_thumbnails_thumbnaildimensions_thumbnail_id_key UNIQUE (thumbnail_id);


--
-- Name: locations_comment locations_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_comment
    ADD CONSTRAINT locations_comment_pkey PRIMARY KEY (id);


--
-- Name: locations_location_likes locations_location_likes_location_id_user_id_dfb1bd7a_uniq; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location_likes
    ADD CONSTRAINT locations_location_likes_location_id_user_id_dfb1bd7a_uniq UNIQUE (location_id, user_id);


--
-- Name: locations_location_likes locations_location_likes_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location_likes
    ADD CONSTRAINT locations_location_likes_pkey PRIMARY KEY (id);


--
-- Name: locations_location locations_location_pkey; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location
    ADD CONSTRAINT locations_location_pkey PRIMARY KEY (id);


--
-- Name: locations_location locations_location_slug_key; Type: CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location
    ADD CONSTRAINT locations_location_slug_key UNIQUE (slug);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: easy_thumbnails_source_name_5fe0edc6; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_source_name_5fe0edc6 ON public.easy_thumbnails_source USING btree (name);


--
-- Name: easy_thumbnails_source_name_5fe0edc6_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_source_name_5fe0edc6_like ON public.easy_thumbnails_source USING btree (name varchar_pattern_ops);


--
-- Name: easy_thumbnails_source_storage_hash_946cbcc9; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_source_storage_hash_946cbcc9 ON public.easy_thumbnails_source USING btree (storage_hash);


--
-- Name: easy_thumbnails_source_storage_hash_946cbcc9_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_source_storage_hash_946cbcc9_like ON public.easy_thumbnails_source USING btree (storage_hash varchar_pattern_ops);


--
-- Name: easy_thumbnails_thumbnail_name_b5882c31; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_thumbnail_name_b5882c31 ON public.easy_thumbnails_thumbnail USING btree (name);


--
-- Name: easy_thumbnails_thumbnail_name_b5882c31_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_thumbnail_name_b5882c31_like ON public.easy_thumbnails_thumbnail USING btree (name varchar_pattern_ops);


--
-- Name: easy_thumbnails_thumbnail_source_id_5b57bc77; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_thumbnail_source_id_5b57bc77 ON public.easy_thumbnails_thumbnail USING btree (source_id);


--
-- Name: easy_thumbnails_thumbnail_storage_hash_f1435f49; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_thumbnail_storage_hash_f1435f49 ON public.easy_thumbnails_thumbnail USING btree (storage_hash);


--
-- Name: easy_thumbnails_thumbnail_storage_hash_f1435f49_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX easy_thumbnails_thumbnail_storage_hash_f1435f49_like ON public.easy_thumbnails_thumbnail USING btree (storage_hash varchar_pattern_ops);


--
-- Name: locations_comment_location_id_ea034776; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_comment_location_id_ea034776 ON public.locations_comment USING btree (location_id);


--
-- Name: locations_comment_user_id_e374516f; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_comment_user_id_e374516f ON public.locations_comment USING btree (user_id);


--
-- Name: locations_location_likes_location_id_b2171f17; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_location_likes_location_id_b2171f17 ON public.locations_location_likes USING btree (location_id);


--
-- Name: locations_location_likes_user_id_da7bd690; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_location_likes_user_id_da7bd690 ON public.locations_location_likes USING btree (user_id);


--
-- Name: locations_location_slug_0338bba7_like; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_location_slug_0338bba7_like ON public.locations_location USING btree (slug varchar_pattern_ops);


--
-- Name: locations_location_user_id_cd2ca905; Type: INDEX; Schema: public; Owner: qcjurrgz
--

CREATE INDEX locations_location_user_id_cd2ca905 ON public.locations_location USING btree (user_id);


--
-- Name: account_profile account_profile_user_id_bdd52018_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_user_id_bdd52018_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: easy_thumbnails_thumbnail easy_thumbnails_thum_source_id_5b57bc77_fk_easy_thum; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnail
    ADD CONSTRAINT easy_thumbnails_thum_source_id_5b57bc77_fk_easy_thum FOREIGN KEY (source_id) REFERENCES public.easy_thumbnails_source(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: easy_thumbnails_thumbnaildimensions easy_thumbnails_thum_thumbnail_id_c3a0c549_fk_easy_thum; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.easy_thumbnails_thumbnaildimensions
    ADD CONSTRAINT easy_thumbnails_thum_thumbnail_id_c3a0c549_fk_easy_thum FOREIGN KEY (thumbnail_id) REFERENCES public.easy_thumbnails_thumbnail(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: locations_comment locations_comment_location_id_ea034776_fk_locations_location_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_comment
    ADD CONSTRAINT locations_comment_location_id_ea034776_fk_locations_location_id FOREIGN KEY (location_id) REFERENCES public.locations_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: locations_comment locations_comment_user_id_e374516f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_comment
    ADD CONSTRAINT locations_comment_user_id_e374516f_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: locations_location_likes locations_location_l_location_id_b2171f17_fk_locations; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location_likes
    ADD CONSTRAINT locations_location_l_location_id_b2171f17_fk_locations FOREIGN KEY (location_id) REFERENCES public.locations_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: locations_location_likes locations_location_likes_user_id_da7bd690_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location_likes
    ADD CONSTRAINT locations_location_likes_user_id_da7bd690_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: locations_location locations_location_user_id_cd2ca905_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: qcjurrgz
--

ALTER TABLE ONLY public.locations_location
    ADD CONSTRAINT locations_location_user_id_cd2ca905_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

