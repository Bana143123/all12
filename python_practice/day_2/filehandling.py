#open a file for reading
file=open("handle_fil.txt","r")
fin=file.read()
#print(fin)
#open a file for writing(creates the file if it doesn't exists)
fie=open("handle_fi.txt","w")
fie.write('Hi hello namaste\ngd mrng\n')
# Write multiple lines
lines = ['First line\n', 'Second line\n', 'Third line\n']
fie.writelines(lines)
# Check if the file is writable
if fie.writable():
    fie.write('This is writable\n')
    fie.flush()#it ensures immediate output

#open a file for appending(creates the file if it doesn't exists)
fil=open("han.txt","a")
# Move cursor to the specific position using seek
file.seek(0)
con=file.read()
print(con)
print()
#read a single line
file.seek(10)
sing=file.readline()
print(sing)
# Get the current cursor position
position = file.tell()
print(position)
#read all the lines into list
all=file.readlines()
#print(all)
#closing a file
file.close()
