# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import goodPractise.prime_num_finder as chec
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    start = time.time()
    bewlist = chec.func_get_prime(100000000)
    print(list(bewlist))
    end = time.time()
    print(f"运行耗时:{end - start}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
