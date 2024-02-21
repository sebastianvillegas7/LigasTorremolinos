CREATE DATABASE IF NOT EXISTS ligas_torremolinos;
USE ligas_torremolinos;

create table if not exists deportes (
	id_deporte int primary key auto_increment,
    nombre varchar(50) not null unique -- Aumentado el tamaño del campo nombre
);

create table if not exists instalaciones (
	id_instalacion int primary key auto_increment,
    nombre varchar(50) not null unique, -- Aumentado el tamaño del campo nombre
    direccion varchar(100) not null,
    iluminacion boolean not null default false,
    cubierta boolean not null default false
);

create table if not exists equipos (
	id_equipo int primary key auto_increment,
    nombre varchar(50) not null unique, -- Aumentado el tamaño del campo nombre
    id_deporte int not null,
    equipacion_principal varchar(100) not null,
    equipacion_suplente varchar(100) not null,
    contacto varchar(100) not null,
    telefono varchar(15) not null,
    email varchar(100) not null,
    foreign key (id_deporte) references deportes(id_deporte) on delete restrict on update cascade
);

create table if not exists jugadores (
	id_jugador int primary key auto_increment,
    nombre varchar(50) not null, -- Aumentado el tamaño del campo nombre
    apellido1 varchar(50) not null, -- Aumentado el tamaño del campo apellido1
    apellido2 varchar(50), -- Aumentado el tamaño del campo apellido2
    id_equipo int not null,
    dorsal int not null,
    fecha_nacimiento date not null,
    altura decimal(3,2) not null check (altura > 0),
    peso int not null check (peso > 0),
    telefono varchar(15) not null,
    foreign key (id_equipo) references equipos(id_equipo) on delete restrict on update cascade
);

-- Índice para evitar que un dorsal se repita en un equipo
create unique index idx_equipo_dorsal on jugadores(id_equipo, dorsal);

CREATE TABLE IF NOT EXISTS partidos (
    id_partido INT PRIMARY KEY AUTO_INCREMENT,
    id_deporte INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    id_instalacion INT,
    id_equipo_local INT NOT NULL,
    id_equipo_visitante INT NOT NULL,
    puntos_local INT CHECK (puntos_local >= 0),
    puntos_visitante INT CHECK (puntos_visitante >= 0),
    observaciones VARCHAR(200),
    FOREIGN KEY (id_deporte) REFERENCES deportes(id_deporte) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_instalacion) REFERENCES instalaciones(id_instalacion) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_equipo_local) REFERENCES equipos(id_equipo) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_equipo_visitante) REFERENCES equipos(id_equipo) ON DELETE RESTRICT ON UPDATE CASCADE
);

