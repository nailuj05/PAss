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
            for line in cell["source"]:
                if line.__contains__("# TESTS"):
                    break
                of.write(line)
            of.write('\n\n')

    of.close()


pack()
