import sqlite3

#Conexão com o bando de dados
conexao = sqlite3.connect('produtos.db')
cursor = conexao.cursor()

# Lê o conteúdo do arquivo .sql e executa
with open('produtos.sql', 'r', encoding='utf-8') as arquivo_sql:
    script = arquivo_sql.read()
    cursor.executescript(script)

#Funçoes CRUD
def adicionar_produto(nome, categoria, preco, estoque):
    cursor.execute('''
        INSERT INTO produtos (nome, categoria, preco, estoque) VALUES (?, ?, ?, ?)
    ''',(nome, categoria, preco, estoque))
    conexao.commit()
    return cursor.lastrowid

def atualizar_produtos(user_id, nome, categoria, preco, estoque):
    cursor.execute('''
        UPDATE produtos SET nome = ?, categoria = ?, preco = ?, estoque = ? WHERE id = ?
    ''', (nome, categoria, preco, estoque, user_id))
    conexao.commit()
    return cursor.rowcount

def deletar_produtos(user_id):
    cursor.execute('''
        DELETE FROM produtos 
        WHERE id = ?
    ''',(user_id,))
    conexao.commit()
    return cursor.rowcount

#Recuperação e consultas
def listar_produtos():
    cursor.execute('''
        SELECT * FROM produtos
    ''')
    produtos = cursor.fetchall()
    print("\n --- Lista de Produtos ---")
    if produtos:
        for produtos in produtos:
            print(f"ID: {produtos[0]}, Nome: {produtos[1]}, Categoria: {produtos[2]}, Preço: {produtos[3]}, Estoque: {produtos[4]}")
        else:
            print("Nenhum produto encontrado")


def buscar_produtos_por_nome(nome):
    cursor.execute("SELECT *FROM produtos WHERE nome LIKE ?", ('%' + nome + '%',))
    produtos = cursor.fetchall()
    print(f"\n--- Busca por nome: '{nome}' ---")
    if produtos:
        for produtos in produtos:
            print(f"ID: {produtos[0]}, Nome: {produtos[1]}, Categoria: {produtos[2]}, Preço: {produtos[3]}, Estoque: {produtos[4]}")
    else:
        print("Nenhum produto encontrado com esse nome")


def buscar_produtos_por_id(user_id):
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (user_id,))
    produtos = cursor.fetchone()
    print(f"\n --- Busca por ID: {user_id}---")
    if produtos:
        print(f"\n ---Produto encontrado---")
        print(f"ID: {produtos[0]}, Nome: {produtos[1]}, Categoria: {produtos[2]}, Preço: {produtos[3]}, Estoque: {produtos[4]}")
    else:
        print("Produto não encontrado")

#função principal com menu de opçoes
def menu():
    while True:
        print("\n --- Menu ---")
        print("1. Adicionar Produtos")
        print("2.Listar todos os produtos")
        print("3. Buscar produto por Nome")
        print("4. Buscar produto por ID")
        print("5.Atualizar produto")
        print("6.Deletar produto")
        print("0. Sair")

        opcao = input("Digite uma opção:")

        if opcao == '1':
            nome = input("Digite o nome do produto:")
            categoria = input("Digite a categoria do produto:")
            preco = float(input("Digite o preço do produto:"))
            estoque = int(input("Digite um valor para identificar a quantidade no estoque:"))
            user_id = adicionar_produto(nome, categoria, preco, estoque)
            print(f"Produto adicionado com id: {user_id}")

        elif opcao == '2':
            listar_produtos()

        elif opcao == '3':
            nome = input("Digite o nome do produto à buscar:")
            buscar_produtos_por_nome(nome)

        elif opcao == '4':
            user_id = int(input("Digite o ID do produto à buscar:"))
            buscar_produtos_por_id(user_id)

        elif opcao == '5':
            user_id = int(input("Digite o ID do produto para atualizar:"))
            nome = input("Diigite o novo nome do produto:")
            categoria = input("Digite a nova categoria do produto:")
            preco = float(input("Digite o novo valor do produto:"))
            estoque = int(input("Digite a nova quantidade no estoque:"))
            rows_updated = atualizar_produtos(user_id, nome, categoria, preco, estoque)
            if rows_updated:
                print(f"Produto com ID {user_id} atualizado com sucesso!")
            else:
                print(f"Nenhum produto encontrado com o ID {user_id}.")

        elif opcao == '6':
            user_id = int(input("Digite o ID do produto à deletar:"))
            rows_deleted = deletar_produtos(user_id)
            if rows_deleted:
                print(f"Produto com ID {user_id} deletado com sucesso!")
            else:
                print(f"Produto com o ID {user_id} não foi encontardo.")
        
        elif opcao == '0':
            print("Saiu do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    menu()
    conexao.close()