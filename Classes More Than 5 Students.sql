-- 596. Classes More Than 5 Students
-- Easy
-- 674
-- 1K
-- Companies
-- SQL Schema
-- Table: Courses

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student     | varchar |
-- | class       | varchar |
-- +-------------+---------+
-- (student, class) is the primary key column for this table.
-- Each row of this table indicates the name of a student and the class in which they are enrolled.
 

-- Write an SQL query to report all the classes that have at least five students.

-- Return the result table in any order.

-- The query result format is in the following example.

-- # Write your MySQL query statement below
SELECT class FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5