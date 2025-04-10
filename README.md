# 📦 Sistema de Gerenciamento de Estoque

Este é um projeto simples de gerenciamento de estoque feito em **Python** com uso de **SQLite3** para armazenamento dos dados.

## 🧠 Funcionalidades

- Adicionar produtos ao estoque
- Listar todos os produtos
- Atualizar informações de um produto
- Remover produtos do estoque
- Armazenamento persistente via banco de dados SQLite
- Menu interativo com repetição até o usuário decidir sair
- Tratamento de erros (ID inexistente, nomes duplicados, etc.)

## 🗂 Estrutura do Projeto

- `estoque.py`: Arquivo principal com todas as funções e menu interativo
- `estoque.db`: Banco de dados gerado automaticamente na primeira execução
- `README.md`: Este documento com explicações e instruções

## 🧪 Exemplos de Testes Realizados

1. **Adição de produto:**
   - Nome: Teclado, Quantidade: 5, Preço: 49.90
   - Resultado: Produto adicionado com sucesso

2. **Listagem:**
   - Mostra todos os produtos adicionados com ID, nome, quantidade e preço

3. **Atualização de produto:**
   - Produto ID 1 alterado para: Nome: Teclado Gamer, Quantidade: 10, Preço: 89.90
   - Resultado: Produto atualizado com sucesso

4. **Remoção de produto:**
   - Remoção do produto com ID 1
   - Resultado: Produto removido com sucesso

5. **Erros tratados:**
   - Tentativa de excluir ID inexistente: mostra mensagem de erro
   - Tentativa de adicionar produto com nome já existente: impede duplicata

## 🧩 Dificuldades e Soluções

- **Erro com nome duplicado:** Resolvido com verificação antes do `INSERT`.
- **Exclusão de ID inexistente:** Adicionada verificação para garantir que o ID exista.
- **Uso do Git e GitHub:** Inicialmente, houve dificuldade com o repositório e permissões. Resolvido com uso do Git Bash e orientação passo a passo.

---

## ✅ Como Executar

1. Instale o Python
2. Baixe o repositório
3. Execute o arquivo `estoque.py` com:

```bash
python estoque.py
