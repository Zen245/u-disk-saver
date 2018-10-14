import zipfile
import os 

sign_3 = False

def yasuo():
     """压缩提取出来的文件夹"""
     global sign_3
     # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
     azip = zipfile.ZipFile(r'./copy_data.zip', 'w')
     # 必须保证路径存在,将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
     azip.write(r'./copy_data', compress_type=zipfile.ZIP_LZMA)
     #假设要把一个叫testdir中的文件全部添加到压缩包里（这里只添加一级子目录中的文件）
     if os.path.isdir(r'./copy_data'):  
          for d in os.listdir(r'./copy_data'):  
              azip.write(r'./copy_data'+os.sep+d)  
              # close() 是必须调用的！  
          azip.close()
          sign_3 = True
