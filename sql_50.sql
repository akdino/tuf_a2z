--1
select w.name, w.population, w.area from World w 
where w.area>=3000000 or w.population >=25000000;

--2
select unique_id ,name from 
employees left join employeeUNI 
using (id)

--3
select p.product_name, s.year, s.price 
from sales s left join product p
on s.product_id=p.product_id;

--7
select p.product_name, s.year, s.price 
from sales s natural join product p

--8
select customer_id ,count(*) as count_no_trans
from visits 
where 
visit_id not in(
select visits.visit_id from visits
right join transactions 
on visits.visit_id=transactions.visit_id)
group by customer_id;

--9
select w1.id from weather w1 join weather w2
where DATEDIFF(w1.recordDate,w2.recordDate)=1 and w1.temperature>w2.temperature

--10
select machine_id, round(avg(diff),3) as processing_time from
(select t1.machine_id,t1.timestamp - t2.timestamp as diff from activity t1 
join activity t2 
on t1.machine_id=t2.machine_id
where 
t1.activity_type="end" and t2.activity_type="start"
and t1.process_id=t2.process_id
)AS sub
group by machine_id

--11
select e.name,b.bonus
from employee e left join
bonus b on 
e.empId=b.empId
where b.bonus<1000 or b.bonus is null

--13
select s.user_id, round(sum(case when c.action="confirmed" then 1 else 0 End)/count(s.user_id),2) as confirmation_rate
from signups s
left join confirmations c 
on s.user_id=c.user_id
group by c.user_id

--14
select * from cinema
where MOD(id,2)=1 and description!="boring"
order by rating desc

--15
select p.product_id, 
case when sum(u.units)>0 then round(sum(p.price * u.units)/sum(units),2) 
else 0
end as average_price from prices p 
left join unitsSold u 
on p.product_id=u.product_id 
and u.purchase_date BETWEEN p.start_date AND p.end_date
group by product_id

--16
select p.project_id, round(sum(e.experience_years)/count(experience_years),2) as average_years
from project p left join employee e 
on e.employee_id=p.employee_id
group by project_id

--17

--18
select query_name, round(sum(rating/position)/count(rating),2) as quality,
round(sum(case when rating<3 then 1 else 0 end)/count(rating)*100,2) as poor_query_percentage
from queries
group by query_name

--19
select DATE_FORMAT(trans_date, '%Y-%m') as month,country,
count(*) as trans_count,
sum(case when state="approved" then 1 else 0 end) as approved_count, 
sum(amount) as trans_total_amount, sum(case when state="approved" then amount else 0 end) as approved_total_amount 
from transactions group by country, month

--20
select 
round(sum(
    case when order_date=customer_pref_delivery_date and order_date in
        (select min(order_date) from delivery d1
        where d2.customer_id=d1.customer_id) 
        then 1 else 0 end) / count(distinct customer_id)*100,2) as immediate_percentage
from delivery d2

--21
select round(sum(case when DATE_SUB(event_date, INTERVAL 1 DAY)
in 
(select min(event_date) from Activity a1
WHERE a2.player_id = a1.player_id
)
then 1 else 0 end)
/count(distinct player_id),2)
as fraction
from Activity a2

--22
select s.product_id,s.year as first_year,s.quantity, s.price
from sales s
join
    (select product_id, MIN(year) AS first_year
    from Sales
    group by product_id
) t
on s.product_id = t.product_id
and s.year = t.first_year;

--23
select class from courses
group by class
having count(student)>=5

--24
select user_id,count(user_id) as followers_count
from followers
group by user_id
order by user_id

(vs)

select distinct user_id, count( distinct follower_id) as followers_count
from Followers
group by user_id
order by user_id
--as user_id,follower_is is primary key first one is best(i wrote)

--25
select max(num) as num from 
(select num from mynumbers
group by num
having count(num)=1) t

--26
SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)

--27
select * from patients
where conditions like "DIAB1%" or conditions like "% DIAB1%"

--28
select e2.employee_id, e2.name, count(*) as reports_count , round(sum(e1.age)/count(*)) as average_age
from Employees e1
join Employees e2
on e1.reports_to=e2.employee_id
group by e2.employee_id
order by e2.employee_id

--29
select employee_id, department_id
from Employee
where primary_flag="Y"
UNION
select employee_id, department_id
from Employee
group by employee_id
having count(employee_id)=1

--30
select x,y,z,
case when
x+y>z and x+z>y and y+z>x then "Yes"
else "No"
end as triangle
from triangle

--31
select distinct l1.num as ConsecutiveNums from logs l1, logs l2,logs l3
where (l1.num=l2.num and l2.num=l3.num)
and l1.id+1=l2.id and l2.id+1=l3.id

--32
select product_id, new_price as price
from products
where (product_id,change_date) in (
    select product_id,max(change_date)
    from products
    WHERE change_date <= '2019-08-16'
    group by product_id
)
union
select product_id, 10 as price
from products
WHERE(product_id) NOT IN
(
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
);

--33
select 
case when count(*)=1
then null
else 
(select salary
from employee
where salary<(select max(salary) from employee) 
order by salary desc
limit 1)
end as secondHighestSalary
from employee
(or)
select max(salary) as SecondHighestSalary from employee 
where salary < (select max(salary) from employee)

--34
select sell_date,count(distinct product) as num_sold,GROUP_CONCAT(distinct product order by product separator ',') as products
from Activities
group by sell_date
order by sell_date 

--35
select p.product_name, sum(o.unit) as unit
from Products p left join Orders o 
on p.product_id=o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by o.product_id
having sum(o.unit)>=100

--36
SELECT *
FROM users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 'c');

--37
select name as person_name from 
(select person_name as name ,sum(weight) over (order by turn) as totweight
from Queue
order by turn) as t
where totweight<=1000
order by totweight desc
limit 1


--38
select "Low Salary" as category ,sum(case when income<20000 then 1 else 0 end) as accounts_count
from Accounts
union 
select "Average Salary", sum(case when income>= 20000 and income<=50000 then 1 else 0 end) as accounts_count
from Accounts
union 
select "High Salary" , sum(case when income>50000 then 1 else 0 end) as accounts_count
from Accounts

--39
select id, student from 
(select case when id%2=0 
then id-1 end as id, student 
from seat 
union all 
select case when id%2=1 
then id+1 
end as id,student 
from seat 
where id <> (select max(id) from seat) 
union all 
select id,student from seat 
where (SELECT COUNT(*) FROM seat) % 2 =1 
and id = (select max(id) from seat)) as t 
where id is not null
ORDER BY id;
