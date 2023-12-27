create table lista_comentarios (
	lista_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    comentario_id INT,
    FOREIGN KEY(comentario_id) REFERENCES comentarios(comentario_id)
);
    