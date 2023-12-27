CREATE TABLE calificacion (
	cali_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	cali_estrellas INT,
    cali_avg FLOAT,
    lista_id INT,
    FOREIGN KEY (lista_id) REFERENCES lista_comentarios(lista_id)
);
