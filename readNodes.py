import networkx as nx

def read_nodes_from_file(file_path):
    graph = nx.Graph()
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                node_id, x_coord, y_coord = parts
                graph.add_node(node_id, x=float(x_coord), y=float(y_coord))
    
    return graph

if __name__ == "__main__":
    file_path = '/path/to/your/file.txt'
    graph = read_nodes_from_file(file_path)
    
    # Print the nodes to verify
    for node in graph.nodes(data=True):
        print(node)

        def read_edges_from_file(file_path, graph):
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 3:
                        node_start, node_end, l2_distance = parts
                        graph.add_edge(node_start, node_end, weight=float(l2_distance))

        if __name__ == "__main__":
            file_path_nodes = '/path/to/your/nodes_file.txt'
            file_path_edges = '/path/to/your/edges_file.txt'
            
            graph = read_nodes_from_file(file_path_nodes)
            read_edges_from_file(file_path_edges, graph)
            
            # Print the edges to verify
            for edge in graph.edges(data=True):
                print(edge)