# CREACIÓN DE JUGADORES PARA EQUIPOS DE FUTBOL, 11 POR EQUIPO
-- Jugadores para el equipo ID 1 (Club Deportivo Los Leones)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (1, 'Luis', 'García', 'Martínez', 1, 1, '1995-03-15', 1.80, 75, '123456789'),
    (2, 'Carlos', 'Hernández', 'López', 1, 2, '1996-07-21', 1.85, 80, '234567890'),
    (3, 'Juan', 'Rodríguez', 'Gómez', 1, 3, '1994-11-10', 1.75, 70, '345678901'),
    (4, 'Pedro', 'Fernández', 'Sánchez', 1, 4, '1993-08-05', 1.82, 78, '456789012'),
    (5, 'David', 'López', 'Pérez', 1, 5, '1997-06-30', 1.79, 76, '567890123'),
    (6, 'Manuel', 'Gómez', 'Martínez', 1, 6, '1992-04-25', 1.81, 77, '678901234'),
    (7, 'José', 'Martínez', 'Hernández', 1, 7, '1996-01-20', 1.78, 74, '789012345'),
    (8, 'Javier', 'Pérez', 'Rodríguez', 1, 8, '1995-10-15', 1.83, 79, '890123456'),
    (9, 'Antonio', 'Sánchez', 'Fernández', 1, 9, '1994-09-10', 1.76, 72, '901234567'),
    (10, 'Mario', 'Martínez', 'Gómez', 1, 10, '1993-07-05', 1.80, 75, '012345678'),
    (11, 'Miguel', 'Fernández', 'López', 1, 11, '1998-02-28', 1.77, 73, '987654321');


-- Jugadores para el equipo ID 2 (Club Atlético Las Águilas)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (12, 'Eduardo', 'Gómez', 'Martínez', 2, 1, '1994-04-20', 1.82, 77, '123456789'),
    (13, 'Sergio', 'Hernández', 'López', 2, 2, '1993-09-15', 1.79, 75, '234567890'),
    (14, 'Jorge', 'Rodríguez', 'Gómez', 2, 3, '1996-06-10', 1.85, 80, '345678901'),
    (15, 'Pablo', 'Fernández', 'Sánchez', 2, 4, '1992-11-05', 1.77, 74, '456789012'),
    (16, 'Andrés', 'López', 'Pérez', 2, 5, '1995-08-30', 1.83, 79, '567890123'),
    (17, 'Miguel Ángel', 'Gómez', 'Martínez', 2, 6, '1997-03-25', 1.76, 72, '678901234'),
    (18, 'Diego', 'Martínez', 'Hernández', 2, 7, '1991-12-20', 1.80, 76, '789012345'),
    (19, 'Rafael', 'Pérez', 'Rodríguez', 2, 8, '1990-07-15', 1.78, 73, '890123456'),
    (20, 'Fernando', 'Sánchez', 'Fernández', 2, 9, '1998-02-10', 1.81, 78, '901234567'),
    (21, 'Alberto', 'Martínez', 'Gómez', 2, 10, '1999-01-05', 1.79, 75, '012345678'),
    (22, 'Roberto', 'Fernández', 'López', 2, 11, '1993-05-28', 1.84, 81, '987654321');
    
    
