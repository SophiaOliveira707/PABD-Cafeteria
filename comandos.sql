CREATE TABLE usuarios(
    cod_usuario int,
    nome varchar(20) not null,
    senha varchar(20) not null,
    CONSTRAINT pk_usuario PRIMARY KEY (cod_usuario)
);

CREATE TABLE produtos(
    cod_produto int,
    nome varchar(20) not null,
    preco float,
    sabor varchar(20) not null,
    tamanho varchar(20) not null,
    CONSTRAINT pk_produto PRIMARY KEY (cod_produto)
);

CREATE TABLE pagamentos(
    cod_pagamento int,
    cod_usuario int,
    cod_produto int,
    quantidade int,
    endereco varchar(50) not null,
    CONSTRAINT pk_pagamento PRIMARY KEY (cod_pagamento),
    CONSTRAINT fk_usuario FOREIGN KEY (cod_usuario) references usuarios (cod_usuario),
    CONSTRAINT fk_produto FOREIGN KEY (cod_produto) references produtos (cod_produto)
);

SELECT * FROM usuarios;
SELECT * FROM produtos;
SELECT * FROM pagamentos;

INSERT INTO usuarios (cod_usuario,nome,senha) VALUES (1,'Sophia','teste');