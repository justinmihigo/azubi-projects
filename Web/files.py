import os
if os.path.exists('justin.txt'):
    os.remove('justin.txt')
else:
    print('file is not found')