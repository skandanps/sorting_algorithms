import random
import time

# Merge Sort
def merge_sort(arr):

    if (len(arr) > 1):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        #recurssive call for both halves
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i in range(0, len(left)) and j in range(0, len(right)):
            if(left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:   
                arr[k] = right[j]
                j += 1
            k += 1
                
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
    
    
        

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
merge_sort(sorted_array_1)
end_time = time.time()
time_lapsed = end_time*1000000000 - start_time*1000000000
print("Time taken to sort 20 random integers : ", time_lapsed, " nanoseconds")
print("Sorted array is:")
sorted_list_1 = ' '.join([str(elem) for elem in sorted_array_1])
print(sorted_list_1,"\n")  
 
sorted_array_2 = [int(numeric_string) for numeric_string in arr_2] 
start_time = time.time()
merge_sort(sorted_array_2)
end_time = time.time()
time_lapsed = end_time*1000000 - start_time*1000000
print("Time taken to sort 100 random integers : ", time_lapsed, " microseconds")
print("Sorted array is:")
sorted_list_2 = ' '.join([str(elem) for elem in sorted_array_2])
print(sorted_list_2,"\n")  

sorted_array_3 = [int(numeric_string) for numeric_string in arr_3]
start_time = time.time()
merge_sort(sorted_array_3)
end_time = time.time()
time_lapsed = end_time*1000 - start_time*1000
print("Time taken to sort 1000 random integers : ", time_lapsed, " milliseconds")
print("Sorted array is:")
sorted_list_3 = ' '.join([str(elem) for elem in sorted_array_3])
print(sorted_list_3,"\n")  

sorted_array_4 = [int(numeric_string) for numeric_string in arr_4]
start_time = time.time()
merge_sort(sorted_array_4)
end_time = time.time()
time_lapsed = end_time*1000 - start_time*1000
print("Time taken to sort 4000 random integers : ", time_lapsed, " milliseconds")
print("Sorted array is:")
sorted_list_4 = ' '.join([str(elem) for elem in sorted_array_4])
print(sorted_list_4,"\n")