import networkx as nx
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import make_course_edge_files as mcef

# This script generalizes previous file "node_info"

def make_graph_objects(ii_file, rr_file):
    # In: recipe_and_ingredient_file
    # Out: Graph object
    II = nx.read_edgelist(ii_file, comments='#',  delimiter=',', encoding='utf-8')
    RR = nx.read_edgelist(rr_file, comments='#',  delimiter=',', encoding='utf-8')
    return II, RR

def draw_network(II, RR, coursetype):
    # Draw network of recipie-recipe connections within a course.
    nx.draw(RR)
    plt.show()
    plt.savefig('network_of_'+ coursetype +'_recipie-recipe_connections.png')
    # Draw network of ingredient-ingredient connections within a course.
    nx.draw(II)
    plt.show()
    plt.savefig('network_of_'+ coursetype +'_ingredient-ingredient_connections.png')

def print_network_info(G, coursetype):
    # print network info for course type
    print '# edges for '+ coursetype +':', G.number_of_edges()
    print '# nodes for '+ coursetype +':', G.number_of_nodes()

def make_con_components(G, coursetype):
    # Make sorted list of connected components, largest first.
    cc_lst_name = 'cc_'+'coursetype'
    cc_lst_name = sorted(nx.connected_components(G), key = len, reverse=True)
    print cc_lst_name, len(cc_lst_name)
    print cc_lst_name[0]
    # Generate connected components as subgraphs. Answers: How many connected components are there?
    cc_sg_names = 'cc_sg_'+'coursetype'
    cc_sg_names = list(nx.connected_component_subgraphs(G))
    print cc_sg_names

def important_nodes(G, num_most_common):
    # Find the most important nodes using centrality.
    mimportant_ing = Counter(nx.degree_centrality(G)).most_common(num_most_common)
    print 'most important ingredients are ', mimportant_ing

def degrees(G):
    degree_dict = G.degree()
    print "degree_dict", degree_dict
    # degree_series = pd.Series(degree_dict)
    # degree_series.describe()
    # plt.show()
    # plt.clf()

# def jaccard():
#     ## Jaccard similarity
#     # Algorithm of the jaccard similarity is the length of the intersection divide the the length of the union.
#     G = nx.complete_graph(5)
#     preds = nx.jaccard_coefficient(G, [nodepair1, nodepair1])
#     for u, v, p in preds:
#         '(%d, %d) -> %.8f' % (u, v, p)

def do_it_all():
    coursetype = 'Desserts'
    ii_file = '../data/'+ coursetype +'_ingredient_edges.tsv'
    rr_file = '../data/'+ coursetype +'_'+ coursetype +'_edges.tsv'
    II, RR = make_graph_object(ii_file, rr_file)

if __name__ == '__main__':
    do_it_all()
