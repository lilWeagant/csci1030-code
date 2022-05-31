def traverse(elements, op):
    for element in elements:
        op(element)

def output(x):
    print(x)

traverse([1, 2, 3], output)