-- Jugadores para el equipo ID 3 (Club Deportivo Los Tigres)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (23, 'Gabriel', 'García', 'Hernández', 3, 1, '1995-03-12', 1.80, 75, '123456789'),
    (24, 'Manuel', 'Hernández', 'López', 3, 2, '1994-08-18', 1.76, 73, '234567890'),
    (25, 'Javier', 'López', 'Gómez', 3, 3, '1993-12-25', 1.78, 74, '345678901'),
    (26, 'David', 'Gómez', 'Martínez', 3, 4, '1992-10-05', 1.85, 80, '456789012'),
    (27, 'Pedro', 'Martínez', 'Rodríguez', 3, 5, '1991-07-20', 1.79, 76, '567890123'),
    (28, 'José', 'Rodríguez', 'Sánchez', 3, 6, '1990-05-15', 1.82, 78, '678901234'),
    (29, 'Daniel', 'Sánchez', 'Fernández', 3, 7, '1996-02-28', 1.77, 72, '789012345'),
    (30, 'Antonio', 'Fernández', 'Pérez', 3, 8, '1998-09-10', 1.81, 77, '890123456'),
    (31, 'Ángel', 'Pérez', 'López', 3, 9, '1997-06-05', 1.83, 79, '901234567'),
    (32, 'Carlos', 'López', 'Hernández', 3, 10, '1999-04-30', 1.76, 73, '012345678'),
    (33, 'Juan', 'Hernández', 'Martínez', 3, 11, '1993-11-22', 1.84, 81, '987654321');
    
    
-- Jugadores para el equipo ID 4 (Club Atlético Los Toros)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (34, 'Miguel', 'González', 'López', 4, 1, '1994-05-18', 1.79, 76, '234567890'),
    (35, 'Luis', 'López', 'García', 4, 2, '1995-08-22', 1.83, 79, '345678901'),
    (36, 'Fernando', 'García', 'Martínez', 4, 3, '1996-11-25', 1.81, 78, '456789012'),
    (37, 'Diego', 'Martínez', 'Sánchez', 4, 4, '1993-02-28', 1.84, 80, '567890123'),
    (38, 'Pablo', 'Sánchez', 'Pérez', 4, 5, '1992-03-15', 1.77, 75, '678901234'),
    (39, 'Jorge', 'Pérez', 'Gómez', 4, 6, '1991-07-10', 1.82, 77, '789012345'),
    (40, 'Manuel', 'Gómez', 'Rodríguez', 4, 7, '1990-09-12', 1.78, 74, '890123456'),
    (41, 'Francisco', 'Rodríguez', 'Fernández', 4, 8, '1997-12-20', 1.85, 82, '901234567'),
    (42, 'José', 'Fernández', 'Hernández', 4, 9, '1998-04-28', 1.80, 76, '012345678'),
    (43, 'Carlos', 'Hernández', 'González', 4, 10, '1999-10-05', 1.76, 73, '098765432'),
    (44, 'Javier', 'González', 'López', 4, 11, '1993-06-08', 1.79, 77, '987654321');    

-- Jugadores para el equipo ID 5 (Club Atlético Los Toros)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (45, 'Sergio', 'García', 'Martínez', 5, 1, '1995-08-17', 1.80, 75, '123456789'),
    (46, 'Antonio', 'Martínez', 'Gómez', 5, 2, '1994-11-29', 1.82, 78, '234567890'),
    (47, 'Daniel', 'Gómez', 'Hernández', 5, 3, '1993-04-12', 1.79, 77, '345678901'),
    (48, 'Manuel', 'Hernández', 'Martínez', 5, 4, '1992-07-24', 1.76, 74, '456789012'),
    (49, 'Francisco', 'Martínez', 'García', 5, 5, '1991-10-06', 1.81, 80, '567890123'),
    (50, 'Luis', 'García', 'Hernández', 5, 6, '1990-01-18', 1.84, 79, '678901234'),
    (51, 'Javier', 'Hernández', 'Gómez', 5, 7, '1989-03-02', 1.77, 76, '789012345'),
    (52, 'Pablo', 'Gómez', 'Martínez', 5, 8, '1998-05-14', 1.83, 78, '890123456'),
    (53, 'José', 'Martínez', 'García', 5, 9, '1997-09-26', 1.85, 82, '901234567'),
    (54, 'Carlos', 'García', 'Hernández', 5, 10, '1996-12-08', 1.78, 77, '012345678'),
    (55, 'Juan', 'Hernández', 'Martínez', 5, 11, '1999-02-20', 1.80, 75, '987654321');


