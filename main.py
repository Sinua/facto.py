import math

import facto
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def print_hi(name):
    coefficient = [1, 1, 1]
    fct = facto.facto.from_factoradic_to_decimal(coefficient)
    coefficients = [1, 1]
    fct2 = facto.facto_from_factoradic(coefficients)
    print(facto.Facto(15))


def script(facto):
    while facto.decimal < 1000000:
        deci = facto.get_integer()
        numCof = len(facto.get_coefficients())
        counter = 0
        while deci > 0:
            deci //= 10
            counter += 1
        print(str(counter) + " : " + str(numCof))
        facto.decimal += 1


def norm_fact(current, rem_counter):
    while rem_counter > 0:
        current = facto.facto.next_permutation(current)
        rem_counter -= 1
    return current


def snapshots_with_decider(reference):
    norm_snapshots = list()
    new_snapshots = list()
    items = reference[:]
    factorial = math.factorial(len(items))
    timers = list()
    curr_num_of_digits = 1
    for i in range(1, factorial):
        start = timer()
        facto.facto.permutation_from_coefficients(reference, facto.facto.decimal_to_coefficients(i))
        timers.append(timer() - start)
        start = timer()
        norm_fact(items, 1)
        end = timer()
        if i == 1:
            timers.append(end - start)
        else:
            timers.append(timers[-2] + (end - start))
        if len(facto.facto.decimal_to_coefficients(i)) > curr_num_of_digits:
            new_snapshots.append(timers[-4])
            norm_snapshots.append(timers[-3])
            new_snapshots.append(timers[-2])
            norm_snapshots.append(timers[-1])
            curr_num_of_digits += 1
    return new_snapshots, norm_snapshots


if __name__ == '__main__':
    ref = [1, 2, 3]
    start_num = 3
    max_num = 10
    snapshots = list()
    while start_num <= max_num:
        new, norm = snapshots_with_decider(ref)
        snapshots.append([new, norm])
        start_num += 1
        ref.append(start_num)
        print(start_num)
    count = 3
    for i in snapshots:
        fig, ax = plt.subplots()
        y = list()
        for j in range(3, count+1):
            y.append(math.factorial(j)-1)
            y.append(math.factorial(j))
        ax.scatter(y, i[0], label=(str(count) + " NEW__DIGIT_INCREASE"))
        ax.scatter(y, i[1], label=(str(count) + " OLD__DIGIT_INCREASE"))
        ax.legend()
        plt.savefig(str(count) + "OLD&NEW__DIGIT_INCREASE.png")
        count += 1
        plt.show()

# fct1 = facto.Facto(0)
# while perm != perm2:
#     perm = facto.facto.next_permutation(perm)
#     fct1.decimal += 1
#     print(facto.facto.permutation_from_coefficients(reference, fct1.get_coefficients()))
#     print(perm)


# print_hi(facto.next_permutation())
