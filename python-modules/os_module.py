
import os

# print(os.path)

# print(os.getcwd())

os.chdir('/home/zhang/desktop/')

from datetime import datetime

# print(os.getcwd())

# os.mkdir('OS-Demo-2/')
# os.rmdir('OS-Demo-2')

# os.makedirs('OS-Demo-1/Sub-Dir-1')
# os.removedirs('OS-Demo-1/Sub-Dir-1')

# os.rename('test.txt', 'demo.txt')

# print(os.stat('demo.txt').st_size)
# print(os.listdir())

# mod_time = os.stat('demo.txt').st_mtime

# print(datetime.fromtimestamp(mod_time))

# print(os.walk('/home/zhang/desktop/'))
# 
# 
# 
# for dirpath, dirnames, filenames in os.walk('/home/zhang/desktop/'):
#     print('Current Path:', dirpath) 
#     print('Directoies:', dirnames)
#     print('Flies:', filenames)
#     print()
# print(os.environ.get('HOME'))

# file_path = os.environ.get('HOME') + 'text.txt'

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

print(os.path.basename('/path/to/test.txt'))
print(os.path.dirname('/path/to/test.txt'))
print(os.path.split('/pathto/to/test.txt'))
print(os.path.exists('/pathto/to/test.txt'))

print(os.path.isdir('/home/zhang/desktop/wallpaper'))

print(os.path.isfile('/home/zhang/desktop/wallpaper/wallpaper1.jpg'))

print(os.path.splitext('/pathto/to/test.txt'))
