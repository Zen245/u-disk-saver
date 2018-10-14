sign_4 = False

try:
    file = open('copy_data.zip')#尝试发送文件，则调用发送模块
    file.close()
    sign_4 = True
    
except FileNotFoundError:#无法找到文件，发送Error邮件
    import fashe_fault_1
except PersmissionError:#文件读取权限不够，发送Error邮件
    import fashe_fault_2
