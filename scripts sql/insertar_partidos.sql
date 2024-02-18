-- Partidos de fútbol
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
    (1, '2024-02-20 14:00:00', 1, 1, 2, 0, 0, 'Partido amistoso'),
    (1, '2024-02-20 16:00:00', 2, 3, 4, 0, 0, 'Partido de liga');

-- Partidos de baloncesto
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
    (2, '2024-02-21 15:00:00', 3, 11, 12, 0, 0, 'Torneo local'),
    (2, '2024-02-21 17:00:00', 4, 13, 14, 0, 0, 'Copa nacional');

-- Partidos de tenis
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_equipo_local, id_equipo_visitante, puntos_local, puntos_visitante, observaciones)
VALUES
    (3, '2024-02-22 12:00:00', 5, 21, 22, 0, 0, 'Partido de exhibición'),
    (3, '2024-02-22 14:00:00', 6, 23, 24, 0, 0, 'Torneo regional');

-- Partidos de fútbol
UPDATE partidos SET puntos_local = 3, puntos_visitante = 2 WHERE id_partido = 1;
UPDATE partidos SET puntos_local = 1, puntos_visitante = 0 WHERE id_partido = 2;

-- Partidos de baloncesto
UPDATE partidos SET puntos_local = 80, puntos_visitante = 76 WHERE id_partido = 3;
UPDATE partidos SET puntos_local = 95, puntos_visitante = 92 WHERE id_partido = 4;

-- Partidos de tenis
UPDATE partidos SET puntos_local = 2, puntos_visitante = 0 WHERE id_partido = 5;
UPDATE partidos SET puntos_local = 6, puntos_visitante = 4 WHERE id_partido = 6;
