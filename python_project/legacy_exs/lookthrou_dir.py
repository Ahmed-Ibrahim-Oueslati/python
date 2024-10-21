file_name = input('provide a file name :')
try :
    fhand = open(file_name)
except:
    print("file not found")
    quit()
fread = fhand.read()
print(fread)