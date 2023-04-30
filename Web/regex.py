import re
justin=open('mytext.txt','w')
justin.write('my name is mihigo justin')
justin.close()
justin=open('mytext.txt','r')
if re.search('justin',justin.read()):
    justin=open('mytext.txt','r')
    print(justin.read())
    print('yes there is justin in the text document')
else:
    print('there is no justin found')
