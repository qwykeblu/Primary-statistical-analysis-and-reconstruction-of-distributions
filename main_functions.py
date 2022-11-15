from credentials import *
import pandas as pd
from math_functions import *
from tkinter import filedialog
import matplotlib.pyplot as plt


def get_file(source):
    source.file_name = filedialog.askopenfilename(initialdir=MAIN_PATH, title="Відкрити Файл", filetypes=(("Text files",
                                                                                                     "*.txt*"),
                                                                                                    ("DAT files",
                                                                                                     "*.DAT*")))
    return source.file_name


def file_choice(filename):  # showing data from appropriate file
    with open(filename,'r') as file:
        lines = file.read().splitlines()
        res = [eval(i) for i in lines]
        res.sort()  # sorting elements from file
        print(res)
        return res


def create_dataframe_variation_series(values):
    #df1 = pd.Series(values).value_counts().sort_index().reset_index().reset_index(drop=True)
    #df1.columns = ['Element', 'Frequency']
    #frequency = (df1['Frequency'].values).tolist()  # list of 'int' data's of frequencies of values from res
    frequency = get_frequency(values)

    elements = list(frequency.keys())
    frequencies = list(frequency.values())

    print(elements)
    print(frequencies)
    relative_frequency = get_relative_frequency(frequencies)
    emperical_distribution = get_emperical_distribution(elements)

    data = {'Element': elements, 'Frequency': frequencies, 'Relative frequency': relative_frequency,'EDF': emperical_distribution}
    dt = pd.DataFrame.from_dict(data=data)
    sorted_dt = dt.sort_values("Element", axis = 0, ascending = False)
    return sorted_dt


def create_dataframe_divided_series(frequency):

    elements={}
    classes={}
    relative_frequency={}
    emperical_distribution = {}

    data = {'Element': elements, 'Classes': classes, 'Relative frequency': relative_frequency, 'EDF': emperical_distribution}
    dt = pd.DataFrame.from_dict(data=data)
    sorted_dt = dt.sort_values("Element", axis=0, ascending=False)
    return sorted_dt


def graph_empericaldistribution(values,emperical_distribution):
    x = values
    y = emperical_distribution

    plt.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    plt.xlabel("X - Елементи вибірки")
    plt.ylabel("Y - Значення  емпіричної функції розподілу")
    plt.title('Графік емпіричної функції розподілу')
    plt.show()
