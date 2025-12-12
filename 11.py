with open("input/11.txt", "r") as f:
    lines = f.readlines()

output_dict: dict[str, list[str]] = {}
node_set = set()

for line in lines:
    line = line.strip()
    input, outputs = line.split(": ")
    outputs = outputs.split()
    output_dict[input] = outputs
    node_set.add(input)
    node_set.update(outputs)


import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(node_set)
for input, outputs in output_dict.items():
    for output in outputs:
        G.add_edge(input, output)


def number_of_paths(G: nx.DiGraph, source: str, target: str) -> int:
    if not nx.is_directed_acyclic_graph(G):
        print("Graph is not a DAG")
        return 0

    if not (source in G and target in G):
        print("Source or target node not in graph")
        return 0

    path_counts = {node: 0 for node in G.nodes()}
    path_counts[source] = 1

    for node in nx.topological_sort(G):
        for neighbor in G.successors(node):
            path_counts[neighbor] += path_counts[node]

    return path_counts[target]


print(number_of_paths(G, "you", "out"))

svr_fft = number_of_paths(G, "svr", "fft")
fft_dac = number_of_paths(G, "fft", "dac")
dac_out = number_of_paths(G, "dac", "out")

svr_dac = number_of_paths(G, "svr", "dac")
dac_fft = number_of_paths(G, "dac", "fft")
fft_out = number_of_paths(G, "fft", "out")

print(svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out)
