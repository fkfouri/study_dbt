-- USE mariadb;
-- -- Using the root user, grant access to the mariadb user.
-- GRANT ALL PRIVILEGES ON * TO 'root' @'%' IDENTIFIED BY 'mariadb';

-- Tentar excluir o banco de dados, caso ele exista
-- DROP DATABASE IF EXISTS intro;

-- Criar o banco de dados
CREATE DATABASE intro;