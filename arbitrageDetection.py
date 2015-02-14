import re
import sys

def parseCurrencyName(iNameLine):
    currencyCodeNameList = iNameLine.split(" ", 1)
    assert len(currencyCodeNameList) == 2
    return currencyCodeNameList

def parseCurrencyExchangeRate(iRateLine):
    separatorIndex = iRateLine.rfind(" ")
    assert separatorIndex != -1
    currencyCodes = iRateLine[0:separatorIndex]
    exchangeRate = iRateLine[separatorIndex+1:]
    return currencyCodes, exchangeRate

def readDataFromFile(iFileName):
    currencyNameRegEx = re.compile("[A-Z]{3} [A-Z\(\)\.& \-]+")
    currencyExchangeRateRegEx = re.compile("[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
    try:
        fileHandle = open(iFileName, 'r')
        for line in fileHandle.readlines():
            line = line.rstrip("\n")
            if re.match(currencyExchangeRateRegEx, line):
                parseCurrencyExchangeRate(line)
            elif re.match(currencyNameRegEx, line):
                parseCurrencyName(line)
            else:
                raise Exception("Invalid line in file " + iFileName + ": " + line)
        #currencyCodeNameMap = dict()
        #currencyExchangeRateMap = dict()
    except IOError as exception:
        print "Cannot open file " + iFileName + ": " + str(exception)

def main():
    readDataFromFile(sys.argv[1])
    
if __name__ == '__main__':
        main()
