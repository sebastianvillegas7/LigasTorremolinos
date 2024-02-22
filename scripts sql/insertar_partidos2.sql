-- Partidos de fútbol
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
(1, '2023-08-23 18:00:00', 1, 5, 6, 2, 2, 'Partido de liga'),
(1, '2024-02-24 20:00:00', 2, 7, 8, 3, 1, 'Copa nacional'),
(1, '2023-12-25 16:00:00', 1, 9, 10, 1, 0, 'Partido amistoso'),
(1, '2024-02-26 19:00:00', 10, 11, 12, 2, 3, 'Partido de liga'),
(1, '2023-06-27 21:00:00', 6, 13, 14, 0, 0, 'Partido de copa');

-- Partidos de baloncesto
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
(2, '2024-03-23 14:00:00', 4, 15, 16, 85, 78, 'Torneo regional'),
(2, '2023-07-24 16:00:00', 3, 17, 18, 100, 92, 'Partido de liga'),
(2, '2024-01-25 18:00:00', 2, 19, 20, 75, 70, 'Torneo local'),
(2, '2023-02-26 20:00:00', 8, 21, 22, 90, 86, 'Copa nacional'),
(2, '2024-01-27 22:00:00', 5, 23, 24, 110, 105, 'Partido amistoso');

-- Partidos de tenis
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
(3, '2023-01-23 10:00:00', 4, 25, 26, 2, 1, 'Torneo local'),
(3, '2023-11-24 12:00:00', 1, 27, 28, 6, 3, 'Partido de exhibición'),
(3, '2023-05-25 14:00:00', 10, 29, 30, 7, 5, 'Copa nacional'),
(3, '2024-01-26 16:00:00', 9, 31, 32, 4, 2, 'Partido de liga'),
(3, '2024-04-27 18:00:00', 2, 33, 34, 3, 6, 'Torneo regional');