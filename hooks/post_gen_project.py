import os

os.chdir(os.getcwd())

os.system("npm install")

print('\n\x1b[0;30;42m' + 'Success!' + '\x1b[0m'  + ' Created react-app at', os.getcwd() + '\n')
