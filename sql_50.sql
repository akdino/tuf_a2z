select w.name, w.population, w.area from World w 
where w.area>=3000000 or w.population >=25000000;

select unique_id ,name from 
employees left join employeeUNI 
using (id)

select p.product_name, s.year, s.price 
from sales s left join product p
on s.product_id=p.product_id;