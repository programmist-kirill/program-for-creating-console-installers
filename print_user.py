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
            print(colored('Error git clone ' + url_package,'red'))
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()

        print(colored('end function dowloaded package','green'))


class copy_package:
    def main(name):
        print(colored('start function copy package','green'))
        
        with open('setup_cashe/package/name_package.txt', 'r') as file:
            name_package = file.read().strip()
        
        try:
            ishod_dir = name_package + '/' + name
            copy_dir = 'package/' + name
            print('     => copy ' + name)
            shutil.copytree(ishod_dir, copy_dir)
        except Exception as e:
            print(colored('Error copy package','red'))
            print(e)
            input('\n\nДля продолжения нажмите ENTER')
            sys.exit()

        print(colored('end function copy package','green'))


class install_package:
    def main(name_package):
        if os.path.exists(name_package + '/install.py'):
            print(colored('start function install package','green'))
            try:
                os.system('python install.py')
            except Exception as e:
                print(f"\n" + {e})
                print(colored('\nError install package','red'))
                input('\n\nДля продолжения нажмите ENTER')
                sys.exit()
            print(colored('end function install package','green'))