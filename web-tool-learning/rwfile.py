fw = open('test.txt', 'w')
fw.write('Bui Cong Thanh\n')
fw.write('Xin chao ban!')
fw.close()

fr = open('test.txt', 'r')
text = fr.read()
print(text)
fr.close()