create table platillo (
	-- Esta cosa debe juntar las recetas con en menu, but howww
    platillo_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    receta_id INT,
    foreign key(receta_id) references recetas(receta_id)
);