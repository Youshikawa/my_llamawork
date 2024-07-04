def remove_empty_lines_and_spaces(input_file, output_file):  
    with open(input_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as outfile:  
        for line in file:  
            # 去除行首和行尾的空格  
            line = line.strip()  
            # 如果行不为空，则写入新文件  
            if line:  
                outfile.write(line + '\n')  
  
# 使用函数  
input_file = '/home/yzc/llamawork/YuLiao.txt'  # 输入文件名  
output_file = '/home/yzc/llamawork/YuLiao.txt.txt'  # 输出文件名，可以是同一个文件名以覆盖原文件  
remove_empty_lines_and_spaces(input_file, output_file)