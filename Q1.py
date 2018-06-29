n=int(input("enter last line you want to read"))
with open ('passage.txt','r')as f:
    a=f.readline()[-n:]
    for line in a:
        print(line)

with open ("passage.txt","r") as f:
    f.read()
    print(f.tell())

