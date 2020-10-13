CREATE TABLE IF NOT EXISTS MacroHard (
    ra INT PRIMARY KEY NOT NULL,
    nome_aluno      VARCHAR(50) UNIQUE NOT NULL,
    email           VARCHAR(50) UNIQUE NOT NULL,
    logadouro       VARCHAR(50) NULL,
    numero          VARCHAR(5) NULL,
    cep             VARCHAR(10) NULL,
    complemento     VARCHAR(20) NULL
    );
