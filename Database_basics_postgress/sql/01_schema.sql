-- 01_schema.sql: additional constraints and useful views
SET search_path TO lab, public;

-- Add a uniqueness constraint on course_code
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint WHERE conname = 'courses_course_code_key'
  ) THEN
    ALTER TABLE courses ADD CONSTRAINT courses_course_code_key UNIQUE (course_code);
  END IF;
END$$;

-- Helpful view: student enrollments with names
CREATE OR REPLACE VIEW v_student_courses AS
SELECT s.student_id, s.first_name, s.last_name, c.course_code, c.title
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id;
