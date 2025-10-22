-- 00_init.sql: one-time setup items (safe to re-run)
CREATE SCHEMA IF NOT EXISTS lab AUTHORIZATION CURRENT_USER;
SET search_path TO lab, public;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
  student_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name  TEXT NOT NULL,
  email      TEXT UNIQUE NOT NULL,
  enrolled_on DATE DEFAULT CURRENT_DATE
);

-- Create courses table
CREATE TABLE IF NOT EXISTS courses (
  course_id SERIAL PRIMARY KEY,
  course_code VARCHAR(20) NOT NULL,
  title VARCHAR(200) NOT NULL
);

-- Create enrollments table
CREATE TABLE IF NOT EXISTS enrollments (
  enrollment_id SERIAL PRIMARY KEY,
  student_id INT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE
);
