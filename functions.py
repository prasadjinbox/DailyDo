FILEPATH="todos_v1.txt"

def generate_list_todos_from_file(in_filepath=FILEPATH):
    with open(in_filepath, 'r', encoding='utf-8') as f_file1:
        out_todos = f_file1.readlines()
    return out_todos


def write_list_todos_to_file( in_list, in_filepath=FILEPATH ):
    with open(in_filepath, 'w', encoding='utf-8') as f_file2:
        f_file2.writelines(in_list)
print(__name__)
if(__name__ == "__main__"):
    print("I am from functions")


