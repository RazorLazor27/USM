CREATE TABLE users_fav_food (
	fav_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    receta_id int,
    cali_id int,
    FOREIGN KEY(receta_id) REFERENCES recetas(receta_id),
    FOREIGN KEY(cali_id) REFERENCES calificacion(cali_id)
);
    
    