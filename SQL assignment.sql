create database xyz;
use xyz;
## problem is find out product_id which have no likes
## first of all we create a table products 
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);

insert into products values
(1001,"blogs"),
(1002,"youtube"),
(1003,"facebook"),
(1004,"linkdin"),
(1005,"instagram"),
(1006,"twitter");
select*from products;

CREATE TABLE ProductLikes 
(
    user_id int8,
    product_id INT,
    like_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

insert into productlikes values
(1,1004,'2023-08-10'),
(2,1001,'2023-08-01'),
(3,1002,'2023-08-15'),
(4,1001,'2023-07-10'),
(5,1002,'2023-06-10'),
(6,1005,'2023-08-30'),
(7,1004,'2023-08-25'),
(8,1003,'2023-08-20'),
(9,1004,'2023-08-21');

## we use join operation 
select a.product_id , count(distinct user_id) from products a left join
productlikes b on a.product_id=b.product_id
group by a.product_id
having count(distinct user_id)=0
order by a.product_id;