CREATE TABLE Users (
	personID int PRIMARY KEY AUTO_INCREMENT,
	username varchar(25),
	password varchar(25),
    user_type varchar(10)
);

insert into Users(username, password, user_type)
values ('bobby', '1234', 'user');

select * FROM Users;

CREATE TABLE Items (
	item_number int primary key AUTO_INCREMENT,
	item_name varchar(25),
	item_type varchar(10),
    price int
);

insert into Items(item_name, item_type, price)
values (
'Stickers', 'Other', 2.99
);

select * from Items;

select price from Items where item_name = 'Digital';

CREATE TABLE Orders (
	order_number int primary key AUTO_INCREMENT,
    customer_id int,
    total int,
	FOREIGN KEY (customer_id) REFERENCES Users(personID)
    );
    
select * from Orders;
DELETE FROM Users WHERE username = 'woah';