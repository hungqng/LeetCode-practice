-- 181. Employees Earning More Than Their Managers

-- Write an SQL query to find the employees who earn more than their managers.

-- Return the result table in any order.

-- The query result format is in the following example.

SELECT e1.Name AS Employee
FROM Employee e1 JOIN Employee e2
ON e1.ManagerID = e2.Id 
WHERE e1.Salary > e2.Salary