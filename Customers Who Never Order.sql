-- 183. Customers Who Never Order

-- Write an SQL query to report all customers who never order anything.

-- Return the result table in any order.

-- The query result format is in the following example.

-- # Write your MySQL query statement below
SELECT A.Name as Customers from Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId limit 1)