-- Jugadores para el equipo ID 6 (Club Deportivo Los Lobos)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (56, 'Miguel', 'Gómez', 'Hernández', 6, 1, '1995-06-23', 1.78, 77, '123456789'),
    (57, 'Jorge', 'Hernández', 'Gómez', 6, 2, '1994-09-15', 1.82, 79, '234567890'),
    (58, 'Rafael', 'Gómez', 'Martínez', 6, 3, '1993-12-07', 1.75, 75, '345678901'),
    (59, 'David', 'Martínez', 'Hernández', 6, 4, '1992-03-30', 1.80, 78, '456789012'),
    (60, 'Roberto', 'Martínez', 'Gómez', 6, 5, '1991-06-21', 1.85, 82, '567890123'),
    (61, 'Alberto', 'Hernández', 'Martínez', 6, 6, '1990-09-13', 1.79, 76, '678901234'),
    (62, 'Santiago', 'Martínez', 'Hernández', 6, 7, '1989-12-05', 1.83, 80, '789012345'),
    (63, 'Ángel', 'Gómez', 'Hernández', 6, 8, '1998-02-26', 1.76, 74, '890123456'),
    (64, 'Fernando', 'Gómez', 'Martínez', 6, 9, '1997-05-20', 1.81, 78, '901234567'),
    (65, 'Mario', 'Martínez', 'Gómez', 6, 10, '1996-08-12', 1.77, 75, '012345678'),
    (66, 'Diego', 'Hernández', 'Gómez', 6, 11, '1999-11-04', 1.84, 81, '987654321');
    
    -- Jugadores para el equipo ID 7 (Club Atlético Los Halcones)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (67, 'Luis', 'Pérez', 'Gómez', 7, 1, '1995-06-23', 1.78, 77, '123456789'),
    (68, 'Carlos', 'Gómez', 'Hernández', 7, 2, '1994-09-15', 1.82, 79, '234567890'),
    (69, 'Manuel', 'Hernández', 'Gómez', 7, 3, '1993-12-07', 1.75, 75, '345678901'),
    (70, 'José', 'Gómez', 'Martínez', 7, 4, '1992-03-30', 1.80, 78, '456789012'),
    (71, 'Juan', 'Martínez', 'Hernández', 7, 5, '1991-06-21', 1.85, 82, '567890123'),
    (72, 'Miguel', 'Martínez', 'Gómez', 7, 6, '1990-09-13', 1.79, 76, '678901234'),
    (73, 'Javier', 'Hernández', 'Martínez', 7, 7, '1989-12-05', 1.83, 80, '789012345'),
    (74, 'Pablo', 'Gómez', 'Hernández', 7, 8, '1998-02-26', 1.76, 74, '890123456'),
    (75, 'Sergio', 'Gómez', 'Martínez', 7, 9, '1997-05-20', 1.81, 78, '901234567'),
    (76, 'Andrés', 'Martínez', 'Gómez', 7, 10, '1996-08-12', 1.77, 75, '012345678'),
    (77, 'Paco', 'Hernández', 'Gómez', 7, 11, '1999-11-04', 1.84, 81, '987654321');
    
    -- Jugadores para el equipo ID 8 (Club Deportivo Los Canguros)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (78, 'David', 'García', 'Martínez', 8, 1, '1994-08-10', 1.75, 75, '123456789'),
    (79, 'Laura', 'Martínez', 'Gómez', 8, 2, '1993-11-02', 1.70, 70, '234567890'),
    (80, 'Ana', 'Gómez', 'Hernández', 8, 3, '1992-02-25', 1.78, 78, '345678901'),
    (81, 'Javier', 'Hernández', 'Martínez', 8, 4, '1991-05-19', 1.80, 80, '456789012'),
    (82, 'Sara', 'Martínez', 'Gómez', 8, 5, '1990-08-12', 1.73, 73, '567890123'),
    (83, 'Pedro', 'Gómez', 'Hernández', 8, 6, '1989-11-04', 1.76, 76, '678901234'),
    (84, 'Elena', 'Hernández', 'Martínez', 8, 7, '1988-01-27', 1.79, 79, '789012345'),
    (85, 'Marta', 'Martínez', 'Gómez', 8, 8, '1998-04-21', 1.72, 72, '890123456'),
    (86, 'Juan', 'Gómez', 'Hernández', 8, 9, '1997-07-15', 1.77, 77, '901234567'),
    (87, 'Luis', 'Hernández', 'Martínez', 8, 10, '1996-10-08', 1.74, 74, '012345678'),
    (88, 'María', 'Martínez', 'Gómez', 8, 11, '1995-12-31', 1.81, 81, '987654321');

