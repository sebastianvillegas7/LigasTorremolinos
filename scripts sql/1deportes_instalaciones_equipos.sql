INSERT INTO deportes (id_deporte, nombre) VALUES (1, 'Fútbol'), (2, 'Baloncesto'), (3, 'Tenis');


INSERT INTO instalaciones (id_instalacion, nombre, direccion, iluminacion, cubierta) VALUES
    (1, 'Club Deportivo Los Robles', 'Calle de los Robles, 123', 1, 0),
    (2, 'Polideportivo El Pinar', 'Avenida del Pinar, 45', 1, 1),
    (3, 'Centro Deportivo La Palmera', 'Calle Palmera, 67', 0, 1),
    (4, 'Complejo Deportivo Las Acacias', 'Calle de las Acacias, 89', 1, 0),
    (5, 'Club Deportivo Los Almendros', 'Avenida de los Almendros, 12', 0, 0),
    (6, 'Polideportivo Los Olivos', 'Calle de los Olivos, 34', 1, 1),
    (7, 'Centro Deportivo Las Flores', 'Avenida de las Flores, 56', 1, 1),
    (8, 'Complejo Deportivo El Bosque', 'Calle del Bosque, 78', 0, 0),
    (9, 'Club Deportivo Los Cerezos', 'Avenida de los Cerezos, 90', 1, 0),
    (10, 'Polideportivo La Laguna', 'Calle de la Laguna, 112', 1, 1);

-- Equipos de fútbol
INSERT INTO equipos (id_equipo, nombre, id_deporte, equipacion_principal, equipacion_suplente, contacto, telefono, email) VALUES
    (1, 'Club Deportivo Los Leones', 1, 'Camiseta rayada azul y blanco', 'Camiseta blanca', 'Juan Pérez', '123456789', 'clubdeportivo@example.com'),
    (2, 'Club Atlético Las Águilas', 1, 'Camiseta a rayas rojas y blancas', 'Camiseta roja', 'Ana Gómez', '987654321', 'clubdeportivo@example.com'),
    (3, 'Club Deportivo Los Tigres', 1, 'Camiseta a rayas amarillas y negras', 'Camiseta amarilla', 'Pedro Rodríguez', '456789123', 'clubdeportivo@example.com'),
    (4, 'Club Atlético Los Toros', 1, 'Camiseta a rayas verdes y blancas', 'Camiseta verde', 'María López', '789123456', 'clubdeportivo@example.com'),
    (5, 'Club Deportivo Los Lobos', 1, 'Camiseta a rayas blancas y negras', 'Camiseta negra', 'Carlos Martínez', '456123789', 'clubdeportivo@example.com'),
    (6, 'Club Atlético Los Halcones', 1, 'Camiseta a rayas azules y blancas', 'Camiseta azul', 'Laura Sánchez', '321654987', 'clubdeportivo@example.com'),
    (7, 'Club Deportivo Los Canguros', 1, 'Camiseta a rayas rojas y negras', 'Camiseta roja', 'José García', '123789456', 'clubdeportivo@example.com'),
    (8, 'Club Atlético Los Osos', 1, 'Camiseta a rayas negras y blancas', 'Camiseta negra', 'Silvia Ruiz', '789456123', 'clubdeportivo@example.com'),
    (9, 'Club Deportivo Los Lobos Marinos', 1, 'Camiseta a rayas azules y negras', 'Camiseta azul', 'Roberto Hernández', '456789123', 'clubdeportivo@example.com'),
    (10, 'Club Atlético Los Delfines', 1, 'Camiseta a rayas blancas y azules', 'Camiseta blanca', 'Elena Fernández', '321987654', 'clubdeportivo@example.com');

-- Equipos de baloncesto
INSERT INTO equipos (id_equipo, nombre, id_deporte, equipacion_principal, equipacion_suplente, contacto, telefono, email) VALUES
    (11, 'Club de Baloncesto Los Titanes', 2, 'Camiseta amarilla', 'Camiseta azul', 'Miguel Ángel Pérez', '123456789', 'clubbaloncesto@example.com'),
    (12, 'Club de Baloncesto Las Águilas', 2, 'Camiseta verde', 'Camiseta roja', 'Ana María Gómez', '987654321', 'clubbaloncesto@example.com'),
    (13, 'Club de Baloncesto Los Halcones', 2, 'Camiseta roja', 'Camiseta azul', 'Pedro Antonio Rodríguez', '456789123', 'clubbaloncesto@example.com'),
    (14, 'Club de Baloncesto Los Lobos', 2, 'Camiseta azul', 'Camiseta roja', 'María José López', '789123456', 'clubbaloncesto@example.com'),
    (15, 'Club de Baloncesto Los Tigres', 2, 'Camiseta negra', 'Camiseta verde', 'Carlos Martín', '456123789', 'clubbaloncesto@example.com'),
    (16, 'Club de Baloncesto Los Canguros', 2, 'Camiseta blanca', 'Camiseta amarilla', 'Laura Sánchez', '321654987', 'clubbaloncesto@example.com'),
    (17, 'Club de Baloncesto Los Elefantes', 2, 'Camiseta naranja', 'Camiseta azul', 'José García', '123789456', 'clubbaloncesto@example.com'),
    (18, 'Club de Baloncesto Los Osos', 2, 'Camiseta roja', 'Camiseta amarilla', 'Silvia Ruiz', '789456123', 'clubbaloncesto@example.com'),
    (19, 'Club de Baloncesto Los Delfines', 2, 'Camiseta azul', 'Camiseta roja', 'Roberto Hernández', '456789123', 'clubbaloncesto@example.com'),
    (20, 'Club de Baloncesto Los Leones', 2, 'Camiseta verde', 'Camiseta amarilla', 'Elena Fernández', '321987654', 'clubbaloncesto@example.com');
    
    -- Equipos de tenis
INSERT INTO equipos (id_equipo, nombre, id_deporte, equipacion_principal, equipacion_suplente, contacto, telefono, email) VALUES
    (21, 'Club de Tenis Los Pinos', 3, 'Camiseta blanca', 'Camiseta blanca', 'Manuel Pérez', '123456789', 'clubtenis@example.com'),
    (22, 'Club de Tenis El Bosque', 3, 'Camiseta azul', 'Camiseta azul', 'María García', '987654321', 'clubtenis@example.com'),
    (23, 'Club de Tenis La Colina', 3, 'Camiseta roja', 'Camiseta roja', 'Luis López', '456789123', 'clubtenis@example.com'),
    (24, 'Club de Tenis Monte Verde', 3, 'Camiseta verde', 'Camiseta verde', 'Sara Martínez', '789123456', 'clubtenis@example.com'),
    (25, 'Club de Tenis Valle Hermoso', 3, 'Camiseta amarilla', 'Camiseta amarilla', 'Javier Rodríguez', '456123789', 'clubtenis@example.com'),
    (26, 'Club de Tenis La Cima', 3, 'Camiseta naranja', 'Camiseta naranja', 'Lucía Sánchez', '321654987', 'clubtenis@example.com');

