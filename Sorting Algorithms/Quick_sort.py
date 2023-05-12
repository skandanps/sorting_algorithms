import random
import time

# Quick Sort
def quick_sort(arr, start, end):

    if(start < end):
        mid = partition(arr, start, end)
        
        
        quick_sort(arr, start, mid-1)
        quick_sort(arr, mid, end)       

def partition(arr, start, end):
    
    #choosing right most element as pivot
    pivot = arr[end]
    
    i = start - 1
    
    for j in range(start, end):
        if(arr[j] <= pivot):
        
            i += 1            
            (arr[i], arr[j]) = (arr[j], arr[i])
            
    (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
    return i + 1    

def read_file(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        numbers = fileObj.read().split() #puts the file into an array
        fileObj.close()
        return numbers
    
# Driver code to test above
arr_1 = read_file("arr_20.txt")
arr_2 = read_file("arr_100.txt")
arr_3 = read_file("arr_1000.txt")
arr_4 = read_file("arr_4000.txt")

sorted_array_1 = [int(numeric_string) for numeric_string in arr_1]
start_time = time.time()
quick_sort(sorted_array_1, 0, len(sorted_array_1)-1)
end_time = time.time()
time_lapsed = end_time*1000000000 - start_time*1000000000
print("Time taken to sort 20 random integers : ", time_lapsed, " nanoseconds")
print("Sorted array is:")
sorted_list_1 = ' '.join([str(elem) for elem in sorted_array_1])
print(sorted_list_1,"\n")  
 
sorted_array_2 = [int(numeric_string) for numeric_string in arr_2] 
start_time = time.time()
quick_sort(sorted_array_2, 0, len(sorted_array_2)-1)
end_time = time.time()
time_lapsed = end_time*1000000 - start_time*1000000
print("Time taken to sort 100 random integers : ", time_lapsed, " microseconds")
print("Sorted array is:")
sorted_list_2 = ' '.join([str(elem) for elem in sorted_array_2])
print(sorted_list_2,"\n")  

sorted_array_3 = [int(numeric_string) for numeric_string in arr_3]
start_time = time.time()
quick_sort(sorted_array_3, 0, len(sorted_array_3)-1)
end_time = time.time()
time_lapsed = end_time*1000 - start_time*1000
print("Time taken to sort 1000 random integers : ", time_lapsed, " milliseconds")
print("Sorted array is:")
sorted_list_3 = ' '.join([str(elem) for elem in sorted_array_3])
print(sorted_list_3,"\n")  

sorted_array_4 = [int(numeric_string) for numeric_string in arr_4]
start_time = time.time()
quick_sort(sorted_array_4, 0, len(sorted_array_4)-1)
end_time = time.time()
time_lapsed = end_time*1000 - start_time*1000
print("Time taken to sort 4000 random integers : ", time_lapsed, " milliseconds")
print("Sorted array is:")
sorted_list_4 = ' '.join([str(elem) for elem in sorted_array_4])
print(sorted_list_4,"\n")