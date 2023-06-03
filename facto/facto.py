from . import segment

import facto


# confirm type
def coefficients_to_decimal(coefficients):
    decimal = 0
    factorial = 1
    for i in range(1, len(coefficients) + 1):
        if coefficients[-1 * i] > i:
            raise ValueError('Coefficient can\'t be larger than the base at the digit')
        factorial *= i
        decimal += coefficients[-1 * i] * factorial
    return decimal


# confirm type
def decimal_to_coefficients(decimal):
    coefficients = []
    iterator = 2
    while decimal != 0:
        decimal, remainder = divmod(decimal, iterator)
        coefficients.append(remainder)
        iterator = iterator + 1
    coefficients.reverse()
    return coefficients


def facto_from_factoradic(coefficients):
    return Facto(facto.facto.coefficients_to_decimal(coefficients))


def next_permutation(perm):
    list_length = len(perm)
    if list_length == 0 or list_length == 1:
        return perm
    iterator = -2
    index_of_first_element_larger_than_iterator = -1
    while iterator != -1 * list_length - 1 and perm[iterator] >= perm[iterator + 1]:
        iterator -= 1
    if iterator == -1 * list_length - 1:
        return perm
    for j in range(iterator + 1, 0):
        if perm[iterator] >= perm[j]:
            index_of_first_element_larger_than_iterator = j - 1
            break
    temp = perm[iterator]
    perm[iterator] = perm[index_of_first_element_larger_than_iterator]
    perm[index_of_first_element_larger_than_iterator] = temp
    perm[list_length + iterator + 1:] = reversed(perm[list_length + iterator + 1:])
    return perm


def permutation_from_coefficients(reference_list, coefficients):
    perm = list()
    for i in range(0, len(reference_list) - len(coefficients) - 1):
        perm.append(reference_list[i])
    seg = segment.SegmentTree(reference_list[len(reference_list) - len(coefficients) - 1: len(reference_list)])
    for j in coefficients:
        perm.append(seg.arr[seg.find_prefix_with_sum(j+1)])
    while seg.tree[1] != 0:
        perm.append(seg.arr[seg.find_prefix_with_sum(1)])
    return perm


class Facto:
    decimal = 0

    def __init__(self, decimal):
        if not isinstance(decimal, int):
            raise TypeError("Factoradic numbers must be integers")
        if decimal < 0:
            raise ValueError("Factoradic numbers must be positive")
        self.decimal = decimal

    def __int__(self):
        return self.decimal

    def __add__(self, other):
        if isinstance(other, Facto):
            return self.decimal + other.decimal
        else:
            raise TypeError("You can only add facto numbers to other facto numbers")

    def __sub__(self, other):
        if isinstance(other, Facto):
            return self.decimal - other.decimal
        else:
            raise TypeError("You can only subtract facto from other facto numbers")

    def __mul__(self, other):
        if isinstance(other, Facto):
            return self.decimal * other.decimal
        else:
            raise TypeError("You can only multiply facto numbers to other facto numbers")

    def __truediv__(self, other):
        if isinstance(other, Facto):
            if other.decimal != 0:
                return self.decimal / other.decimal
        raise TypeError("You can only subtract facto numbers to other facto numbers")

    def __str__(self):
        facto_string = ""
        coefficients = facto.facto.decimal_to_coefficients(self.decimal)
        facto_string += str(coefficients[0])
        for i in coefficients[1:]:
            facto_string += ":" + str(i)
        return facto_string

    def get_integer(self):
        return self.decimal

    def get_coefficients(self):
        return decimal_to_coefficients(self.decimal)
