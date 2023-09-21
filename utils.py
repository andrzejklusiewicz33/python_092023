def get_csv(file_name,enc='utf-8',delimiter=';'):
    return [e.strip().split(delimiter) for e in open(file_name,encoding=enc)]

def print_list(data):
    for e in data:
        print(e)