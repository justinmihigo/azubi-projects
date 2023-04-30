
use justin;
show tables;
select * from student;
delimiter //
create trigger class_correct
before insert on student
for each row
if new.CLASS="" then set new.CLASS="MPG";
END IF; 
// delimiter ;
insert into student values("Jules",57,"");
select * from student;