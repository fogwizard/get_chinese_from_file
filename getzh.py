import os
import sys
import codecs
#input file should be ISO8859 text file

def get_gb2312_one_file(fin, outf):
	with open(fin) as f:
		lines = f.read()
	save_next = False
	for i in range(len(lines)):
		if(save_next):
			outf.write((lines[i]));
			save_next = False
		elif(ord(lines[i]) >= 0xa0):
			outf.write((lines[i]));
			save_next = True 
			print(ord(lines[i]),ord(lines[i+1]))
pass

with open('gb2312.txt', "wb") as fgb2312: 
	for i in sys.argv[1:]:
		get_gb2312_one_file(i, fgb2312)

fin  = open("gb2312.txt", 'r')
fout = open("utf8.txt", 'w')

reader = codecs.getreader('gb2312')(fin)
writer = codecs.getwriter('utf-8')(fout)

data = reader.read(2)
while data:
	writer.write(data)
	data = reader.read(2)
fin.close()
fout.close()

