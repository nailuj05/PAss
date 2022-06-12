# Imports
import os

# Compiler Statements

LAST_CELL = 63

VARS = {
}

COMMANDS = {
    "TEST": "Test",
    ":=": "Assign",
    "read": "Read",
    "puts": "Puts",
    #"+": "Add",
    #"print": "Print",
    #"=": "Equals",
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
        raise NotImplementedError("Method %s not implemented" % name)
    return method


def interpret_statement(statement: str):
    tokens = tokenize(statement)

    if tokens[0] == tokens[1] == "/":
        res = f";{tokens[1:]}"

    for token in tokens:
        if token in COMMANDS:
            res = COMMANDS[token]
            break

    # if len(tokens) == 1 and tokens[0] in VARS:
    #     res = 

    if not res:
        print("No command or variable in statement")
        return ""

    method = get_method(res)
    res = method(statement)
    if not res:
        res = ""
    return res + "\n"

# Commands

def Assign(statement: str):
    tokens = tokenize(statement)
    # Check Tokens
    if is_num(tokens[0]):
        raise NotImplementedError("Variable Name incorrect")

    if is_num(tokens[2]):
        load = tokens[2]
    else:
        load = get_var(tokens[2])

    asm = f"ld {load} \n"
    asm += "st "
    asm += get_or_create_var(tokens[0])
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

def Test(statement: str):
    return "Test"



