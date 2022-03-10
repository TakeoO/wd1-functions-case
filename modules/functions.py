def cleanString(string):
    newString = string.strip()
    specialSigns = [" ", "-", "/", "\\"]

    for sign in specialSigns:
        newString = newString.replace(sign, "_")

    newString = newString.lower()
    return newString


def getPriceWithVAT(price, rate):
    if rate in [1.22, 1.095]:
        return price * rate
    else:
        return price


def parseFileContent(fileName):
    file = open(fileName)
    fileContent = file.read()
    file.close()
    return fileContent.split("\n")


def parseCSVLines(lines):
    data = []
    for line in lines:
        lineItems = line.split(";")
        data.append(lineItems)

    keys = data[0]
    rows = data[1:]
    return {
        "rows": rows,
        "keys": keys
    }


def parseCsvFile(fileName):
    lines = parseFileContent(fileName)
    data = parseCSVLines(lines)

    dictionaries = []

    for row in data["rows"]:
        newDictionary = {}
        for index in range(len(data["keys"])):
            cleanedKey = cleanString(data["keys"][index])
            newDictionary[cleanedKey] = row[index]
        dictionaries.append(newDictionary)
    return dictionaries