-- Jugadores para el equipo ID 9 (Club Atlético Los Osos)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (89, 'Roberto', 'García', 'Martínez', 9, 1, '1994-08-10', 1.75, 75, '123456789'),
    (90, 'Lucía', 'Martínez', 'Gómez', 9, 2, '1993-11-02', 1.70, 70, '234567890'),
    (91, 'Javier', 'Gómez', 'Hernández', 9, 3, '1992-02-25', 1.78, 78, '345678901'),
    (92, 'Sara', 'Hernández', 'Martínez', 9, 4, '1991-05-19', 1.80, 80, '456789012'),
    (93, 'Pedro', 'Martínez', 'Gómez', 9, 5, '1990-08-12', 1.73, 73, '567890123'),
    (94, 'Elena', 'Gómez', 'Hernández', 9, 6, '1989-11-04', 1.76, 76, '678901234'),
    (95, 'Marta', 'Hernández', 'Martínez', 9, 7, '1988-01-27', 1.79, 79, '789012345'),
    (96, 'Juan', 'Martínez', 'Gómez', 9, 8, '1998-04-21', 1.72, 72, '890123456'),
    (97, 'Laura', 'Gómez', 'Hernández', 9, 9, '1997-07-15', 1.77, 77, '901234567'),
    (98, 'Carlos', 'Hernández', 'Martínez', 9, 10, '1996-10-08', 1.74, 74, '012345678'),
    (99, 'María', 'Hernández', 'Gómez', 9, 11, '1995-12-31', 1.81, 81, '987654321');
    
-- Jugadores para el equipo ID 10 (Club Deportivo Los Lobos Marinos)
INSERT INTO jugadores (id_jugador, nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono)
VALUES
    (100, 'Diego', 'López', 'García', 10, 1, '1990-01-15', 1.80, 75, '123456789'),
    (101, 'Marta', 'García', 'Fernández', 10, 2, '1991-02-20', 1.75, 68, '234567890'),
    (102, 'Pedro', 'Fernández', 'López', 10, 3, '1992-03-25', 1.85, 80, '345678901'),
    (103, 'Elena', 'López', 'García', 10, 4, '1993-04-30', 1.78, 72, '456789012'),
    (104, 'Juan', 'García', 'Fernández', 10, 5, '1994-05-05', 1.82, 77, '567890123'),
    (105, 'Ana', 'Fernández', 'López', 10, 6, '1995-06-10', 1.79, 73, '678901234'),
    (106, 'José', 'López', 'García', 10, 7, '1996-07-15', 1.83, 78, '789012345'),
    (107, 'Laura', 'García', 'Fernández', 10, 8, '1997-08-20', 1.76, 70, '890123456'),
    (108, 'Carlos', 'Fernández', 'López', 10, 9, '1998-09-25', 1.81, 76, '901234567'),
    (109, 'Sara', 'López', 'García', 10, 10, '1999-10-30', 1.77, 74, '012345678'),
    (110, 'Daniel', 'García', 'Fernández', 10, 11, '2000-11-04', 1.80, 75, '987654321');


