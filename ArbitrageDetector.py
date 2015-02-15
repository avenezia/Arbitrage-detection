from CurrencyExchangeReader import CurrencyExchangeReader
import sys

def main():
    reader = CurrencyExchangeReader(sys.argv[1])
    print reader.readData()

if __name__ == '__main__':
    main()
