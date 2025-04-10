🧮 Sistema de Gerenciamento de Estoque (Python + SQLite)
Este projeto é um sistema simples de gerenciamento de estoque feito em Python, utilizando banco de dados SQLite. Ele permite realizar operações básicas como adicionar, listar, atualizar e excluir produtos, tudo por meio de um menu interativo no terminal.

🚀 Funcionalidades
📦 Adicionar produto ao estoque

📋 Listar todos os produtos cadastrados

✏️ Atualizar informações de um produto

❌ Deletar um produto

💾 Banco de dados criado automaticamente (SQLite)

🔐 Tratamento de erros para entradas inválidas e IDs inexistentes

🧩 Código modularizado com funções separadas para cada operação

🧩 Dificuldades encontradas e como foram resolvidas
Durante o desenvolvimento do sistema, o principal desafio foi garantir a integridade dos dados no banco SQLite, especialmente em relação à validação de entradas duplicadas e à manipulação de IDs inexistentes nas operações de atualização e exclusão. Para resolver isso, foi necessário implementar tratamento de exceções com try/except e validar os dados antes de cada operação sensível.

Outro ponto importante foi estruturar o código de forma modular, separando cada funcionalidade em funções específicas para facilitar a manutenção e a legibilidade. Essa organização permitiu um fluxo de desenvolvimento mais claro e seguro, além de tornar o código mais escalável para futuras melhorias, como interface gráfica ou integração com APIs.

🧪 Exemplos de testes realizados
✅ Adição de produto
Entrada:

makefile
Copiar
Editar
Nome: Caneta  
Preço: 2.50  
Quantidade: 100  
Resultado:
Produto adicionado com sucesso e armazenado no banco de dados.

📋 Listagem de produtos
Resultado esperado:

yaml
Copiar
Editar
ID: 1 | Nome: Caneta | Preço: R$ 2.5 | Quantidade: 100
✏️ Atualização de produto
Entrada:

yaml
Copiar
Editar
ID: 1  
Novo nome: Caneta Azul  
Novo preço: 3.00  
Nova quantidade: 150  
Resultado:
Produto atualizado corretamente no banco de dados.

❌ Exclusão de produto
Entrada:

makefile
Copiar
Editar
ID: 1  
Resultado:
Produto deletado com sucesso.

