import numpy as np

def get_numpy_version():
    return np.version.version

def convert_list_to_array(lst):
    converted_arr = np.array(lst)
    print(type(converted_arr))
    return converted_arr

def multiply_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return arr1*arr2

def dot_product(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return np.dot(arr1, arr2)

def sum_arrays(arr, axis=None):
    arr = np.array(arr)
    return np.sum(arr, axis)


if __name__ == "__main__":
    # print(get_numpy_version())
    # print(convert_list_to_array([[1,2,3,4], [4,5,6,7]]))
    # print(multiply_arrays([1,2,3], [4,5,6]))
    # print(dot_product([[1,2,3], [4,5,6]], [4,5,6]))
    print(sum_arrays([[4,5,6], [4,5,6]]))