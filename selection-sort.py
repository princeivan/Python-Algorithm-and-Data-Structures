# import sys 
# from load  import load_numbers 

# numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list 

def index_of_min(values):
    min_index = 0 
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index 

numbers = [5,6,7,9,2,3,8,1,10,4]
print(selection_sort(numbers))
