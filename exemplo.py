# Importa o módulo e todas as suas dependências 
from ArvoreBinaria import ArvoreBinaria

def teste1(): 
    """Teste 1: Cria uma árvore e imprime para o usuário 
    """

    # Cria a árvore binária 
    a = ArvoreBinaria.ArvoreBinaria() 

    # Adiciona seus nós
    for i in range(0, 9): 
        a.add_node(i)

    # Imprime num arquivo .png para o usuário a árvore gerada
    a.print_tree()

def teste2():
    """Teste 2: Cria uma árvore, transforma ela num max-heap e a imprime para o usuário 
    """

    # Cria a árvore binária 
    b = ArvoreBinaria.ArvoreBinaria()

    # Adiciona seus nós 
    for i in range(0, 12): 
        b.add_node(i)

    # Transforma a árvore num max-heap 
    b.build_max_heap()

    # Imprime num arquivo .png para o usuário a árvore gerada 
    b.print_tree()

# Execute as funções para obter os testes! 