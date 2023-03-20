
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
        checkIfInteger(runTime) and \
        len(title) > 0 and \
        len(runTime) > 0:
        runTime = int(runTime)
        return 1
    else:
        return 0
    
def checkInputBookOrReferenceBook(title, author, pages):
    if isinstance(title, str) and \
    isinstance(author, str) and \
    checkIfInteger(pages) and \
        len(title) > 0 and \
        len(author) > 0 and \
            len(pages) > 0:
        pages = int(pages)
        return 1
    else:
        return 0
    
def checkInputEmployee(firstName, lastName):
    if isinstance(firstName, str) and \
    isinstance(lastName, str) and \
        len(firstName) > 0 and \
        len(lastName) > 0:
        return 1
    else:
        return 0
    
def checkManagerIdInput(managerId):
    if checkIfInteger(managerId) and len(managerId) > 0:
        managerId = int(managerId)
        return 1
    else:
        return 0
    
    
def checkIfInteger(value):
    try:
        int(value)
        return 1
    except ValueError:
        return 0



