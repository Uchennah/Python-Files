import os
os.chdir('C:\\Users\\Stephnie\\Desktop')
file_name ='Message Schedule'
filename = open(file_name, 'r')
for line in filename.readline():
    line = line.strip('\n')
    line = line[::-1]
    print(line)
    filename.close()
    filename = open(file_name, 'a')
    line = line + '\n'
    filename.write(line)
    filename.close()
    filename = open(file_name, 'r')

filename.close()
