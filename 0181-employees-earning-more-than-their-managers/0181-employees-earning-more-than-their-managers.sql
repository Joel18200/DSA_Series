 select e.name as 'Employee' from Employee e
 join Employee d
 on e.managerId=d.id
 where e.salary>d.salary;
