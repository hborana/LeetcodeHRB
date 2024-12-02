# Write your MySQL query statement below
Select
   e.name,
   b.bonus
From
   Employee e
Left join
   Bonus b
ON 
   e.empId = b.empId
where b.bonus < 1000 OR b.bonus IS NULL;