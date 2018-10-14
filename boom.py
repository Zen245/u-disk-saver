import os
import shutil

a = True
while (a == True):
    delList_1 = []
    delDir_1 = r"./copy_data"
    delList_1 = os.listdir(delDir_1) #返回指定的文件夹包含的文件或文件夹的名字的列表
    for f_1 in delList_1:
        filePath_1 = os.path.join(delDir_1, f_1 ) #拼接，把目标文件夹下的目录和文件名合成一个路径
        if os.path.isfile(filePath_1): #判断目标路径下是否为文件
            os.remove(filePath_1)
            a = False
        elif os.path.isdir(filePath_1):
            shutil.rmtree(filePath_1, True)
            a = False


b = True
while (b == True):
    delList_2 = []
    delDir_2 = r"./data"
    delList_2 = os.listdir(delDir_2) 
    for f_2 in delList_2:
        filePath_2 = os.path.join(delDir_2, f_2 ) 
        if os.path.isfile(filePath_2): 
            os.remove(filePath_2)
            b = False
        elif os.path.isdir(filePath_2):
            shutil.rmtree(filePath_2, True)
            b = False
            
os.rmdir(delDir_1)
os.rmdir(delDir_2)
os.remove('copy_data.zip')

