# Imports
import os

# Compiler Statements

LAST_CELL = 63
CURRENT_LINE = 0

VARS = {
}

COMMANDS = {
    ":=": "Assign",
    "+": "Add",
    "+=": "AddTo",
    "read": "Read",
    "puts": "Puts",
    "//": "Comment"
    # "+": "Add",
    # "print": "Print",
    # "=": "Equals",
}

# IO functions


def read_input_file(filepath: str):
    with open(filepath) as f:
        lines = f.readlines()
    f.close()
    return lines


def write_output_file(program: str, filepath: str):
    f = open(filepath, "w")
    f.write(program)
    f.close()
    return


# Compiler

def compile(lines: str, name: str, path: str):
    program = f";==={name}===\n"
    for line in lines:
        program += compile_line(line)
    program += 'end'
    write_output_file(program, path)
    pass


def compile_line(line: str):
    global CURRENT_LINE
    CURRENT_LINE += 1

    res = interpret_statement(line)
    return res


def tokenize(line: str):
    tokens = line.split()
    return tokens


def get_last_cell():
    global LAST_CELL
    return f"${LAST_CELL}"


def bump_last_cell(amount: int = 1):
    global LAST_CELL
    LAST_CELL += amount

    if(LAST_CELL > 71):
        raise StopIteration("Ram exceeded")

    return f"${LAST_CELL}"


def create_var(var: str):
    global VARS
    VARS.update({var: bump_last_cell()})
    pass


def get_var(var: str):
    global VARS

    if(var not in VARS):
        raise NotImplementedError("Variable doesn't exist")

    return VARS[var]


def get_or_create_var(var: str):
    global VARS

    if(var not in VARS):
        create_var(var)

    return VARS[var]


def is_num(token: str):
    return token.isnumeric()


# Method execution

def get_method(name: str):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(name)
    if not method:
        raise NotImplementedError(
            f"Error in line {CURRENT_LINE}:\n Method {name} not implemented.")
    return method


def interpret_statement(statement: str):
    tokens = tokenize(statement)
    res = ""

    # if len(tokens) == 1 and not is_num(tokens[0]):
    #         res = f""

    for i in range(len(tokens)):
        if tokens[i].__contains__("//") and not tokens[i] == "//":
            tokens.insert(i+1, tokens[i][2:].strip())
            tokens[i] = "//"

        if tokens[i] in COMMANDS:
            res = COMMANDS[tokens[i]]
            method = get_method(res)
            res = method(statement)
            break

    return res + "\n"

# Commands


def Assign(statement: str):
    tokens = tokenize(statement)
    asm = ""
    # Check Tokens
    if is_num(tokens[0]):
        raise NotImplementedError(
            f"Error in line {CURRENT_LINE}:\n Variable Name incorrect")

    if tokens[1] != ':=':
        raise SyntaxError(f"Command in wrong place")

    if len(tokens[2:]) > 1:
        load = interpret_statement(' '.join(tokens[2:]))
        print(f"Nested: \n{load}")
    else:
        if is_num(tokens[2]):
            load = tokens[2]
        else:
            load = get_var(tokens[2])
        asm = f"ld {load} \n"

    asm += "st "
    asm += get_or_create_var(tokens[0])

    return asm


def Comment(statement: str):
    statement = statement.strip()
    print(statement)
    asm = ""
    if(len(statement) > 2):
        asm = f";{statement[2:]}"
    return asm


def Read(statement: str):
    tokens = tokenize(statement)
    var = get_or_create_var(tokens[1])
    asm = f"in {var}"
    return asm


def Puts(statement: str):
    tokens = tokenize(statement)
    var = get_or_create_var(tokens[1])
    asm = f"out {var}"
    return asm
