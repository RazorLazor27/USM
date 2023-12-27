create table Users(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    user_password varchar(255) NOT NULL,
    user_num_almuerzos INT NULL,
    users_login_date DATE,
    users_login_hour TIME
);