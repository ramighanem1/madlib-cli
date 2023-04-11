def read_template(path):
    try:
        with open(path) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError("Error : file not found")

def parse_template(template):
    parts = []
    stripped = ""
    start = 0
    while True:
        left_brace = template.find("{", start)
        if left_brace == -1:
            stripped += template[start:]
            break
        right_brace = template.find("}", left_brace)
        if right_brace == -1:
            stripped += template[start:]
            break
        parts.append(template[left_brace + 1:right_brace])
        stripped += template[start:left_brace] + "{}"
        start = right_brace + 1
    return stripped, tuple(parts)

def merge(stripped, parts):
    return stripped.format(*parts)


def welcome():
    print('*'*20)
    print("Welcome to the Madlib game")
    print("to create your own text follow instruction")
    print('*'*20)

def user_input(parts):
    user_inputs = []
    for part in parts:
        one_input = input("Please Enter {} : ".format(part))
        user_inputs.append(one_input)
    return user_inputs

def add_to_file(merge_madlib,resultpath1):
    with open(resultpath1, "w") as file:
        file.write(merge_madlib)




if __name__ == "__main__":
    welcome()
    path1="assets/dark_and_stormy_night_template.txt"
    path2="assets/full_text.txt"
    resultpath1="assets/result1.txt"
    resultpath2 = "assets/result2.txt"

    template = read_template(path1)
    # template = read_template(path2)

    stripped, parts = parse_template(template)
    user_inputs = user_input(parts)
    merge_madlib = merge(stripped, user_inputs)
    add_to_file(merge_madlib,resultpath1)
    # add_to_file(merge_madlib,resultpath2)

    print(merge_madlib)
    