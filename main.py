# criado pelo claude
'''import json
import os
from datetime import datetime

class ControleEstoque:
    def __init__(self, arquivo_estoque='estoque.json'):
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        """Carrega o estoque do arquivo JSON ou cria um novo se não existir."""
        try:
            if os.path.exists(self.arquivo_estoque):
                with open(self.arquivo_estoque, 'r', encoding='utf-8') as arquivo:
                    return json.load(arquivo)
            else:
                # Estoque inicial pré-definido
                estoque_inicial = {
                    "Camiseta": {"quantidade": 50, "preco": 29.90},
                    "Calça Jeans": {"quantidade": 30, "preco": 89.90},
                    "Tênis": {"quantidade": 20, "preco": 199.90}
                }
                
                # Salva o estoque inicial
                with open(self.arquivo_estoque, 'w', encoding='utf-8') as arquivo:
                    json.dump(estoque_inicial, arquivo, indent=4, ensure_ascii=False)
                
                return estoque_inicial
        except Exception as e:
            print(f"Erro ao carregar estoque: {e}")
            return {}

    def salvar_estoque(self):
        """Salva o estoque atualizado no arquivo JSON."""
        try:
            with open(self.arquivo_estoque, 'w', encoding='utf-8') as arquivo:
                json.dump(self.estoque, arquivo, indent=4, ensure_ascii=False)
            print("Estoque salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar estoque: {e}")

    def adicionar_produto(self, nome, quantidade, preco):
        """Adiciona um novo produto ao estoque."""
        if nome in self.estoque:
            print(f"Produto {nome} já existe. Use atualizar quantidade para modificar.")
            return False
        
        self.estoque[nome] = {
            'quantidade': quantidade,
            'preco': preco
        }
        self.salvar_estoque()
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    def realizar_venda(self, nome, quantidade_vendida):
        """Realiza uma venda, atualizando o estoque."""
        # Debug: Imprimir estoque atual antes da venda
        print(f"\nEstoque antes da venda:\n{json.dumps(self.estoque, indent=2)}")
        
        if nome not in self.estoque:
            print(f"Produto {nome} não encontrado no estoque.")
            return False
        
        if self.estoque[nome]['quantidade'] < quantidade_vendida:
            print(f"Estoque insuficiente de {nome}.")
            return False
        
        # Atualiza a quantidade em estoque
        self.estoque[nome]['quantidade'] -= quantidade_vendida
        
        # Calcula o valor total da venda
        valor_venda = self.estoque[nome]['preco'] * quantidade_vendida
        
        # Salva o estoque imediatamente após a venda
        self.salvar_estoque()
        
        # Debug: Imprimir estoque após a venda
        print(f"\nEstoque após a venda:\n{json.dumps(self.estoque, indent=2)}")
        
        print(f"Venda realizada: {quantidade_vendida} {nome}(s). Valor total: R${valor_venda:.2f}")
        return True

    def exibir_estoque(self):
        """Exibe todo o estoque atual."""
        if not self.estoque:
            print("Estoque vazio.")
            return
        
        print("\n--- ESTOQUE ATUAL ---")
        for produto, detalhes in self.estoque.items():
            print(f"Produto: {produto}")
            print(f"Quantidade: {detalhes['quantidade']}")
            print(f"Preço: R${detalhes['preco']:.2f}")
            print("---")

def menu_vendedor():
    """Interface interativa para o vendedor."""
    controle = ControleEstoque()
    
    while True:
        print("\n--- SISTEMA DE VENDAS ---")
        print("1. Exibir Estoque")
        print("2. Realizar Venda")
        print("3. Adicionar Novo Produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            controle.exibir_estoque()
        
        elif opcao == '2':
            # Exibe estoque antes da venda
            controle.exibir_estoque()
            
            # Solicita detalhes da venda
            nome_produto = input("Digite o nome do produto: ")
            
            try:
                quantidade = int(input("Digite a quantidade vendida: "))
                
                # Tenta realizar a venda
                if controle.realizar_venda(nome_produto, quantidade):
                    print("\nVenda concluída com sucesso!")
                    
                    # Pergunta se deseja continuar
                    continuar = input("Deseja realizar outra venda? (s/n): ").lower()
                    if continuar != 's':
                        break
            
            except ValueError:
                print("Quantidade inválida. Por favor, digite um número.")
        
        elif opcao == '3':
            # Adicionar novo produto
            nome = input("Digite o nome do novo produto: ")
            
            try:
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade inicial em estoque: "))
                
                controle.adicionar_produto(nome, quantidade, preco)
            
            except ValueError:
                print("Valores inválidos. Não foi possível adicionar o produto.")
        
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def main():
    menu_vendedor()

if __name__ == "__main__":
    main()'''

#criado com chat black box
'''import json

def carregar_estoque():
    with open('estoque2.json', 'r') as file:
        return json.load(file)

def salvar_estoque(estoque):
    with open('estoque2.json', 'w') as file:
        json.dump(estoque, file, indent=4)

def listar_produtos(estoque):
    print("Estoque Atual:")
    for produto in estoque['produtos']:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']}")

def realizar_venda(estoque, id_produto, quantidade_vendida):
    for produto in estoque['produtos']:
        if produto['id'] == id_produto:
            if produto['quantidade'] >= quantidade_vendida:
                produto['quantidade'] -= quantidade_vendida
                print(f"Venda realizada: {quantidade_vendida} unidades de {produto['nome']}.")
                return
            else:
                print("Quantidade insuficiente em estoque.")
                return
    print("Produto não encontrado.")

def main():
    estoque = carregar_estoque()
    
    while True:
        listar_produtos(estoque)
        id_produto = int(input("Digite o ID do produto que deseja vender (ou 0 para sair): "))
        if id_produto == 0:
            break
        quantidade_vendida = int(input("Digite a quantidade a ser vendida: "))
        
        realizar_venda(estoque, id_produto, quantidade_vendida)
        salvar_estoque(estoque)

if __name__ == "__main__":
    main()'''
import json

# Função para carregar o estoque de um arquivo JSON
def carregar_estoque(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar o estoque em um arquivo JSON
def salvar_estoque(estoque, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

# Função para adicionar um item ao estoque
def adicionar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

# Função para registrar uma venda e atualizar o estoque
def registrar_venda(estoque, nome, quantidade):
    if nome in estoque and estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        print(f"Venda registrada: {quantidade} unidades de {nome}")
    else:
        print(f"Estoque insuficiente para {nome} ou item não encontrado")

# Função para exibir o menu e interagir com o usuário
def menu():
    arquivo_estoque = 'estoque.json'
    estoque = carregar_estoque(arquivo_estoque)

    while True:
        print("\nControle de Estoque")
        print("1. Adicionar item ao estoque")
        print("2. Registrar venda")
        print("3. Ver estoque")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(estoque, nome, quantidade)
            salvar_estoque(estoque, arquivo_estoque)
            print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")
        elif escolha == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            registrar_venda(estoque, nome, quantidade)
            salvar_estoque(estoque, arquivo_estoque)
        elif escolha == '3':
            print("Estoque atual:")
            print(json.dumps(estoque, indent=4))
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()



