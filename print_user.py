import os

def main():
    print('start fumct')
    with open('setup.list','r') as file:
        lines = file.readlines()
    
    index_input = len(lines)
    index_input = int(index_input)
    index_output = 0
    while index_input > index_output:
        if index_input >= index_output:
            name = lines[index_output]
            with open('setup_cashe/file' ,'w') as fp:
                fp.write(name)
            index_output += 1

    print('end fumct')