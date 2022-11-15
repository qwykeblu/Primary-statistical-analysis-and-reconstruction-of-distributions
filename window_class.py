from tkinter import *
from tkinter import ttk
from main_functions import *
import tkinter as tk
from tkinter.font import BOLD, Font
from pandastable import Table

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        window_height = 600
        window_width = 1000

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.title('Лабораторна 1')
        # set up variable
        self.option_var = tk.StringVar(self)
        self.notebook = ttk.Notebook(self)

        self.add_notebook_widget()
        self.style = ttk.Style(self)
        self.style.theme_use('vista') #clam winnative vista xpnative


    #self.output_label['text'] = f'You selected: {self.option_var.get()}'


    def add_notebook_widget(self):

        #--------------------------| VARIATIONAL SERIES |--------------------------
        variational_series = Frame(self, bg='grey')
        self.notebook.add(variational_series, text="Варіаційний ряд")
        Frame_00 = Frame(variational_series, bg='Red', borderwidth=2, relief=GROOVE)
        Frame_00.pack(side=TOP, padx=10, pady=2.5)

        # Positive
        Frame_title011 = Frame(Frame_00, bg="white", height = 10, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_title011.grid(row = 0, column = 0, padx=5, pady=5)
        Label(Frame_title011, text="Варіаціний ряд").pack(padx=2, pady=2)


        Frame_01 = Frame(Frame_00, bg="white", height = 200, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_01.grid(row = 1, column = 0, padx=5, pady=5)

        res = file_choice(filename=get_file(self))



        created_dataframe = create_dataframe_variation_series(res)


        cols = list(created_dataframe.columns)

        tree1 = ttk.Treeview(Frame_01)

        tree1.grid(row = 0, column = 0, padx = 20, pady = 5)
        verscrlbar = ttk.Scrollbar(Frame_01,
                                   orient="vertical",
                                   command=tree1.yview)
        verscrlbar.grid(row=0, column=1, sticky=NS)

        tree1.configure(yscrollcommand=verscrlbar.set)
        tree1["columns"] = cols
        for i in cols:
            tree1.column(i, anchor="w", width=50)
            tree1.heading(i, text=i, anchor='w')

        for index, row in created_dataframe.iterrows():
            tree1.insert("", 0, text=index+1, values=list(row))

        s = ttk.Style()
        s.configure('Treeview', rowheight=20)  # repace 40 with whatever you need
        # b = Button(Frame_01, text="Показати графік", command=lambda: graph_empericaldistribution(res, ed))
        # b.grid(row = 0, column = 0, padx = 80, pady = 5)










        Frame_title02 = Frame(Frame_00, bg="white", height = 10, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_title02.grid(row = 0, column = 1, padx=2, pady=2)
        Label(Frame_title02, text="Розподілення на класи").pack(padx=2, pady=2)

        Frame_02 = Frame(Frame_00, bg="white", height = 200, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_02.grid(row = 1, column = 1, padx=5, pady=5)

        # spin_box = ttk.Spinbox(
        #     Frame_02,
        #     from_=1,
        #     to=30,  # межі класу
        #     textvariable=self.option_var,
        #     wrap=True)
        # label_classes = ttk.Label(
        #     Frame_02,
        #     text='Кількість класів для розбиття',
        #     foreground='black',
        #     font=("Arial", 10))
        # label_classes.pack(side=BOTTOM, padx=1,pady=20)
        # spin_box.pack(side=BOTTOM, padx=15, pady=20)

        tree2 = ttk.Treeview(Frame_02)

        tree2.grid(row = 0, column = 1, padx = 20, pady = 5)
        verscrlbar = ttk.Scrollbar(Frame_02,
                                   orient="vertical",
                                   command=tree2.yview)
        verscrlbar.grid(row=0, column=2, sticky=NS)

        tree2.configure(yscrollcommand=verscrlbar.set)
        tree2["columns"] = cols
        for i in cols:
            tree2.column(i, anchor="w", width=50)
            tree2.heading(i, text=i, anchor='w')

        for index, row in created_dataframe.iterrows():
            tree2.insert("", 0, text=index + 1, values=list(row))

        s1 = ttk.Style()
        s1.configure('Treeview', rowheight=20, )


        # b = Button(Frame_02, text="Показати графік",
        #            command=lambda: graph_empericaldistribution(res, ed))
        # b.grid(row=0, column=0, padx=80, pady=5)


        #frame_left = Frame(variational_series, bg='violet')
        # frame_left.pack(side=LEFT)
        #
        # frame_right = Frame(variational_series)
        # frame_right.pack(side=RIGHT)
        # res = file_choice(filename=get_file(self))
        #
        #
        #
        # created_dataframe = create_dataframe_variation_series(res)
        #
        #
        # cols = list(created_dataframe.columns)
        # label_variation_series = ttk.Label(
        #     frame_left,
        #     text='Варіаційний ряд',
        #     foreground='blue',
        #     font=("Arial", 10))
        # label_variation_series.pack(side=TOP)
        #
        # tree1 = ttk.Treeview(frame_left)
        #
        # tree1.pack(side=LEFT)
        # verscrlbar = ttk.Scrollbar(frame_left,
        #                            orient="vertical",
        #                            command=tree1.yview)
        # verscrlbar.pack(side='right', fill='y')
        #
        # tree1.configure(yscrollcommand=verscrlbar.set)
        # tree1["columns"] = cols
        # for i in cols:
        #     tree1.column(i, anchor="w", width=50)
        #     tree1.heading(i, text=i, anchor='w')
        #
        # for index, row in created_dataframe.iterrows():
        #     tree1.insert("", 0, text=index+1, values=list(row))
        #
        # s = ttk.Style()
        # s.configure('Treeview', rowheight=20)  # repace 40 with whatever you need
        #
        #
        fr = get_frequency(res)
        division_into_classes(res, fr)
        ed=get_emperical_distribution(res)
        #
        # separator = ttk.Separator(variational_series, orient='vertical')
        # separator.place(relx=0.5, rely=0, relwidth=0, relheight=1)
        # spin_box = ttk.Spinbox(
        #     frame_right,
        #     from_=1,
        #     to=30,  # межі класу
        #     textvariable=self.option_var,
        #     wrap=True)
        # label_classes = ttk.Label(
        #     frame_right,
        #     text='Кількість класів для розбиття',
        #     foreground='black',
        #     font=("Arial", 10))
        # label_classes.pack(side=BOTTOM, padx=1,pady=20)
        # spin_box.pack(side=BOTTOM, padx=15, pady=20)
        # label_divided_series = ttk.Label(
        #     frame_right,
        #     text='Розділення на класи',
        #     foreground='blue',
        #     font=("Arial", 10))
        # label_divided_series.pack(side=TOP)
        # tree2 = ttk.Treeview(frame_right)
        #
        # tree2.pack(side=RIGHT)
        # verscrlbar = ttk.Scrollbar(frame_right,
        #                            orient="vertical",
        #                            command=tree2.yview)
        # verscrlbar.pack(side='right', fill='y')
        #
        # tree2.configure(yscrollcommand=verscrlbar.set)
        # tree2["columns"] = cols
        # for i in cols:
        #     tree2.column(i, anchor="w", width=50)
        #     tree2.heading(i, text=i, anchor='w')
        #
        # for index, row in created_dataframe.iterrows():
        #     tree2.insert("", 0, text=index + 1, values=list(row))
        #
        # s1 = ttk.Style()
        # s1.configure('Treeview', rowheight=20, )
        #
        # current_value = tk.StringVar(value=0)

        statistical_characteristics = Frame(self)
        density_distribution_function_probabilitygrid = Frame(self)
        abnormal_values = Frame(self)

        self.notebook.add(statistical_characteristics, text="Статистичні характеристики")

        self.notebook.add(density_distribution_function_probabilitygrid, text="Щільність, функція розподілу,ймовірнісна сітка")
        Frame_0 = Frame(density_distribution_function_probabilitygrid, bg = 'Black', borderwidth = 2, relief = GROOVE)
        Frame_0.pack(side = TOP, padx = 10, pady = 2.5)

        # Positive
        Frame_title01 = Frame(Frame_0, bg="white", height = 10, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_title01.grid(row = 0, column = 0, padx=5, pady=5)
        Label(Frame_title01, text="Гістограма та теоретична функція щільності").pack(padx=2, pady=2)

        Frame_01 = Frame(Frame_0, bg="white", height = 200, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_01.grid(row = 1, column = 0, padx=5, pady=5)

        b = Button(Frame_01, text="Показати графік", command=lambda: graph_empericaldistribution(res, ed))
        b.grid(row = 0, column = 0, padx = 80, pady = 5)


        Frame_title02 = Frame(Frame_0, bg="white", height = 10, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_title02.grid(row = 0, column = 1, padx=2, pady=2)
        Label(Frame_title02, text="Емпірична функція розподілу").pack(padx=2, pady=2)

        Frame_02 = Frame(Frame_0, bg="white", height = 200, width = 300, borderwidth = 2, relief=GROOVE)
        Frame_02.grid(row = 1, column = 1, padx=5, pady=5)

        b = Button(Frame_02, text="Показати графік",
                   command=lambda: graph_empericaldistribution(res, ed))
        b.grid(row=0, column=0, padx=80, pady=5)

        Frame_1 = Frame(density_distribution_function_probabilitygrid, bg = 'white', borderwidth = 2, relief = FLAT)
        Frame_1.pack(side = TOP)

        button = Button(Frame_1, text = 'Run')
        button.pack(pady = 10)

        Button(density_distribution_function_probabilitygrid, text='Click me !', bd='5',command=self.destroy).pack(side='top')







        self.notebook.add(abnormal_values, text="Аномальні значення")
        self.notebook.pack(expand=True, fill="both")

        Label(statistical_characteristics, text="Goodbye, this is tab#2", width=50, height=25).pack()

        #Button(abnormal_values, text="Click Me !\nI'm a Button").pack(side=BOTTOM)
















