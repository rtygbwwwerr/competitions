import os  
from os.path import getsize, join  
import sys  
import Queue  
import networkx as nx  
import matplotlib.pyplot as plt
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydotplus
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either "
                          "PyGraphviz or PyDotPlus")
def drawStructure(file):
    
    G = nx.DiGraph()
    f = open(file)
    raws = f.readlines()
    for raw in raws:
        info = raw.split('\t')
        child = info[0]
        fathers =[]
        G.add_node(child)
        if len(info) > 1:
            fathers = info[1].split(',')
            
            for father in fathers:
                if father.strip() != '':
                    G.add_node(father)
                    G.add_edge(father, child)

        
        
    
    print("node num:%d" , G.number_of_nodes())
    print("edge num:%d" , G.number_of_edges())
    pos = graphviz_layout(G, prog='twopi', args='')
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, node_size=20, alpha=0.5, node_color="blue", with_labels=False)
    plt.axis('equal')
    plt.savefig('circular_tree.png')
    plt.show()


def drawStructure2(file):
    tree_graph = pygraphviz.AGraph(directed=True, strict=True)
    tree_graph.node_attr['style'] = 'filled'  
    tree_graph.node_attr['shape'] = 'circle'
    f = open(file)
    raws = f.readlines()
    for raw in raws:
        info = raw.split('\t')
        child = info[0]
        fathers =[]
        tree_graph.add_node(child)
        if len(info) > 1:
            fathers = info[1].split(',')
            for father in fathers:
                if father.strip() != '':
                    tree_graph.add_node(father)
                    tree_graph.add_edge(father, child)
                
    tree_graph.graph_attr['epsilon'] = '0.001'
    tree_graph.write('director_tree.dot')
    tree_graph.layout('dot')
    tree_graph.draw('director_tree.png')
    
if __name__ == '__main__':
    drawStructure("./data/topic_info.txt")
    

    #drawStructure2("./data/topic_info.txt")
    