from pprint import pprint
from string import ascii_letters
import random
import ast
from time import perf_counter


def read_files_as_content(file_name):
    """
    read string content from file.txt
    """
    with open(file_name, 'r+') as file:

        string = file.read()
    return string



def find_letters(x):
    """
    this func find all letters in file and their frequency as key,val {letter:frequency}
    """
    duplicated_dic = {}

    for char in set(x):
        counts=x.count(char)
        if char not in ["\n" , " "]:
            duplicated_dic[char] = counts
    return  duplicated_dic


def set_key_per_letter(letters):
    """
    set a random value for every letter one by one
    """
    sample_index = 0
    sampled_list = random.sample(ascii_letters, len(letters))
    for k,v in letters.items():
        letters[k] = sampled_list[sample_index]
        sample_index +=1
    return letters

def encrypt_text_letters(content):
    """ 
    encrypt content by set_key_per_letter func
    """
    let = find_letters(content)
    set_keys = set_key_per_letter(let)
    with open("keys.txt", "w") as keys:
        keys.write(str(set_keys))

    for key, val in set_keys.items():
        content = content.replace(key, val)
    return  content, set_keys


def decrypt_text_by_key(encrypted_contnet):
    """
    decrypt content by its unique keys
    """
    enc_dict = {}
    decrypted_content = ''
    with open("keys.txt", "r") as keys:
        keyys = ast.literal_eval(keys.read())

    for ks,vs in keyys.items():
        enc_dict[vs] = ks
        
    for let in encrypted_contnet:
        if let == " ":
            decrypted_content += " "
        else :
            for i,j in enc_dict.items():
                if let == i:
                    decrypted_content += j

    return  decrypted_content


if __name__ == "__main__":

    # here in read_files_as_content you must enter your file1.txt name as a arg 
    # file1.txt contains content that you want encrypt it.
    print( encrypt_text_letters(read_files_as_content("file1.txt"))) 

    # if you want decrypt output  content to origin content you have to pass all contnet as a arg
    #  to  decrypt_text_by_key and uncomment below code .
    # print(decrypt_text_by_key(output_content_as_string))

    # for esimating runtime to encrypt or decrypt content you need do like below:

    """
    start_time = perf_counter()

    codes you want to estiamte

    end_time = perf_counter()

    print(start_time - end_time)


    """

    # and at the end , certainly runtime in long content is bigger than short.
