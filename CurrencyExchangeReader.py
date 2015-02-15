import re
from CurrencyExchange import CurrencyExchange

class CurrencyExchangeReader:

    def __init__(self, iFileName):
        self.__fileName = iFileName

    def parseCurrencyName(self, iNameLine):
        currencyCodeNameList = iNameLine.split(" ", 1)
        assert len(currencyCodeNameList) == 2
        return currencyCodeNameList

    def parseCurrencyExchangeRate(self, iRateLine):
        exchangeInfoList = iRateLine.split(" ", 2)
        assert len(exchangeInfoList) == 3
        return CurrencyExchange(*exchangeInfoList)

    def readData(self):
        currencyNameRegEx = re.compile("[A-Z]{3} [A-Z\(\)\.& \-]+")
        currencyExchangeRateRegEx = re.compile("[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        currencyCodeNameMap = {}
        currencyExchangeRateList = []
        try:
            fileHandle = open(self.__fileName, 'r')
            for line in fileHandle.readlines():
                line = line.rstrip("\n\r")
                if re.match(currencyExchangeRateRegEx, line):
                    currencyExchangeRateList.append(self.parseCurrencyExchangeRate(line))
                elif re.match(currencyNameRegEx, line):
                    currencyCode, currencyName = self.parseCurrencyName(line)
                    currencyCodeNameMap[currencyCode] = currencyName
                else:
                    raise Exception("Invalid line in file " + self.__fileName + ": " + line)
        except IOError as exception:
            print "Cannot open file " + self.__fileName + ": " + str(exception)

        return currencyCodeNameMap, currencyExchangeRateList
