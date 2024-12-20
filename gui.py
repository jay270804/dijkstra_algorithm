# # # # from graphs import graphs
# # # # from dijkstra import dijkstra_visualized
# # # # import tkinter as tk
# # # # from tkinter import ttk, messagebox
# # # # import matplotlib.pyplot as plt

# # # # def Gui():
# # # #     """Method to run gui to select and display graphs and dijkstra algorithm"""
# # # #     def update_source_entry(event):
# # # #         selected_graph = graph_selector.get()  # Get the selected graph
# # # #         nodes_range = list(range(len(graphs[selected_graph])))  # Generate node range based on graph length
# # # #         source_entry['values'] = nodes_range  # Update the combobox values
# # # #         source_entry.set(nodes_range[0])

# # # #     def run_dijkstra():
# # # #         graph_key = graph_selector.get()
# # # #         source = source_entry.get()

# # # #         if not source.isdigit():
# # # #             messagebox.showerror("Error", "Source must be an integer.")
# # # #             return

# # # #         source = int(source)
# # # #         graph = graphs.get(graph_key)

# # # #         if source < 0 or source >= len(graph):
# # # #             messagebox.showerror("Error", "Source vertex out of range.")
# # # #             return

# # # #         plt.ion()  # Turn on interactive mode
# # # #         dijkstra_visualized(graph, source)
# # # #         plt.ioff()  # Turn off interactive mode
# # # #     plt.show()  # Display the final graph

# # # #     root = tk.Tk()
# # # #     root.title("Dijkstra Algorithm Visualization")

# # # #     frame = ttk.Frame(root, padding="10")
# # # #     frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# # # #     ttk.Label(frame, text="Select Graph:").grid(column=0, row=0, sticky=tk.W)
# # # #     graph_selector = ttk.Combobox(frame, values=list(graphs.keys()), state="readonly")
# # # #     graph_selector.grid(column=1, row=0, sticky=(tk.W, tk.E))
# # # #     graph_selector.set("g4")  # Default selection


# # # #     source_entry = ttk.Combobox(frame, values=list(range(len(graphs["g4"]))), state="readonly")
# # # #     source_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# # # #     # Bind the combobox selection change to the update function
# # # #     graph_selector.bind("<<ComboboxSelected>>", update_source_entry)

# # # #     # Label and combobox for entering source node
# # # #     ttk.Label(frame, text="Enter Source Node:").grid(column=0, row=1, sticky=tk.W)


# # # #     run_button = ttk.Button(frame, text="Run Dijkstra", command=run_dijkstra)
# # # #     run_button.grid(column=0, row=2, columnspan=2, pady=10)

# # # #     root.mainloop()

# # # # Gui()
# # # from graphs import graphs
# # # from dijkstra import dijkstra_visualized, graph_iterations, current_iteration
# # # import tkinter as tk
# # # from tkinter import ttk, messagebox
# # # import matplotlib.pyplot as plt

# # # def Gui():
# # #     """Method to run GUI to select and display graphs and Dijkstra algorithm"""
# # #     def update_source_entry(event):
# # #         selected_graph = graph_selector.get()  # Get the selected graph
# # #         nodes_range = list(range(len(graphs[selected_graph])))  # Generate node range based on graph length
# # #         source_entry['values'] = nodes_range  # Update the combobox values
# # #         source_entry.set(nodes_range[0])

# # #     def run_dijkstra():
# # #         graph_key = graph_selector.get()
# # #         source = source_entry.get()

# # #         if not source.isdigit():
# # #             messagebox.showerror("Error", "Source must be an integer.")
# # #             return

# # #         source = int(source)
# # #         graph = graphs.get(graph_key)

# # #         if source < 0 or source >= len(graph):
# # #             messagebox.showerror("Error", "Source vertex out of range.")
# # #             return

# # #         plt.ion()  # Turn on interactive mode
# # #         dijkstra_visualized(graph, source)
# # #         plt.ioff()  # Turn off interactive mode
# # #         plt.show()  # Display the final graph

# # #     def navigate_iteration(event):
# # #         global current_iteration

# # #         if event.keysym == "Right":
# # #             if current_iteration < len(graph_iterations) - 1:
# # #                 current_iteration += 1
# # #         elif event.keysym == "Left":
# # #             if current_iteration > 0:
# # #                 current_iteration -= 1

# # #         # Update the display with the selected iteration
# # #         if 0 <= current_iteration < len(graph_iterations):
# # #             fig, title = graph_iterations[current_iteration]
# # #             plt.figure(fig.number)
# # #             plt.title(title)
# # #             plt.draw()

# # #     # Initialize Tkinter GUI
# # #     root = tk.Tk()
# # #     root.title("Dijkstra Algorithm Visualization")

# # #     frame = ttk.Frame(root, padding="10")
# # #     frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# # #     ttk.Label(frame, text="Select Graph:").grid(column=0, row=0, sticky=tk.W)
# # #     graph_selector = ttk.Combobox(frame, values=list(graphs.keys()), state="readonly")
# # #     graph_selector.grid(column=1, row=0, sticky=(tk.W, tk.E))
# # #     graph_selector.set("g1")  # Default selection

