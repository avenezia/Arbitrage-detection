class CurrencyExchange:
    def __init__(self, iFrom, iTo, iRate):
        self.__fromCurrency = iFrom
        self.__toCurrency = iTo
        self.__exchangeRate = iRate

    def __str__(self):
        return self.__fromCurrency + "->" + self.__toCurrency + ": " + self.__exchangeRate

    def __repr__(self):
        return self.__str__()

    @property
    def fromCurrency(self):
        return self.__fromCurrency

    @property
    def toCurrency(self):
        return self.__toCurrency

    @property
    def exchangeRate(self):
        return self.__exchangeRate
