# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
num_dict = {}
maxNum = 0

for i in xrange(n):
    x = raw_input().strip().split()
    numX = int(x[0])
    linX = x[1]
    
    if i < n/2:
        linX = "-"
      
    if numX > maxNum:
        maxNum = numX
        
    if numX in num_dict:
        num_dict[numX].append(linX)
    else:
        num_dict[numX] = [linX]
        
    

output = []

for i in xrange(maxNum + 1):
    if i in num_dict:
        for line in num_dict[i]:
            output.append(line)

print " ".join(map(str,output))