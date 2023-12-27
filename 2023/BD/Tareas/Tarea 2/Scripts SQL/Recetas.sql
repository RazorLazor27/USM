create table menu (
	menu_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    receta_foto BLOB,
    receta_nombre VARCHAR(100) NOT NULL,
    receta_instrucciones VARCHAR(1000),
    receta_tiempo float,
    receta_diabetico BOOL,
    receta_lactosa BOOL,
    receta_gluten BOOL,
    receta_vegan BOOL,
    receta_type INT NOT NULL,
    comentario_id INT,
    lista_ing_id INT,
    FOREIGN KEY (comentario_id) REFERENCES comentarios(comentario_id),
    FOREIGN KEY (lista_ing_id) REFERENCES lista_ingredientes(lista_ing_id)
);
    
    