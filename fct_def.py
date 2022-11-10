import matplotlib.pyplot as plt


def writefile(data_to_write):
    with open('test', 'w', encoding='UTF8') as f:
        f.writelines('\n'.join(data_to_write))


def readfile():
    with open('test', 'r', encoding='UTF8') as f:
        return(f.read())