import networkx as nx

with open("input/8.txt", "r") as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]
coords_parts = [line.split(",") for line in lines]
coords: list[tuple[int, int, int]] = [
    (int(x), int(y), int(z)) for x, y, z in coords_parts
]


def distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


pairwise_distances: dict[tuple[int, int], int] = {}
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        pairwise_distances[(i, j)] = distance(coords[i], coords[j])

sorted_distances = sorted(pairwise_distances.items(), key=lambda item: item[1])


G = nx.Graph()
G.add_nodes_from(range(len(coords)))

for (i, j), dist in sorted_distances[0:1000]:
    G.add_edge(i, j, weight=dist)

components = list(nx.connected_components(G))
components.sort(key=lambda c: len(c), reverse=True)
largest_components = components[0:3]
product_of_sizes = 1
for c in largest_components:
    product_of_sizes *= len(c)
print(product_of_sizes)

G = nx.Graph()
G.add_nodes_from(range(len(coords)))

for (i, j), dist in sorted_distances:
    G.add_edge(i, j, weight=dist)
    if nx.is_connected(G):
        print(coords[i][0] * coords[j][0])
        break
