show databases;
use sakila;
select concat(first_name," ",last_name) as full_name from customer;
select last_name from customer where last_name like "M%__r_";
select * from customer;
select first_name, last_name, store_id from customer order by(store_id);
delimiter &&
create procedure select_names(out fn varchar (10) )
begin
select first_name, store_id from customer where first_name=fn;
end
&& delimiter ;
call select_names('Mary');
select rank() over (partition by store_id) as row_num, first_name from customer;
