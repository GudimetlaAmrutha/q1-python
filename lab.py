file1=open("ftemps.txt","w")
tempratures=[int(line.strip())for line in open("temps.txt")]
for t in tempratures:
    print(t*9/5+32,file=file1)
file1.close()
