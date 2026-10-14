# Lab 122 Calculating the Net Charge of Insulin by Using Python Lists and Loops
# ex.1
# Python3.11
# Coding: utf-8
# Store the human preproinsulin sequen in a variable called preproinsulin:
preproinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y': 10.07,'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# ex.2
# seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
# ^ how exercise said to do it
# seqCount = {x: float(insulin.count(x)) for x in list(pKR.keys())} - how I think it should be done
seqCount = {x: float(insulin.count(x)) for x in pKR} 
# ^ a refactored cleraner way to write it bc list () & .keys() are not needed, looping over a dictionary already gives you the keys


# ex.3
pH = 0
while (pH <= 14): 
    # how the lab said to do it:
    # netCharge = (
    #     +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    #     for x in ['k','h','r']}.values()))
    #     -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    #     for x in ['y','c','d','e']}.values())))
    # same but refactored bc the dictionary comprehension is not needed, a generator inside sum() does the same thing
    netCharge = (
    sum(seqCount[x] * 10**pKR[x] / (10**pH + 10**pKR[x]) for x in 'khr')
    - sum(seqCount[x] * 10**pH / (10**pH + 10**pKR[x]) for x in 'ycde')
)
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1

# with for loop with manual counter instead fo while loop 
# to avoid it becoming an infinite loop & won't need to use pH = 0 or pH +1
for pH in range(15):
    netCharge = (
        sum(seqCount[x] * 10**pKR[x] / (10**pH + 10**pKR[x]) for x in 'khr') 
        - sum(seqCount[x] * 10**pH / (10**pH + 10**pKR[x]) for x in 'ycde')
    )
    print('{0:.2f}'.format(pH), netCharge)

# Result should be for all refactors:
# 0.00 3.999773036108418
# 1.00 3.997731498980362
# 2.00 3.9774281495747488
# 3.00 3.7850011255505267
# 4.00 2.540057926152534
# 5.00 0.4181014741593989
# 6.00 -0.9698633190556047
# 7.00 -2.186629624776233
# 8.00 -4.403272105402016
# 9.00 -7.551924685030059
# 10.00 -9.980672054414311
# 11.00 -12.349327503864025
# 12.00 -13.168625084165932
# 13.00 -13.75988990979344
# 14.00 -13.969868023471733