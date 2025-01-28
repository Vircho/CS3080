import time

def zigzag(lines, shape, wait):

    indent = 0
    indent_increasing = True

    #Ensure correct datatypes
    lines = int(lines)
    shape = str(shape)
    wait = int(wait)

    for i in range(lines):
        print(' ' *indent, end ='')
        print(shape * 8)
        time.sleep(wait)

        if indent_increasing:
            indent = indent + 1
            if indent == 20:
                indent_increasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indent_increasing = True


zigzag(5, '+', 0.1)