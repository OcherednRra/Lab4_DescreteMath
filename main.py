from tkinter import *
from tkinter import messagebox
from graph_generation import GraphGeneration
import matplotlib.pyplot as plt
import networkx as nx

from student_info_window import StudentInfoWindow


class Lab(Tk):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Лаб4")

        self.about_student_button()

        self.caption = Label(self, text="Введіть кількість вершин графа")
        self.caption.grid(row=0, column=0, pady=(50, 10), padx=(10, 10))

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0, padx=(10, 0))

        self.generation_button = Button(self, width=20, height=1, wraplength=200,
                                 text=" ----------> ",
                                 command=self.generate_graph_window)
        self.generation_button.grid(row=2, column=0, pady=(10, 15), padx=(10, 0))

    def generate_graph_window(self):
        nodes_num = int(self.entry.get())
        self.nodes_number = nodes_num

        self.destroyer()

        main_master = Frame(self)
        main_master.grid(padx=(30, 30), pady=(10, 0))

        table_master = Frame(main_master)
        table_master.grid(column=0, columnspan=nodes_num, row=nodes_num+2)

        labels_row = [Label(table_master, text=str(i+1)) for i in range(nodes_num)]
        labels_column = [Label(table_master, text=str(i+1)) for i in range(nodes_num)]
        matrix_entries = [[Entry(table_master, width=3) for i in range(nodes_num)]
                                                        for j in range(nodes_num)]

        for i in range(len(labels_row)):
            labels_row[i].grid(row=0, column=i+1)
            labels_column[i].grid(row=i+1, column=0)

        for i in range(len(labels_row)):
            for j in range(len(labels_row)):
                matrix_entries[i][j].grid(row=i+1, column=j+1)
                matrix_entries[i][j].insert(END, "0")

        self.matrix_entries = matrix_entries

        caption = Label(main_master, text="Матриця суміжності", justify=CENTER)
        caption.grid(row=nodes_num+3, column=1, columnspan=nodes_num, pady=(0, 20))

        self.graph_show = Button(main_master, width=20, text="Згенерувати граф", command=self.draw_graph)
        self.graph_show.grid(row=nodes_num+4, column=1, columnspan=nodes_num, pady=(0, 5))

        self.task_calculate = Button(main_master, width=20, wraplength=180,
                                     text="Розфарбувати граф", command=self.draw_color_graph)
        self.task_calculate.grid(row=nodes_num+5, column=1, columnspan=nodes_num, pady=(0, 10))

    def about_student_button(self):
        self.bruh_button = Button(self, width=16, height=1, fg="#d9073d", text="!  Інфо  !",
               activebackground="grey", command=self.open_student_info_window)
        self.bruh_button.grid(column=0, row=0, padx=(10, 0), columnspan=2, pady=(0, 30))

    def open_student_info_window(self):
        student_info_window = StudentInfoWindow(self)
        student_info_window.grab_set()

    def destroyer(self):
        self.entry.destroy()
        self.generation_button.destroy()
        self.bruh_button.destroy()
        self.caption.destroy()

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
