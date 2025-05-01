# Find unique proteins
#........Program 1: Unique Proteins......................

file_input1 = open('D:\\remma\\New_ECC\\YMBD\\YMBD.txt', 'r')
file_output1 = open('D:\\remma\\New_ECC\\YMBD\\unique.txt', 'w')
p=set()
hold1 = file_input1.readlines()
for line2 in hold1:
    line2=line2.strip('\n')
    str2=line2.split(',')
    for i in range(len(str2)):
        print(str2[i])
        p.add(str2[i])

for line in p:
    file_output1.write(line+'\n')

file_output1.close()
file_input1.close()
