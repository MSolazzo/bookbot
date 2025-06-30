filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words_calc = file_contents.split()
    return len(words_calc)

def count_characters(file_contents):
    final_list = {}
    for letter in file_contents:
        lowercase_let = letter.lower()
        if lowercase_let not in final_list:
            final_list[lowercase_let] = 1
        else:
            final_list[lowercase_let] = final_list[lowercase_let] + 1
    return final_list

def sort_on(let):
    return let["num"]

def organized_list(built_dic):
    sorted_list = []
    for item in built_dic:
        if item.isalpha():
            sorted_list.append({"char": item, "num": built_dic[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


