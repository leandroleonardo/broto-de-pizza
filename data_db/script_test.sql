CREATE DATABASE brotodepizza;

USE brotodepizza;

CREATE TABLE USUARIOS(
	id_usuario int not null primary key auto_increment,
    login varchar(255),
    senha blob
);

CREATE TABLE PIZZAS(
	id_pizza int not null primary key auto_increment,
    grupo varchar(25),
	nome varchar(100),
	ingredientes varchar(250),
	preco float
);

CREATE TABLE CLIENTES(
	id_cliente int not null primary key auto_increment,
	nome varchar(100),
	endereco varchar(250),
	telefone varchar(25)
);

CREATE TABLE ENCOMENDAS(
    id_encomenda int not null primary key auto_increment,
    id_cliente int,
    id_pizza int,

    data_entrega date,
    combo int,

    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
    FOREIGN KEY (id_pizza) REFERENCES PIZZAS(id_pizza)
);

SELECT SUM(PR.preco) FROM ENCOMENDAS E INNER JOIN PIZZAS PR ON PR.id_pizza = E.id_pizza;

SELECT *
from encomendas;

/* Insert usuários */

INSERT INTO USUARIOS (login, senha) VALUES ('admin', AES_ENCRYPT('admin','chave-aleatoria'));

/* Insert Pizzas */

INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Calabresa','Mussarela,Calabresa,azeitona e Órenago','Salgada', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Mussarela','Mussarela,azeitona e Órenago','Salgada', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Milho verde','Mussarela,Milho verde,azeitona e Órenago','Salgada', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Frango','Mussarela,Frango,azeitona e Órenago','Salgada', 7.00);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('3 Queijos','Mussarela,Calabresa,azeitona e Órenago','Salgada', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Calabresa e bacon','Mussarela,Requeijão,Gorgonzola,Azeitona e Óregano','Salgada', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Atum','Mussarela,Atum,azeitona e Órenago','Salgada', 7.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Frango cremoso','Mussarela,Requeijão,Frango,azeitona e Órenago','Salgada', 7.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Romeu e Julieta','Mussarela,Goiabada','Doce', 6.50);
INSERT INTO Pizzas(nome, ingredientes, grupo, preco) VALUES ('Brigadeiro','Brigadeiro,Granulado','Doce', 6.50);

/* Insert usuários */

INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Leonardo L','-','33563453');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Rafael M','-','34658710');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Amanda F','-','33563453');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Joao Silva','-','35421327');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Guilherme','-','34658710');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Mateus L','-','35421324');