# # #     source_entry = ttk.Combobox(frame, values=list(range(len(graphs["g4"]))), state="readonly")
# # #     source_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# # #     graph_selector.bind("<<ComboboxSelected>>", update_source_entry)

# # #     ttk.Label(frame, text="Enter Source Node:").grid(column=0, row=1, sticky=tk.W)

# # #     run_button = ttk.Button(frame, text="Run Dijkstra", command=run_dijkstra)
# # #     run_button.grid(column=0, row=2, columnspan=2, pady=10)

# # #     # Bind arrow keys to navigate between iterations
# # #     root.bind("<Left>", navigate_iteration)
# # #     root.bind("<Right>", navigate_iteration)

# # #     root.mainloop()

# # # Gui()
# # from graphs import graphs
# # from dijkstra import dijkstra_visualized, graph_iterations, current_iteration
# # import tkinter as tk
# # from tkinter import ttk, messagebox
# # import matplotlib.pyplot as plt

# # def Gui():
# #     """Method to run GUI to select and display graphs and Dijkstra algorithm"""
# #     def update_source_entry(event):
# #         selected_graph = graph_selector.get()  # Get the selected graph
# #         nodes_range = list(range(len(graphs[selected_graph])))  # Generate node range based on graph length
# #         source_entry['values'] = nodes_range  # Update the combobox values
# #         source_entry.set(nodes_range[0])

# #     def run_dijkstra():
# #         graph_key = graph_selector.get()
# #         source = source_entry.get()

# #         if not source.isdigit():
# #             messagebox.showerror("Error", "Source must be an integer.")
# #             return

# #         source = int(source)
# #         graph = graphs.get(graph_key)

# #         if source < 0 or source >= len(graph):
# #             messagebox.showerror("Error", "Source vertex out of range.")
# #             return

# #         plt.ion()  # Turn on interactive mode
# #         dijkstra_visualized(graph, source)
# #         plt.ioff()  # Turn off interactive mode
# #         plt.show()  # Display the final graph

# #     def navigate_iteration(direction):
# #         global current_iteration

# #         if direction == "next":
# #             if current_iteration < len(graph_iterations) - 1:
# #                 current_iteration += 1
# #         elif direction == "previous":
# #             if current_iteration > 0:
# #                 current_iteration -= 1

# #         # Update the display with the selected iteration
# #         if 0 <= current_iteration < len(graph_iterations):
# #             fig, title = graph_iterations[current_iteration]
# #             plt.figure(fig.number)
# #             plt.title(title)
# #             plt.draw()

# #     # Initialize Tkinter GUI
# #     root = tk.Tk()
# #     root.title("Dijkstra Algorithm Visualization")

# #     frame = ttk.Frame(root, padding="10")
# #     frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# #     ttk.Label(frame, text="Select Graph:").grid(column=0, row=0, sticky=tk.W)
# #     graph_selector = ttk.Combobox(frame, values=list(graphs.keys()), state="readonly")
# #     graph_selector.grid(column=1, row=0, sticky=(tk.W, tk.E))
# #     graph_selector.set("g4")  # Default selection

# #     source_entry = ttk.Combobox(frame, values=list(range(len(graphs["g4"]))), state="readonly")
# #     source_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# #     graph_selector.bind("<<ComboboxSelected>>", update_source_entry)

# #     ttk.Label(frame, text="Enter Source Node:").grid(column=0, row=1, sticky=tk.W)

# #     run_button = ttk.Button(frame, text="Run Dijkstra", command=run_dijkstra)
# #     run_button.grid(column=0, row=2, columnspan=2, pady=10)

# #     # Buttons to navigate between iterations
# #     prev_button = ttk.Button(frame, text="Previous", command=lambda: navigate_iteration("previous"))
# #     prev_button.grid(column=0, row=3, pady=10)

# #     next_button = ttk.Button(frame, text="Next", command=lambda: navigate_iteration("next"))
# #     next_button.grid(column=1, row=3, pady=10)

# #     root.mainloop()

# # Gui()
# from graphs import graphs
# from dijkstra import dijkstra_visualized, graph_iterations, current_iteration
# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt

# def Gui():
#     """Method to run GUI to select and display graphs and Dijkstra algorithm"""
#     def update_source_entry(event):
#         selected_graph = graph_selector.get()  # Get the selected graph
#         nodes_range = list(range(len(graphs[selected_graph])))  # Generate node range based on graph length
#         source_entry['values'] = nodes_range  # Update the combobox values
#         source_entry.set(nodes_range[0])

#     def run_dijkstra():
#         graph_key = graph_selector.get()
#         source = source_entry.get()

#         if not source.isdigit():
#             messagebox.showerror("Error", "Source must be an integer.")
#             return

#         source = int(source)
#         graph = graphs.get(graph_key)

