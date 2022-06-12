import os
import json


def pack():
    # Get Global Paths
    dev_path = os.path.dirname(__file__) + "\\dev.ipynb"
    pass_path = os.path.dirname(__file__) + "\\PAss.py"

    # Compile .py
    f = open(dev_path, "r")
    j = json.load(f)
    of = open(pass_path, 'w')
    if j["nbformat"] >= 4:
        for i, cell in enumerate(j["cells"]):
            of.write("#cell "+str(i)+"\n")
            for line in cell["source"]:
                of.write(line)
            of.write('\n\n')
    else:
        for i, cell in enumerate(j["worksheets"][0]["cells"]):
            of.write("#cell "+str(i)+"\n")
            for line in cell["input"]:
                of.write(line)
            of.write('\n\n')

    of.close()


pack()
