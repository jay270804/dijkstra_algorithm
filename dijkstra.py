# # # # from tkinter import messagebox
# # # import networkx as nx
# # # import matplotlib.pyplot as plt
# # # # from graphs import graphs

# # # def dijkstra_visualized(graph, source):
# # #     # Initialize distances and visited nodes
# # #     V = len(graph)
# # #     dist = [float('inf')] * V
# # #     visited = [False] * V
# # #     dist[source] = 0

# # #     # Create a NetworkX graph
# # #     G = nx.Graph()

# # #     # Add edges with weights to the graph
# # #     for u in range(V):
# # #         for v in range(V):
# # #             if graph[u][v] > 0:
# # #                 G.add_edge(u, v, weight=graph[u][v])

# # #     # Visualization setup
# # #     pos = nx.spring_layout(G)  # Position the nodes
# # #     draw_graph(G, pos, dist, visited, source)

# # #     for _ in range(V):
# # #         # Find the vertex with the minimum distance
# # #         u = min_distance(dist, visited)
# # #         visited[u] = True

# # #         # Update distances of adjacent vertices
# # #         for v in range(V):
# # #             if (
# # #                 not visited[v]
# # #                 and graph[u][v] > 0
# # #                 and dist[u] != float('inf')
# # #                 and dist[u] + graph[u][v] < dist[v]
# # #             ):
# # #                 dist[v] = dist[u] + graph[u][v]

# # #         # Update the visualization
# # #         draw_graph(G, pos, dist, visited, source, highlight_node=u)

# # #     # Final visualization with distances
# # #     draw_graph(G, pos, dist, visited, source, final=True)

# # #     # Print distances
# # #     print_solution(dist)

# # # def min_distance(dist, visited):
# # #     min_val = float('inf')
# # #     min_index = -1
# # #     for v in range(len(dist)):
# # #         if not visited[v] and dist[v] < min_val:
# # #             min_val = dist[v]
# # #             min_index = v
# # #     return min_index

# # # def draw_graph(G, pos, dist, visited, source, highlight_node=None, final=False):
# # #     plt.clf()  # Clear the current plot
# # #     node_colors = ['green' if visited[node] else 'blue' for node in G.nodes()]
# # #     edge_labels = nx.get_edge_attributes(G, 'weight')

# # #     if highlight_node is not None and not final:
# # #         node_colors[highlight_node] = 'grey'  # Highlight current node

# # #     nx.draw(
# # #         G,
# # #         pos,
# # #         with_labels=True,
# # #         node_color=node_colors,
# # #         node_size=700,
# # #         font_size=10,
# # #         font_color="white",
# # #     )
# # #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# # #     plt.title(f"Source: {source} | Distances: {dist}")
# # #     plt.pause(1)  # Pause for animation

# # # def print_solution(dist):
# # #     print("Vertex \t Distance from Source")
# # #     for i in range(len(dist)):
# # #         print(f"{i} \t\t {dist[i]}")

# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # Global variables to store graph iterations and current iteration index
# # graph_iterations = []
# # current_iteration = 0  # To track the current iteration

# # def dijkstra_visualized(graph, source):
# #     global current_iteration
# #     V = len(graph)
# #     dist = [float('inf')] * V
# #     visited = [False] * V
# #     dist[source] = 0

# #     # Create a NetworkX graph
# #     G = nx.Graph()

# #     # Add edges with weights to the graph
# #     for u in range(V):
# #         for v in range(V):
# #             if graph[u][v] > 0:
# #                 G.add_edge(u, v, weight=graph[u][v])

# #     # Visualization setup
# #     pos = nx.spring_layout(G)  # Position the nodes
# #     draw_graph(G, pos, dist, visited, source)

# #     for _ in range(V):
# #         # Find the vertex with the minimum distance
# #         u = min_distance(dist, visited)
# #         visited[u] = True

# #         # Update distances of adjacent vertices
# #         for v in range(V):
# #             if (
# #                 not visited[v]
# #                 and graph[u][v] > 0
# #                 and dist[u] != float('inf')
# #                 and dist[u] + graph[u][v] < dist[v]
# #             ):
# #                 dist[v] = dist[u] + graph[u][v]

# #         # Update the visualization
# #         draw_graph(G, pos, dist, visited, source, highlight_node=u)

# #     # Final visualization with distances
# #     draw_graph(G, pos, dist, visited, source, final=True)

# #     # Print distances
# #     print_solution(dist)

# # def min_distance(dist, visited):
# #     min_val = float('inf')
# #     min_index = -1
# #     for v in range(len(dist)):
# #         if not visited[v] and dist[v] < min_val:
# #             min_val = dist[v]
# #             min_index = v
# #     return min_index

# # def draw_graph(G, pos, dist, visited, source, highlight_node=None, final=False):
# #     global current_iteration
# #     plt.clf()  # Clear the current plot
# #     node_colors = ['green' if visited[node] else 'blue' for node in G.nodes()]
# #     edge_labels = nx.get_edge_attributes(G, 'weight')

# #     if highlight_node is not None and not final:
# #         node_colors[highlight_node] = 'grey'  # Highlight current node

# #     nx.draw(
# #         G,
# #         pos,
# #         with_labels=True,
# #         node_color=node_colors,
# #         node_size=700,
# #         font_size=10,
# #         font_color="white",
# #     )
# #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# #     # Display the title above the graph
# #     plt.title(f"Source: {source} | Distances: {dist}", fontsize=12, verticalalignment="bottom")
# #     plt.pause(1)  # Pause for animation

