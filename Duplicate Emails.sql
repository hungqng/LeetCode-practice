-- 182. Duplicate Emails

-- Write an SQL query to report all the duplicate emails.

-- Return the result table in any order.

-- The query result format is in the following example.

-- # Write your MySQL query statement below
SELECT email
FROM person
GROUP BY email
HAVING COUNT(email) > 1