#         if source < 0 or source >= len(graph):
#             messagebox.showerror("Error", "Source vertex out of range.")
#             return

#         # Run Dijkstra and start displaying iterations
#         plt.ion()  # Turn on interactive mode
#         dijkstra_visualized(graph, source)
#         plt.ioff()  # Turn off interactive mode
#         plt.show()  # Display the final graph

#     def navigate_iteration(direction):
#         global current_iteration

#         # Navigate through stored iterations
#         if direction == "next":
#             if current_iteration < len(graph_iterations) - 1:
#                 current_iteration += 1
#         elif direction == "previous":
#             if current_iteration > 0:
#                 current_iteration -= 1

#         # Update the displayed graph
#         if 0 <= current_iteration < len(graph_iterations):
#             fig, title = graph_iterations[current_iteration]
#             plt.figure(fig.number)
#             plt.title(title)
#             plt.draw()

#     # Initialize Tkinter GUI
#     root = tk.Tk()
#     root.title("Dijkstra Algorithm Visualization")

#     frame = ttk.Frame(root, padding="10")
#     frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

#     ttk.Label(frame, text="Select Graph:").grid(column=0, row=0, sticky=tk.W)
#     graph_selector = ttk.Combobox(frame, values=list(graphs.keys()), state="readonly")
#     graph_selector.grid(column=1, row=0, sticky=(tk.W, tk.E))
#     graph_selector.set("g4")  # Default selection

#     source_entry = ttk.Combobox(frame, values=list(range(len(graphs["g4"]))), state="readonly")
#     source_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

#     graph_selector.bind("<<ComboboxSelected>>", update_source_entry)

#     ttk.Label(frame, text="Enter Source Node:").grid(column=0, row=1, sticky=tk.W)

#     run_button = ttk.Button(frame, text="Run Dijkstra", command=run_dijkstra)
#     run_button.grid(column=0, row=2, columnspan=2, pady=10)

#     # Buttons to navigate between iterations
#     prev_button = ttk.Button(frame, text="Previous", command=lambda: navigate_iteration("previous"))
#     prev_button.grid(column=0, row=3, pady=10)

#     next_button = ttk.Button(frame, text="Next", command=lambda: navigate_iteration("next"))
#     next_button.grid(column=1, row=3, pady=10)

#     root.mainloop()

# Gui()
from graphs import graphs
from dijkstra import dijkstra_visualized, graph_iterations, current_iteration
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

def Gui():
    """Method to run GUI to select and display graphs and Dijkstra algorithm"""
    def update_source_entry(event):
        selected_graph = graph_selector.get()  # Get the selected graph
        nodes_range = list(range(len(graphs[selected_graph])))  # Generate node range based on graph length
        source_entry['values'] = nodes_range  # Update the combobox values
        source_entry.set(nodes_range[0])

    def run_dijkstra():
        graph_key = graph_selector.get()
        source = source_entry.get()

        if not source.isdigit():
            messagebox.showerror("Error", "Source must be an integer.")
            return

        source = int(source)
        graph = graphs.get(graph_key)

        if source < 0 or source >= len(graph):
            messagebox.showerror("Error", "Source vertex out of range.")
            return

        # Run Dijkstra and start displaying iterations
        plt.ion()  # Turn on interactive mode
        dijkstra_visualized(graph, source)
        plt.ioff()  # Turn off interactive mode
        plt.show()  # Display the final graph

    def on_key_press(event):
        global current_iteration

        if event.keysym == "Right":
            # Move to the next iteration
            if current_iteration < len(graph_iterations) - 1:
                current_iteration += 1
        elif event.keysym == "Left":
            # Move to the previous iteration
            if current_iteration > 0:
                current_iteration -= 1

        # Update the displayed graph
        if 0 <= current_iteration < len(graph_iterations):
            fig, title = graph_iterations[current_iteration]
            plt.figure(fig.number)
            plt.title(title)
            plt.draw()

    # Initialize Tkinter GUI
    root = tk.Tk()
    root.title("Dijkstra Algorithm Visualization")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Select Graph:").grid(column=0, row=0, sticky=tk.W)
    graph_selector = ttk.Combobox(frame, values=list(graphs.keys()), state="readonly")
    graph_selector.grid(column=1, row=0, sticky=(tk.W, tk.E))
    graph_selector.set("g4")  # Default selection

    source_entry = ttk.Combobox(frame, values=list(range(len(graphs["g4"]))), state="readonly")
    source_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

    graph_selector.bind("<<ComboboxSelected>>", update_source_entry)

    ttk.Label(frame, text="Enter Source Node:").grid(column=0, row=1, sticky=tk.W)

    run_button = ttk.Button(frame, text="Run Dijkstra", command=run_dijkstra)
    run_button.grid(column=0, row=2, columnspan=2, pady=10)

    # Bind left and right arrow keys to navigate iterations
    root.bind("<Left>", on_key_press)
    root.bind("<Right>", on_key_press)

    root.mainloop()

Gui()
