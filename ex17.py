# exists(file) 判断文件是否存在
# open(file[, mode])  第二个参数可选择读写模式，默认为只读模式，'w'为写入模式（不可读），'w+'为读写模式
# 写模式（'w'或'w+'）会清空原始文件内容

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

fromFile = open(from_file)
fromData = fromFile.read()

print(f"The input file is {len(fromData)} bytes long")

print(f"Does the output file exist? {exists(to_file)}") # exists(file) 判断文件是否存在
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input('?')

toFile = open(to_file, 'w+') # 'w'为写入模式（不可读），'w+'为读写模式，默认为只读模式
print('toFile: ', toFile.read()) # 输出为空
toFile.write(fromData)

print("Alright, all done.")

toFile.close()
fromFile.close()