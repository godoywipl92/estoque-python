import sqlite3

def conectar():
    return sqlite3.connect("estoque.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def criar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
    except ValueError:
        print("Erro: quantidade e preço devem ser números.")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)", (nome, quantidade, preco))
        conn.commit()
        print("Produto cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: nome duplicado.")
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    if produtos:
        for prod in produtos:
            print(f"ID: {prod[0]} | Nome: {prod[1]} | Quantidade: {prod[2]} | Preço: R${prod[3]:.2f}")
    else:
        print("Nenhum produto encontrado.")

def atualizar_produto():
    try:
        id = int(input("ID do produto: "))
        nova_quantidade = int(input("Nova quantidade: "))
        novo_preco = float(input("Novo preço: "))
    except ValueError:
        print("Erro: entrada inválida.")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?", (nova_quantidade, novo_preco, id))
    if cursor.rowcount == 0:
        print("Erro: produto não encontrado.")
    else:
        print("Produto atualizado com sucesso!")
    conn.commit()
    conn.close()

def deletar_produto():
    try:
        id = int(input("ID do produto a deletar: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        print("Erro: produto não encontrado.")
    else:
        print("Produto deletado com sucesso!")
    conn.commit()
    conn.close()

def menu():
    criar_tabela()
    while True:
        print("\n=== MENU ESTOQUE ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
