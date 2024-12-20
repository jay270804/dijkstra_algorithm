from graphviz import Digraph

# Create a flowchart for Dijkstra's Algorithm
flowchart = Digraph("Dijkstra_Algorithm_Flowchart", format="png")
flowchart.attr(bgcolor="#dad5d1")

# Define nodes with appropriate shapes
flowchart.node("start", "Start", shape="ellipse", style="filled", fillcolor="#ffffff")
flowchart.node("init", "Initialize distances \nand mark unvisited", shape="parallelogram", style="filled", fillcolor="#ffffff")
flowchart.node("curr", "Set current node \nto source", shape="rectangle", style="filled", fillcolor="#ffffff")
flowchart.node("calc", "Calculate tentative \ndistances", shape="parallelogram", style="filled", fillcolor="#ffffff")
flowchart.node("update", "Update if shorter", shape="diamond", style="filled", fillcolor="#ffffff")
flowchart.node("mark", "Mark current node \nas visited", shape="rectangle", style="filled", fillcolor="#ffffff")
flowchart.node("select", "Select unvisited node \nwith smallest distance", shape="parallelogram", style="filled", fillcolor="#ffffff")
flowchart.node("end", "All nodes visited \nor path found?", shape="diamond", style="filled", fillcolor="#ffffff")
flowchart.node("finish", "End", shape="ellipse", style="filled", fillcolor="#ffffff")

# Define edges with flow direction
flowchart.edges([
    ("start", "init"),
    ("init", "curr"),
    ("curr", "calc"),
    ("calc", "update"),
    ("update", "mark"),
    ("mark", "select"),
    ("select", "end")
])
flowchart.edge("end", "curr", label="No", style="dashed")
flowchart.edge("end", "finish", label="Yes")

# Render the flowchart
file_path = "C:/Users/Admin/dev/Dijkstra_Algo/Dijkstra_Algorithm_Flowchart"
flowchart.render(file_path, cleanup=True)

file_path + ".png"
