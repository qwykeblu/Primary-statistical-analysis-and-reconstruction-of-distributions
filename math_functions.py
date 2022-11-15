import numpy as np
from collections import Counter
import math
import itertools

def get_frequency(values):
    frequency_list = Counter(values)
    dict_frequency = dict(frequency_list)
    return dict_frequency


def get_relative_frequency(frequency):
    a = np.array(frequency)
    total = 0
    for ele in range(0, len(frequency)):
        total = total + frequency[ele]
    relative_frequency_list = (a / total).tolist()
    return relative_frequency_list


def get_emperical_distribution(values):
    x = np.sort(values)
    n = x.size
    emperical_distribution = (np.arange(1, n + 1) / n).tolist()
    return emperical_distribution


#xmin
def xmin(source):
    min_element = min(source)
    return min_element


def xmax(source):
    max_element = max(source)
    return max_element


# N - обсяг вибірки
def total_frequencies(frequency):
    total = sum(frequency)
    return total


# M - кількість класів
def total_classes(total_frequency):
    total = round(1 + 1.44 * math.log(total_frequency))
    return total


def division_into_classes(list_elements, frequency):
    min_x = xmin(list_elements)
    max_x = xmax(list_elements)

    total_f = total_frequencies(frequency)
    total_c = total_classes(total_f)

    class_width = (max_x - min_x)/total_c  # h - ширина кожного класу
    class_boarders = []
    for element, num in zip((range(1, (total_c+1))), range(1, (total_c))):  # можливо треба буде змінити значення +1
        element = min_x + class_width*num
        class_boarders.append(element)

    print(class_boarders)
    # return class_boarders

