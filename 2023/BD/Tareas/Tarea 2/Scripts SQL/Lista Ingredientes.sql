CREATE TABLE lista_ingredientes (
	lista_ing_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ingre_id int,
    FOREIGN KEY(ingre_id) REFERENCES ingredientes(ingre_id)
);
    