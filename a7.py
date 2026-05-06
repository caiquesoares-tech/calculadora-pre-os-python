# Função para aumentar o preço em 10%
def atualiza_preco(valor):
    resultado = valor * 1.10
    return resultado

# Função para calcular a taxa de 2.5% sobre o valor atualizado
def taxa(valor):
    resultado_taxa = valor * 0.025
    return resultado_taxa

# Programa Principal
def main():
    # Entrada de dados (teclado)
    preco_original = float(input("Digite o valor do produto: "))
    
    # Chamada das funções
    preco_com_aumento = atualiza_preco(preco_original)
    valor_da_taxa = taxa(preco_com_aumento)
    
    # Saída com 2 casas decimais
    print(f"Valor atualizado: R$ {preco_com_aumento:.2f}")
    print(f"Valor da taxa: R$ {valor_da_taxa:.2f}")

# Execução do programa
main()