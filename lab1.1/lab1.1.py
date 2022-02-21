from func import *

path_to_first_file = "text.txt"
path_to_second_file = "text_res.txt"

input_file(path_to_first_file)

n = int(input("Enter max word count: "))
print("\n")

output_file(path_to_first_file)
process_file(path_to_first_file, path_to_second_file, n)
print("\n")
output_file(path_to_second_file)
print("\n")
