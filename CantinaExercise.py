import json


#reads the file and extracts json components
def jsonReader(filename):
    with open(filename, encoding='utf-8') as data_file:
        jsonData = json.loads(data_file.read())
    return jsonData


#outputs the relevant json data based on the word given by the user
def promptOutput(jsonData, inputWord):
    output = searchWordRecurser(jsonData, inputWord)
    outputList = []
    numInputClass = 0

    if (inputWord == "classNames"):
        for sublist in output:
            for curr in sublist:
                outputList.append(curr)

    else:           
        for curr in output:
            outputList.append(curr)
            if curr == "Input":
                numInputClass = numInputClass + 1

    print(outputList)
    print("")
    
    if (inputWord == "class"):
        print("Number of Classes called 'Input' (Test to ensure correctness)")
        print(numInputClass)
    return


#outputs all the possible json data points the user would otherwise see separately
#extra functionality, more so for testing purposes
def promptAllOutput(jsonData):
    outputClass = searchWordRecurser(jsonData, "class")
    outputNames = searchWordRecurser(jsonData, "classNames")
    outputIdents = searchWordRecurser(jsonData, "identifier")
    outputList = []
    for curr in outputClass:
        outputList.append(curr)
    for sublist in outputNames:
            for curr in sublist:
                outputList.append(curr)
    for curr in outputIdents:
        outputList.append(curr)
    print(outputList)
    return
    
    
#looks for the relevant data points based on the selector the user chose
def searchWordRecurser(jsonData, userInput):
    
    #check if data is list type
    #recursively checks subgroups, yield matching data points to user input
    if (isinstance(jsonData, list)):
        for dataPoint in jsonData:
            for children in searchWordRecurser(dataPoint, userInput):
                yield children
                
    #check if data is dictionary type 
    #recursively check subgroups, yield matching data points to user input
    elif (isinstance(jsonData, dict)):
        for currWord, nestedData in jsonData.items():
            if currWord == userInput:
                yield nestedData
            for jsonDataPoint in searchWordRecurser(nestedData, userInput):
                yield jsonDataPoint
                
    else:
        return
    return

#main method, user is consistently prompted to select a selector
def main():  
    cantinaData = jsonReader('SystemViewController.json')
    
    userAnswer = "";
    print("Welcome!")
    print("Please select the type that you would like to see.")
    print("Your options: 'class', 'classNames', 'identifier', 'all' or enter 'exit' if you wish to end the program.")
    print("")
    

    #consistently prompt for user input until the user exits
    while userAnswer != "exit":
        
        userAnswer = input("Please enter your answer: ")
        userAnswer = userAnswer.lower()
        print("")

        if userAnswer == "class":
            promptOutput(cantinaData, userAnswer)
            
        elif userAnswer == "classnames":
            userAnswer = "classNames"
            promptOutput(cantinaData, userAnswer)
            
        elif userAnswer == "identifier":
            promptOutput(cantinaData, userAnswer)

        elif userAnswer == "all":
            promptAllOutput(cantinaData)
            
        elif userAnswer == "exit":
            print("Thank you for your participation. Have a nice day!")
            break;

        else:
            print("Not valid. Try Again!")
        
    
#needed so that main method is run when program is run
if __name__ == "__main__":
    main()





