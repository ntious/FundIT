-- 02_seed.sql: sample data (idempotent inserts)
SET search_path TO lab, public;

INSERT INTO students (first_name, last_name, email) VALUES
  ('Alex','Rivera','alex.rivera@example.edu'),
  ('Bri','Chen','bri.chen@example.edu'),
  ('Cam','Lopez','cam.lopez@example.edu')
ON CONFLICT DO NOTHING;

INSERT INTO courses (course_code, title) VALUES
  ('IT1050','Fundamentals of IT'),
  ('IT2023','Information Security & Assurance'),
  ('IT4065C','Data Technologies Administration')
ON CONFLICT DO NOTHING;

-- Enroll everyone in the first two courses (avoid duplicates)
INSERT INTO enrollments (student_id, course_id)
SELECT s.student_id, c.course_id
FROM students s CROSS JOIN LATERAL (
  SELECT course_id FROM courses WHERE course_code IN ('IT1050','IT2023')
) c
ON CONFLICT DO NOTHING;
