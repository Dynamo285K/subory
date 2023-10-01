import os

def Folders(path,depth= 0):
    for item in os.listdir(path):
        if os.path.isdir(path+'\\'+item) and item[0] not in '.$':
            print('-'*depth,item)
            if len(os.listdir(path+'\\'+item)) == 0:
                print('-'*depth,item)
            if os.listdir(path+'\\'+item):
                Folders(path+'\\'+item,depth+1)
    # print(os.listdir(path))

Folders('C:\\Riot Games')


