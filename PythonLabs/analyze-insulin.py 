# Lab118 Preparing to Analyze Insulin with Python
import re 

# ex.2
# Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.
# assigns insulin sequence to a variable. Uses triple quotes("""") because of the line breaks
inSeq = """ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

# cleans string as per instructions using replace, regex is for bonus
inSeqClean = (
    inSeq.replace("ORIGIN", "")
    .replace("61", "") 
    .replace("1", "") # if use this before replacing 61 then would have to replace 6 not 61
    .replace("/", "")
    .replace("\n", "")
    .replace(" ", "") # removed spaces last to keep it simple
)

# seeing if above worked in terminal
print(inSeq)
print(inSeqClean)
print(len(inSeqClean))

# creates file writes content of variable and saves file"
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(inSeqClean)

# In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.
lsinsulin = inSeqClean[0:24] # 24
print(len(lsinsulin))
with open("lsinsulin-seq-clean.txt", "w") as file:
   file.write(lsinsulin)

# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.
binsulin = inSeqClean[24:54] # 30
print(len(binsulin))
with open("binsulin-seq-clean.txt", "w") as file:
   file.write(binsulin)

# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.
cinsulin = inSeqClean[54:89] # 35
print(len(cinsulin))
with open("cinsulin-seq-clean.txt", "w") as file:
   file.write(cinsulin)    

# In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.
ainsulin = inSeqClean[89:110] # 21
print(len(ainsulin))
with open("ainsulin-seq-clean.txt", "w") as file:
   file.write(ainsulin)  

# ex.1 bonus
with open("preproinsulin-seq.txt", "r") as file:
    inSeqR = file.read()
# print(inSeqR)
inSeqCleanR = re.sub("ORIGIN|//|[0-9]|\s", "", inSeqR)
print(inSeqCleanR)
print(len(inSeqCleanR))

# ex.2 bonus
# Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.

# In the VS Code IDE, choose File > New File and save the file as preproinsulin-seq-clean.txt.

# In the file preproinsulin-seq-clean.txt, copy your results.

# Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

# In the VS Code IDE, choose File > New File and save the file as lsinsulin-seq-clean.txt.

# In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

# In the VS Code IDE, choose File > New File and save the file as binsulin-seq-clean.txt.

# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

# In the VS Code IDE, choose File > New File and save the file as cinsulin-seq-clean.txt.

# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

# In the VS Code IDE, choose File > New File and save the file as ainsulin-seq-clean.txt.

# In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.


#  DID IT LIKE THIS FIRST DURING CLASS BC WORRIED ABOUT DOG DURING CLASS
# insulinSeq = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
# insulinSeqClean = insulinSeq.replace(" ", "")
# insulinSeqCleanCount = len(insulinSeqClean)

# print(insulinSeqClean)
# print(insulinSeqCleanCount)

# insulinClean = insulinSeqClean[0:24] # 24
# insulinClean2 = insulinSeqClean[24:54] # 30
# insulinClean3 = insulinSeqClean[54:89] # 35
# insulinClean4 = insulinSeqClean[89:110] # 21
# countOne = len(insulinClean) # 24
# countTwo = len(insulinClean2) # 30
# countThree = len(insulinClean3) # 35
# countFour = len(insulinClean4) # 21

# print(insulinClean)
# print(countOne)

# print(insulinClean2)
# print(countTwo)

# print(insulinClean3)
# print(countThree)

# print(insulinClean4)
# print(countFour)