# #     # Store the current iteration's figure and title
# #     graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))
# #     current_iteration = len(graph_iterations) - 1  # Set current iteration to the latest one

# # def print_solution(dist):
# #     print("Vertex \t Distance from Source")
# #     for i in range(len(dist)):
# #         print(f"{i} \t\t {dist[i]}")
# import networkx as nx
# import matplotlib.pyplot as plt

# # Global variables to store iterations and current iteration index
# graph_iterations = []
# current_iteration = 0

# def dijkstra_visualized(graph, source):
#     global graph_iterations, current_iteration

#     # Initialize distances and visited nodes
#     V = len(graph)
#     dist = [float('inf')] * V
#     visited = [False] * V
#     dist[source] = 0

#     # Create a NetworkX graph
#     G = nx.Graph()

#     # Add edges with weights to the graph
#     for u in range(V):
#         for v in range(V):
#             if graph[u][v] > 0:
#                 G.add_edge(u, v, weight=graph[u][v])

#     # Visualization setup
#     pos = nx.spring_layout(G)  # Position the nodes
#     draw_graph(G, pos, dist, visited, source)

#     # Store the first iteration
#     graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

#     for _ in range(V):
#         # Find the vertex with the minimum distance
#         u = min_distance(dist, visited)
#         visited[u] = True

#         # Update distances of adjacent vertices
#         for v in range(V):
#             if (
#                 not visited[v]
#                 and graph[u][v] > 0
#                 and dist[u] != float('inf')
#                 and dist[u] + graph[u][v] < dist[v]
#             ):
#                 dist[v] = dist[u] + graph[u][v]

#         # Update the visualization
#         draw_graph(G, pos, dist, visited, source, highlight_node=u)

#         # Store each iteration
#         graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

#     # Final visualization with distances
#     draw_graph(G, pos, dist, visited, source, final=True)

#     # Store the final iteration
#     graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

#     # Print distances
#     print_solution(dist)

# def min_distance(dist, visited):
#     min_val = float('inf')
#     min_index = -1
#     for v in range(len(dist)):
#         if not visited[v] and dist[v] < min_val:
#             min_val = dist[v]
#             min_index = v
#     return min_index

# def draw_graph(G, pos, dist, visited, source, highlight_node=None, final=False):
#     plt.clf()  # Clear the current plot
#     node_colors = ['green' if visited[node] else 'blue' for node in G.nodes()]
#     edge_labels = nx.get_edge_attributes(G, 'weight')

#     if highlight_node is not None and not final:
#         node_colors[highlight_node] = 'grey'  # Highlight current node

#     nx.draw(
#         G,
#         pos,
#         with_labels=True,
#         node_color=node_colors,
#         node_size=700,
#         font_size=10,
#         font_color="white",
#     )
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#     plt.title(f"Source: {source} | Distances: {dist}")
#     plt.pause(1)  # Pause for animation

# def print_solution(dist):
#     print("Vertex \t Distance from Source")
#     for i in range(len(dist)):
#         print(f"{i} \t\t {dist[i]}")
import networkx as nx
import matplotlib.pyplot as plt

# Global variables to store iterations and current iteration index
graph_iterations = []
current_iteration = 0

def dijkstra_visualized(graph, source):
    global graph_iterations, current_iteration

    # Initialize distances and visited nodes
    V = len(graph)
    dist = [float('inf')] * V
    visited = [False] * V
    dist[source] = 0

    # Create a NetworkX graph
    G = nx.Graph()

    # Add edges with weights to the graph
    for u in range(V):
        for v in range(V):
            if graph[u][v] > 0:
                G.add_edge(u, v, weight=graph[u][v])

    # Visualization setup
    pos = nx.spring_layout(G)  # Position the nodes
    draw_graph(G, pos, dist, visited, source)

    # Store the first iteration
    graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

    for _ in range(V):
        # Find the vertex with the minimum distance
        u = min_distance(dist, visited)
        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(V):
            if (
                not visited[v]
                and graph[u][v] > 0
                and dist[u] != float('inf')
                and dist[u] + graph[u][v] < dist[v]
            ):
                dist[v] = dist[u] + graph[u][v]

        # Update the visualization
        draw_graph(G, pos, dist, visited, source, highlight_node=u)

        # Store each iteration
        graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

    # Final visualization with distances
    draw_graph(G, pos, dist, visited, source, final=True)

    # Store the final iteration
    graph_iterations.append((plt.gcf(), f"Source: {source} | Distances: {dist}"))

    # Print distances
    print_solution(dist)

def min_distance(dist, visited):
    min_val = float('inf')
    min_index = -1
    for v in range(len(dist)):
        if not visited[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index

def draw_graph(G, pos, dist, visited, source, highlight_node=None, final=False):
    plt.clf()  # Clear the current plot
    node_colors = ['green' if visited[node] else 'blue' for node in G.nodes()]
    edge_labels = nx.get_edge_attributes(G, 'weight')

    if highlight_node is not None and not final:
        node_colors[highlight_node] = 'grey'  # Highlight current node

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=700,
        font_size=10,
        font_color="white",
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Source: {source} | Distances: {dist}")
    plt.pause(1)  # Pause for animation

def print_solution(dist):
    print("Vertex \t Distance from Source")
    for i in range(len(dist)):
        print(f"{i} \t\t {dist[i]}")
