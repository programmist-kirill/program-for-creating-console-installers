import os
import sys
import shutil
from termcolor import colored
class dowloaded_package:
    def main():
        print(colored('start function dowloaded package','green'))
        with open('setup_cashe/package/url_package.txt', 'r') as file:
            url_package = file.read().strip()
        try:
            os.system('git clone ' + url_package)
        except:
            print(colored('Error git clone '+ url_package,'red'))
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()
        print(colored('end function dowloaded package','green'))
class copy_package:
    def main(name):
        with open('setup_cashe/package/name_package.txt', 'r') as name_package:
            name_package = name_package.read().strip()  # удалить символ новой строки
        
        try:
            ishod_dir = name_package + '/' + name
            copy_dir = 'package/' + name
            print('     => copy ' + name)
            shutil.move(ishod_dir, copy_dir)
        except Exception as e:
            print(colored('Error copy package','red'))
            print(e)
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()

class install_package:
    def main():
        with open('setup_cashe/package/name_package.txt', 'r') as name_package:
            name_package = name_package.read().strip('\n')  # удалить символ новой строки
        print(colored('start install package','green'))
        if os.path.exists(name_package + '/install.py'):
            try:
                os.system('python ' + name_package + '/install.py')
            except Exception as e:
                print(f'\n' + {e})
                print(colored('Error install package','red'))
                input('\n\nДля продолжения нажмите ENTER')
                sys.exit()
            print(colored('end install package','green'))
        else:
            if os.path.exists('install'):
                try:
                    os.system('sudo chmod +x \"./install\"')
                    os.system('./install')
                except Exception as e:
                    print(f'\n' + {e})
                    print(colored('Error install package','red'))
                    input('\n\nДля продолжения нажмите ENTER')
                    sys.exit()
                print(colored('end install package','green'))