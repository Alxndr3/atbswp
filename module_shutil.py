import shutil
import os


#os.chdir('/home/alexandre')
#shutil.copy('./.vimrc', '/home/alexandre/Documents/delicious')
#shutil.copy('/home/alexandre/.vimrc', '/home/alexandre/Documents/delicious/.vimrc2')
#shutil.copytree('/home/alexandre/.vim', '/home/alexandre/Documents/delicious/.vim_backup')
os.chdir('/home/alexandre/Documents/delicious')
print(os.getcwd())
#os.makedirs('new_dir')
shutil.move('.vim_backup/colors/monokai.vim', 'new_dir/')
shutil.move('.vim_backup/colors/monokai.vim', 'new_dir/new_monokai.vim')
for x in os.listdir():
    print(x)



