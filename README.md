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

## 🧩 Dificuldades encontradas e como foram resolvidas
Durante o desenvolvimento do sistema, o principal desafio foi garantir a integridade dos dados no banco SQLite, especialmente em relação à validação de entradas duplicadas e à manipulação de IDs inexistentes nas operações de atualização e exclusão. Para resolver isso, foi necessário implementar tratamento de exceções com try/except e validar os dados antes de cada operação sensível.

Outro ponto importante foi estruturar o código de forma modular, separando cada funcionalidade em funções específicas para facilitar a manutenção e a legibilidade. Essa organização permitiu um fluxo de desenvolvimento mais claro e seguro, além de tornar o código mais escalável para futuras melhorias, como interface gráfica ou integração com APIs.

---

## ✅ Como Executar

1. Instale o Python
2. Baixe o repositório
3. Execute o arquivo `estoque.py` com:

```bash
python estoque.py
