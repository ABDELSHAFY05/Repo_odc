#with open('attendence.csv','r') as in_file, open('ouput.csv','w+') as out_file:
  
    #seen = set() # set for fast O(1) amortized lookup
    
    #for line in in_file:
        ##if line in seen:
          #continue # skip duplicate

        #seen.add(line)
        #out_file.write(line)
import fileinput
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('ouput.csv', inplace=1):
    if line not in seen:
        seen.add(line)
        print (line) # standard output is now redirected to the file