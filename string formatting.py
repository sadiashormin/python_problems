uinput=raw_input()
n=int(uinput)
width=len(bin(n)[2:])
print width
for i in range(1,n+1):
	print str(i).rjust(width," ") , oct(i)[1:].rjust(width," "), hex(i).upper()[2:].rjust(width," "), bin(i)[2:].rjust(width," ")
