CREATE DATABASE IF NOT EXISTS goalfactory;
USE goalfactory;

CREATE TABLE tbl_times(
id_time INT AUTO_INCREMENT PRIMARY KEY,
nome_time VARCHAR(100) NOT NULL
);


CREATE TABLE tbl_jogadores(
id_jogador INT AUTO_INCREMENT PRIMARY KEY,
nome_jogador VARCHAR(100) NOT NULL,
time_jogador INT,
FOREIGN KEY (time_jogador) REFERENCES tbl_times(id_time)
);


CREATE TABLE tbl_partidas_realizadas(
id_partida INT AUTO_INCREMENT PRIMARY KEY,
placar_vencedor INT,
placar_perdedor INT,
time_vencedor INT,
time_perdedor INT,
FOREIGN KEY (time_vencedor) REFERENCES tbl_times(id_time),
FOREIGN KEY (time_perdedor) REFERENCES tbl_times(id_time)
);