def input_file(path):
    fout = open(path, "w")
    line = input("Enter your strings (to finish entering go to a new line and press Ctrl + X):\n")
    while line != chr(24):
        fout.write(line + "\n")
        line = input()
    fout.close()


def output_file(path):
    print(f"{path} file content:\n")
    fin = open(path,"rt")
    for string in fin:
        print(string, end = "")
    fin.close()


def process_file(path_to_first_file, path_to_second_file, n):
    fin = open(path_to_first_file, "r")
    fout = open(path_to_second_file, "w")
    words = []
    res_words = []
    for line in fin:
        string = line.split()
        for word in string:
            words.append(word)
    for i in words:
        if words.count(i) < n:
            res_words.append(i)
    res_words = sorted(res_words, key = len, reverse = True)
    new_line = "\n".join(res_words)
    fout.write(new_line)
    fin.close()
    fout.close()