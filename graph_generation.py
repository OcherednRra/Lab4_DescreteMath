import networkx as nx
from tkinter import messagebox
import pylab as plt


class GraphGeneration():
    def __init__(self, nodes):
        """ ----- Количество вершин графа ----- """
        self.nodes_number = nodes

    def create_connections(self, table_entries):
        nodes_number = self.nodes_number

        self.data_array = [[int(table_entries[i][j].get())
                            for i in range(nodes_number)]
                            for j in range(nodes_number)]

        """ ----- Создание графа и вершин графа -----"""
        self.graph = nx.Graph()
        for i in range(1, nodes_number):
            self.graph.add_node(i)

        """ ----- Создание связей между вершинами ----- """
        for i in range(1, nodes_number):
            for j in range(nodes_number):
                if self.data_array[i][j] == 1:
                    self.graph.add_edge(i+1, j+1)


    def draw(self):
        """ ----- Визуализация графа ----- """
        nx.draw(self.graph, node_color="#DC143C", with_labels=True,
                pos=nx.circular_layout(self.graph))
        plt.show()


    def coloring_algorithm(self):
        """ ----- Алгоритм разкрашивания ----- """

        def graph_coloring():
            colored_list = [[]]
            color_number = 0
            subarray = []
            temp2 = temp1 = -1

            def bruh(num):
                for t in colored_list[color_number]:
                    if self.data_array[t][num] == 1:
                        return False
                return True

            for i in self.data_array:
                temp1 += 1
                if temp1 not in subarray:

                    if not bruh(temp1):
                        colored_list.append([])
                        color_number += 1
                        subarray.append(temp1)
                        colored_list[color_number].append(temp1)

                    temp2 = temp1
                    for j in i[temp1:]:
                        if j == 0 and temp2 not in subarray and bruh(temp2):
                            subarray.append(temp2)
                            colored_list[color_number].append(temp2)
                        temp2 += 1

            for i in range(len(colored_list)):
                for j in range(len(colored_list[i])):
                    colored_list[i][j] += 1

            return colored_list


        def show_colored_graf(nodes):
            color_list = ["#cf0200", "#4040ff", "#14b927", "#f5ff05", "#9932CC", "#FF1493"]
            for i in range(len(nodes)):
                nx.draw(self.graph, node_color=color_list[i], nodelist=nodes[i],
                        with_labels=True, pos=nx.circular_layout(self.graph))
            plt.show()

        show_colored_graf(graph_coloring())
