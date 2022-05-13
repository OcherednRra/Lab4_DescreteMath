from tkinter import *
from tkinter import messagebox
from graph_generation import GraphGeneration
import matplotlib.pyplot as plt
import networkx as nx


class Lab(Tk):
    def __init__(self, master=None):
        super().__init__(master)

        self.caption = Label(self, text="Введіть кількість вершин графа")
        self.caption.grid(row=0, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0)

        self.generation_button = Button(self, width=30, height=2, wraplength=200,
                                 text="Перейти до наступного етапу генерування графа",
                                 command=self.generate_graph_window)
        self.generation_button.grid(row=2, column=0)

    def generate_graph_window(self):
        nodes_num = int(self.entry.get())
        self.nodes_number = nodes_num

        self.destroyer()

        labels_row = [Label(self, text=str(i+1)) for i in range(nodes_num)]
        labels_column = [Label(self, text=str(i+1)) for i in range(nodes_num)]
        matrix_entries = [[Entry(self, width=3) for i in range(nodes_num)]
                                               for j in range(nodes_num)]

        for i in range(len(labels_row)):
            labels_row[i].grid(row=0, column=i+1)
            labels_column[i].grid(row=i+1, column=0)

        for i in range(len(labels_row)):
            for j in range(len(labels_row)):
                matrix_entries[i][j].grid(row=i+1, column=j+1)
                matrix_entries[i][j].insert(END, "0")

        self.matrix_entries = matrix_entries

        self.caption.config(text="Матриця суміжності графа", justify=CENTER)
        self.caption.grid(row=nodes_num+2, column=1, columnspan=nodes_num)

        self.graph_show = Button(self, width=20, text="Згенерувати граф", command=self.draw_graph)
        self.graph_show.grid(row=nodes_num+3, column=1, columnspan=nodes_num)

        self.task_calculate = Button(self, width=20, wraplength=180,
                                     text="Розфарбувати граф", command=self.draw_color_graph)
        self.task_calculate.grid(row=nodes_num+4, column=1, columnspan=nodes_num)

    def destroyer(self):
        self.entry.destroy()
        self.generation_button.destroy()

    def graph_generator(self):
        self.graph = GraphGeneration(self.nodes_number)
        self.graph.create_connections(self.matrix_entries)

    def draw_graph(self):
        self.graph_generator()
        self.graph.draw()

    def draw_color_graph(self):
        self.graph_generator()
        self.graph.coloring_algorithm()



if __name__ == "__main__":
    app = Lab()
    app.mainloop()
