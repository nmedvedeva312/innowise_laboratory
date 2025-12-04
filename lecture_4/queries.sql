-- ----------------------------
--   Lecture 4 - SQL Queries
-- ----------------------------

-- 1. Find all grades for a specific student (Alice Johnson)
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 2. Calculate the average grade per student
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id;

-- 3. List all students born after 2004
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 4. List all subjects and their average grades
SELECT subject, ROUND(AVG(grade), 2) AS average_grade
FROM grades
GROUP BY subject;

-- 5. Top 3 students with the highest average grades
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 3;

-- 6. Students who have scored below 80 in any subject
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade < 80;

-- Optional: indexes for optimization
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);
CREATE INDEX IF NOT EXISTS idx_grades_grade ON grades(grade);