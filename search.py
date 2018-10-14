import shutil,os,re

sign_2 = False

def search():
    """查找拥有所要求的后缀名的文件并把它提取到新文件夹中"""
    global sign_2
    #新建文件夹
    new_path='./copy_data'
    os.makedirs(new_path)
    #遍历查找所有符合要求的文件
    for derName, subfolders, filenames in os.walk('data'):
        #print(derName/subfolders/filenames)
        for i in range(len(filenames)):
            if (filenames[i].endswith('.txt')
                or filenames[i].endswith('.xlsx')
                or filenames[i].endswith('.ppt')
                or filenames[i].endswith('.pptx')
                or filenames[i].endswith('.xls')
                or filenames[i].endswith('.doc')
                or filenames[i].endswith('.docx')
                or filenames[i].endswith('.pdf')
                or filenames[i].endswith('.py')
                or filenames[i].endswith('.jpg')
                or filenames[i].endswith('.png')
                ):
                file_path = derName + '/' +filenames[i]
                shutil.copy(file_path, new_path)
                sign_2 = True
