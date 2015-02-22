import argparse
from CurrencyExchangeReader import CurrencyExchangeReader
import graph_tool
import graph_tool.draw
import graph_tool.search
import math
import sys

class ArbitrageDetector:
    def __init__(self, iDataFile):
        self.__exchangeRateGraph = graph_tool.Graph()
        # The map between a currency (e.g EUR) and the corresponding vertex in the graph
        self.__currencyCodeVertexMap = {}
        # The property map containing the label for each vertex
        self.__vertexLabelPropertyMap = self.__exchangeRateGraph.new_vertex_property("string")
        # The property map containing -ln(exchange rate) for the edge connecting two currencies
        self.__exchangeRatePropertyMap = self.__exchangeRateGraph.new_edge_property("float")
        self.__currencyDataReader = CurrencyExchangeReader(iDataFile)

    def detectArbitrage(self):
        currencyCodeNameMap, currencyExchangeRateList = self.__currencyDataReader.readData()
        for currencyCode in currencyCodeNameMap.keys():
            # Creating the vertex for the currency
            currencyVertex = self.__exchangeRateGraph.add_vertex()
            self.__currencyCodeVertexMap[currencyCode] = currencyVertex
            self.__vertexLabelPropertyMap[currencyVertex] = currencyCode

        for currencyExchange in currencyExchangeRateList:
            if self.isValidCurrencyExchange(currencyExchange):
                fromVertex = self.__currencyCodeVertexMap[currencyExchange.fromCurrency]
                toVertex = self.__currencyCodeVertexMap[currencyExchange.toCurrency]
                edge = self.__exchangeRateGraph.add_edge(fromVertex, toVertex)
                self.__exchangeRatePropertyMap[edge] = -math.log(currencyExchange.exchangeRate)

        allEdgesAreMinimized, distanceMap, predecessorsMap = graph_tool.search.bellman_ford_search(self.__exchangeRateGraph,
            self.__exchangeRateGraph.vertex(0), self.__exchangeRatePropertyMap, infinity=200000000.0)
        return allEdgesAreMinimized

    def isValidCurrencyExchange(self, iCurrencyExchange):
        return (iCurrencyExchange.fromCurrency != iCurrencyExchange.toCurrency and
            iCurrencyExchange.exchangeRate > 0)

def parseCommandLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("currencyExchangeFile", type=str, help="The file containing currency exchange rates")
    args = parser.parse_args()
    return args.currencyExchangeFile

def main():
    arbitrageDetector = ArbitrageDetector(parseCommandLineArgs())
    arbitrageDetector.detectArbitrage()

if __name__ == '__main__':
    main()
