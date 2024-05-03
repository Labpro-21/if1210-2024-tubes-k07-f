import os


def read_csv_to_list(file_path):
    data = []
    with open(file_path, 'r') as file:
        row = []
        field = ""
        in_quotes = False

        for char in file.read():
            if char == ';' and not in_quotes:
                row.append(field)
                field = ""
            elif char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == '\n' and not in_quotes:
                row.append(field)
                data.append(row)
                row = []
                field = ""
            else:
                field += char

        if field:
            row.append(field)
            data.append(row)

    return data


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

tempFilepath = get_current_directory()
charFilepath = [char for char in tempFilepath]
newcharFilepath = []
for i in (charFilepath):
    if ord(i) != 92:
        newcharFilepath.append(i)
    else:
        newcharFilepath.append("/")
filepath = ("".join(map(str, newcharFilepath)))
file_path = filepath+"/data/user.csv"

csv_data = read_csv_to_list(file_path)
print (csv_data)