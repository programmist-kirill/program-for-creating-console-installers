import os

import print_user

class Information_package:
    def main():
        with open('information', 'r') as file:
            lines = file.readlines()

        with open('setup_cashe/package/name_package.txt', 'w') as name_package:
            name_package.write(lines[0])

        with open('setup_cashe/package/version_package.txt', 'w') as version_package:
            version_package.write(lines[1])
        
        with open('setup_cashe/package/url_package.txt', 'w') as url_package:
            url_package.write(lines[2])


class File_package:
    def main():
        print('start fumct')
        with open('setup.list','r') as file:
            lines = file.readlines()
        #index = количество строк в файле setup.list
        index_input = len(lines)
        index_input = int(index_input)
        index_output = 0
        while index_input != index_output:
            if index_input != index_output:
                name = lines[index_output]
                with open('setup_cashe/file' ,'w') as fp:
                    fp.write(name)
                print_user.main(name)
                
                index_output += 1
        print('end fumct')

File_package.main()