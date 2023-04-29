import re

myfile = open("main.pysd", "r")
myline = myfile.readline()
while myline:
    myline = myline.replace("//", "#")
    myline = myline.replace("++", " += 1")
    myline = myline.replace("--", " -= 1")
    myline = myline.replace("NULL", "None")
    myline = myline.replace("<n>", "\n")
    myline = myline.replace("<t>", "\t")
    myline = myline.replace("true", "True")
    myline = myline.replace("false", "False")
    if "include" in myline:
        myline = myline.replace("include<", "import ")
        myline = myline.replace("include <", "import ")
        myline = myline.replace("include", "import")
        myline = myline.replace(">", "")
    if "int " in myline:
        tokens = re.split(" ", myline)
        if type(int(tokens[3])) == "int":
            myline = myline.replace("int ", "")
            exec(myline)
    if "char " in myline:
        tokens = re.split(" ", myline)
        if type(tokens[3]) == "str":
            myline = myline.replace("char ", "")
            exec(myline)
    if "bool " in myline:
        tokens = re.split(" ", myline)
        if type(bool(tokens[3])) == "bool":
            myline = myline.replace("bool ", "")
            exec(myline)
    if "float " in myline:
        tokens = re.split(" ", myline)
        if type(float(tokens[3])) == "float":
            myline = myline.replace("float ", "")
            exec(myline)
    if "list " in myline:
        tokens = re.split(" ", myline)
        if type(list(tokens[3])) == "list":
            myline = myline.replace("list ", "")
            exec(myline)
    myline = myline.replace("list ", "")
    myline = myline.replace("int ", "")
    myline = myline.replace("char ", "")
    myline = myline.replace("bool ", "")
    myline = myline.replace("float ", "")
    exec(myline)
    myline = myfile.readline()
myfile.close()
