import os
from termcolor import colored
import print_user
class Information_package:
    def main():
        directory_is_information_file = input('Введите директорию файла "information" :')
        if os.path.exists(directory_is_information_file):
            with open(directory_is_information_file, 'r') as file:
                lines = file.readlines()
            with open('setup_cashe/package/name_package.txt', 'w') as name_package:
                name_package.write(lines[0])
            with open("setup_cashe/package/version_package.", 'w') as version_package:
                 version_package.write(lines[1])
            with open("setup_cashe/package/url_package.txt", "w") as url_package:
                 url_package.write(lines[2])
            print_user.dowloaded_package.main()
class File_package:
    def main():
        directory_setup_list_file = input('Введите директорию файла "setup.list" :')
        if os.path.exists(directory_setup_list_file):
            with open(directory_setup_list_file, 'r') as file:
                lines = file.read().split("n")
        else:
            print(colored('Отсутствует директория файла "setup.list"','red'))
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()
        try:
            print(colored('\n\n\nstart install package','green'))
            #index = количество строк в файле setup.list
            index_input = len(lines)
            index_input = int(index_input)
            index_output = 0
            while index_input!= index_output:
                if index_input!= index_output:
                    name = lines[index_output]
                    with open('setup_cashe/file', 'w') as fp:
                        fp.write(name)
                    print_user.copy_package.main(name)
                    index_output += 1
        except Exception as e:
            print(colored('Error install package','red'))
            print(e)
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()
    print(colored('end install package','green'))
class Install_package:
    def main():
        print_user.install_package.main()
Information_package.main()
File_package.main()
Install_package.main()
