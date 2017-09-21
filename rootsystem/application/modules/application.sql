CREATE TABLE IF NOT EXISTS producto (
    producto_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    denominacion VARCHAR(100),
    precio DECIMAL(6,2)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS domicilio(
  domicilio_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  numero VARCHAR(100),
  puerta VARCHAR(100),
  calle VARCHAR(100),
  piso INT(11),
  ciudad VARCHAR(25),
  cp VARCHAR(20)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS datodecontacto(
  datodecontacto_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  mail VARCHAR(100),
  telefono VARCHAR(25)
)ENGINE=InnoDB;
