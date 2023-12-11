# funções matemáticas 
import math
# tipagem especial 
from typing import List, Tuple
# matplotlib para plotagem do grafo 
import matplotlib.pyplot as plt
# networkx para manipulação e plotagem do grafo 
import networkx as nx
# EoN para manipulação e plotagem do grafo 
import EoN
# marcação temporal 
from time import time 

# Classe que simula uma árvore binária
class ArvoreBinaria: 
    def __init__(self) -> None:
        """Inicializa uma árvore binária vazia
        """
        # representação da árvore binária em array 
        self.arvore_array = [] 
        # variável que armazena o tamanho do heap armazenado 
        self.heap_size = 0
        # variável que armazena o pai da última folha 
        self.last_leaf_parent = math.floor(self.heap_size / 2 ) - 1

    def add_node(self, value : float) -> None: 
        """Adiciona um novo nó à árvore 

        Args:
            value (float): valor do nó
        """
        # cria uma nova instância de nó com o valor especificado na última posição da árvore (nova folha)
        node = Node(value, self.heap_size)
        # adiciona o nó criado no array que representa a árvore 
        self.arvore_array.append(node)
        # aumenta o tamanho da árvore em uma unidade
        self.heap_size = len(self.arvore_array)
        # atualiza o pai da última folha 
        self.last_leaf_parent = math.floor(self.heap_size / 2 ) - 1

    def fix_pos(self) -> None: 
        """Corrige as posições armazenadas em cada nó da árvore
        """
        for node in self.arvore_array: 
            node.pos = self.arvore_array.index(node) 

    def heapfy(self, pos : int) -> None:
        """Transforma a subárvore enraizada num dado nó "pos" num max-heap 

        Args:
            pos (int): posição do nó na árvore
        """
        # Filho da esquerda do nó 
        l = 2 * pos + 1 
        # Filho da direita do nó 
        r = 2 * pos + 2

        # Se o filho à esquerda do nó recebido estiver dentro da árvore e seu valor for maior que o de seu pai... 
        if l < self.heap_size and self.arvore_array[l].value > self.arvore_array[pos].value:
            # Marque esse filho como sendo o maior nó encontrado até agora 
            largest = l 
        else: 
            # Caso contrário, o maior nó encontrado até agora é o seu pai 
            largest = pos 

        # Se o filho à direita do nó recebido estiver dentro da árvore e seu valor for maior que o valor do maior nó encontrado... 
        if r < self.heap_size and self.arvore_array[r].value > self.arvore_array[largest].value:
            # Marque esse filho como sendo o maior nó encontrado até agora 
            largest = r
            
        # Caso o maior nó encontrado não seja o nó raiz da subárvore... 
        if largest != pos: 
            # Troque o maior nó encontrado pelo nó raiz da subárvore! 
            aux = self.arvore_array[pos]
            self.arvore_array[pos] = self.arvore_array[largest]
            self.arvore_array[largest] = aux 
            # Depois disso, aplique o algoritmo heapfy no maior nó encontrado
            self.heapfy(largest) 

 
    def build_max_heap(self) -> None: 
        """Transforma toda a árvore binária num max-heap por meio da execução sucessiva do heapfy das folhas até a raiz
        """
        # Para cada nó partindo do pai das últimas folhas até a raiz... 
        for i in range(self.last_leaf_parent, -1, -1): 
            # Aplique o algoritmo heapfy no nó escolhido
            self.heapfy(i)

    def to_array_values(self) -> List: 
        """Retorna os valores de cada nó da árvore num formato de lista

        Returns:
            List: Lista contendo os valores de todos os nós da árvore
        """

        # Forma uma lista dos valores de cada nó por meio de list comprehension 
        lista_valores = [node.value for node in self.arvore_array]

        # Retorna a lista gerada 
        return lista_valores
    
    
    def list_edges(self) -> List[Tuple]:
        """Retorna uma lista de tuplas, com cada tupla contendo dois nós que estão conectados na árvore. 
        Este método é um método auxiliar para o método print_tree(). 

        Returns:
            List[Tuple]: _description_
        """
        # Lista de conexões que será preenchida 
        edges = []

        # Execução da função auxiliar fix_pos(), organizando as posições armazenadas em cada nó
        self.fix_pos()

        # Verifica os filhos de cada nó da raiz até o último nó do penúltimo nível (antes das folhas)
        for node in self.arvore_array:
            # Essa condição serve para assegurar que as folhas não serão verificadas!
            if node.pos <= self.last_leaf_parent:
                # Caso o nó analisado possua um filho à esquerda... 
                if node.left() < self.heap_size:
                    # Adicione na lista de conexões a tupla contendo o valor do nó atual e o valor do seu filho à esquerda 
                    edges.append((node.value, self.arvore_array[node.left()].value))

                # Caso o nó analisando possua filho à direita... 
                if node.right() < self.heap_size:
                    # Adicione na lista de conexões a tupla contendo o valor do nó atual e o valor do seu filho à direita 
                    edges.append((node.value, self.arvore_array[node.right()].value))

        # Retorna a lista contendo as tuplas com as conexões da árvore 
        return edges

    
    def print_tree(self) -> None: 
        """Registra numa versão gráfica da árvore para o usuário 
        """
        
        # Cria um objeto Graph na biblioteca NetworkX
        graph = nx.Graph()

        # Povoa o objeto Graph com os nodos registrados na árvore 
        for node in self.arvore_array:
            graph.add_node(node.value)

        # Adiciona as conexões entre os nós de cada árvore de acordo com o retornado pelo método list_edges() 
        for dupla in self.list_edges():
            graph.add_edge(dupla[0], dupla[1])

        # Ajuda a posição de cada nó num formato de "hierarquia" por meio da biblioteca EoN 
        pos_nos = EoN.hierarchy_pos(graph)

        # Forma a versão gráfica da árvore 
        nx.draw(graph, pos=pos_nos, with_labels=True)

        # Registra a timestamp atual 
        timestamp = int(time())

        # Salva como .png o arquivo imagem da árvore gerado 
        plt.savefig(f"arvore_{timestamp}.png")
    
# Classe que simboliza um nó da árvore binária
class Node:
    def __init__(self, value : float, pos : int) -> None: 
        """Inicializa uma instância de um nó da árvore

        Args:
            value (float): valor do nó 
            pos (int): posição do nó na árvore 
        """
        self.value = value
        self.pos = pos

    def parent(self) -> int: 
        """Retorna a posição do nó pai 

        Returns:
            parent (int): posição do nó pai no array que representa a árvore 
        """
        
        return math.ceil(self.pos/2) - 1 
    
    def left(self) -> int: 
        """Retorna a posição do filho da esquerda do nó

        Returns:
            int: posição do filho da esquerda do nó no array que representa a árvore 
        """

        return 2 * self.pos + 1 
    
    def right(self) -> int: 
        """Retorna a posição do filho da direita do nó

        Returns:
            int: posição do filho da direita do nó no array que representa a árvore
        """

        return 2 * self.pos + 2