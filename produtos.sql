


-- Criar a tabela
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
);

-- Produtos de mecânica
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Chave de fenda', 'Ferramenta manual', 12.50, 50),
('Chave inglesa', 'Ferramenta manual', 25.00, 30),
('Compressor de ar', 'Equipamento', 750.00, 5),
('Macaco hidráulico', 'Equipamento', 320.00, 8),
('Multímetro digital', 'Instrumento de medição', 95.00, 12),
('Jogo de soquetes', 'Ferramenta manual', 110.00, 20),
('Pistola de pintura', 'Equipamento', 210.00, 7),
('Cabo de bateria', 'Acessório automotivo', 40.00, 25),
('Chave torque', 'Ferramenta especial', 180.00, 6),
('Alicate universal', 'Ferramenta manual', 18.00, 40),
('Chave de fenda', 'Ferramentas', 12.90, 50),
('Chave Phillips', 'Ferramentas', 13.50, 40),
('Chave inglesa', 'Ferramentas', 25.00, 30),
('Martelo de borracha', 'Ferramentas', 18.75, 20),
('Alicate universal', 'Ferramentas', 22.00, 35),
('Multímetro digital', 'Equipamentos', 89.90, 15),
('Compressor de ar', 'Máquinas', 550.00, 5),
('Macaco hidráulico', 'Equipamentos', 130.00, 10),
('Jogo de soquetes', 'Ferramentas', 75.50, 25),
('Chave catraca', 'Ferramentas', 39.99, 20),
('Graxa lubrificante', 'Lubrificantes', 14.90, 100),
('Óleo de motor 20W50', 'Lubrificantes', 39.90, 60),
('Luva de proteção', 'Segurança', 9.99, 100),
('Óculos de proteção', 'Segurança', 15.90, 75),
('Escova de aço', 'Acessórios', 11.25, 45),
('Lanterna LED recarregável', 'Equipamentos', 69.00, 20),
('Bateria automotiva 60Ah', 'Peças', 379.00, 12),
('Cabo de chupeta', 'Acessórios', 49.90, 18),
('Macacão de mecânico', 'Vestuário', 120.00, 10),
('Scanner automotivo OBD2', 'Equipamentos', 250.00, 6);