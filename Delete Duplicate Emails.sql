-- 196. Delete Duplicate Emails

-- SQL Schema
-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table contains an email. The emails will not contain uppercase letters.
 

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

-- Return the result table in any order.

-- The query result format is in the following example.

-- # Please write a DELETE statement and DO NOT write a SELECT statement.
-- # Write your MySQL query statement below
DELETE p1
FROM Person p1 JOIN Person p2
ON p1.Email = p2.Email
AND p1.Id < p2.Id

-- Solution 2
DELETE p from Person p, Person q where p.Id>q.Id AND q.Email=p.Email 

-- Solution 3
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;