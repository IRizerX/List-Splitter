
# IRizerX


loopcount = 1
countline = int(input('Lines Per File : '))
splittedfile = None
with open('IRizerX.txt', 'r') as biglist:
    for linenum, line in enumerate(biglist):
        if linenum % countline == 0:
            if splittedfile:              
                splittedfile.close()
                loopcount+=1
            splittedfile_name = f'list_{loopcount}.txt'
            splittedfile = open(splittedfile_name, "w")
        splittedfile.write(line)        
    if splittedfile:
        splittedfile.close()
input("All Done!")    


 