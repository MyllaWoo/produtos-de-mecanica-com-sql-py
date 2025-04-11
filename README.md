# 🛠️ Sistema de Gerenciamento de Produtos - Oficina Mecânica

## 📌 Introdução

Este projeto foi desenvolvido como parte de uma atividade prática da disciplina de Programação com Banco de Dados. Seu objetivo é criar um sistema funcional em Python que permita o gerenciamento de produtos em uma oficina mecânica por meio de um banco de dados SQLite. As operações realizadas incluem adicionar, listar, buscar, atualizar e deletar produtos, de forma simples e direta via terminal.

---

## 🗃️ Estrutura do Banco de Dados

O banco de dados utilizado é o `produtos.db`, criado a partir de um script SQL. A tabela principal é:

### Tabela: `produtos`

| Campo     | Tipo      | Descrição                          |
|-----------|-----------|------------------------------------|
| `id`      | INTEGER   | Identificador único (Primary Key)  |
| `nome`    | TEXT      | Nome do produto                    |
| `categoria` | TEXT    | Categoria do produto (ex: Freio, Motor, Elétrica) |
| `preco`   | REAL      | Preço unitário do produto          |
| `estoque` | INTEGER   | Quantidade disponível em estoque   |

---

## 🖥️ Capturas de Tela
Abaixo estão exemplos de funcionamento do código no terminal:

- Tela do menu principal
 ![Menu](https://github.com/user-attachments/assets/7c5956ac-43ae-4d26-9f83-c7d17dc745ae)
- Inserção de novo produto
 ![Inserção](https://github.com/user-attachments/assets/4a7d03ab-7a92-4ee2-9eef-5efd18fa9978)
- Listagem dos produtos
 ![Listagem](https://github.com/user-attachments/assets/2b131900-32ca-4415-be2f-d653069abf17)
- Busca por ID e Nome
 ![Busca por ID](https://github.com/user-attachments/assets/916de829-5bc4-4dab-a687-c70f5449d870)
 ![Busca por nome](https://github.com/user-attachments/assets/832603be-252b-425e-8c54-a6859a808c86)
- Atualização e exclusão
 ![Atualização](https://github.com/user-attachments/assets/42184f35-ce9d-47c1-9124-7fc4f8cbae30)
 ![Delete](https://github.com/user-attachments/assets/72dec4a4-80f3-4bb7-bc7d-9fd2ef88edae)

---

## 📚 Bibliotecas Utilizadas

- `sqlite3`: Biblioteca padrão do Python para interação com bancos de dados SQLite.
  - **Motivo do uso:** Permite a criação, manipulação e consulta a bancos de dados leves sem necessidade de servidor, ideal para projetos simples e portáveis.

---

## ✅ Funcionalidades Implementadas

- 📥 Adicionar novos produtos com nome, categoria, preço e estoque
- 📋 Listar todos os produtos cadastrados
- 🔍 Buscar produtos por nome ou por ID
- ✏️ Atualizar as informações de um produto existente
- 🗑️ Deletar produtos pelo ID
- ✅ Interface simples baseada em terminal com menu de opções

---

## 💡 Observações

- O projeto funciona totalmente via terminal.
- O banco de dados é criado e populado automaticamente ao rodar o script, desde que o arquivo `produtos.sql` esteja presente no mesmo diretório.
- Todos os dados são persistidos no arquivo `produtos.db`.

---

## 🚀 Execução

1. Clone o repositório
2. Certifique-se de ter Python instalado
3. Execute o script com:
```bash
python main.py
