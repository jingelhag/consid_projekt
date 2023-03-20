
def getAcronym(stringVariable):
   
    # add first letter
    output = stringVariable[0]
     
    # iterate over string
    for i in range(1, len(stringVariable)):
        if stringVariable[i-1] == ' ':
           
            # add letter next to space
            output += stringVariable[i]
             
    # uppercase oupt
    output = output.upper()
    return str("(" + output + ")")

def checkInputAudioBookorDvd(title, runTime):
    if isinstance(title, str) and \
    checkIfInteger(runTime):
        runTime = int(runTime)
        return 1
    else:
        return 0
    
def checkInputBookOrReferenceBook(title, author, pages):
    if isinstance(title, str) and \
    isinstance(author, str) and \
    checkIfInteger(pages):
        pages = int(pages)
        return 1
    else:
        return 0
    
def checkIfInteger(value):
    try:
        int(value)
        return 1
    except ValueError:
        return 0



