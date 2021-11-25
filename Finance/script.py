from matplotlib.pyplot import plot
import yfinance as YF
import seaborn
from pandas_datareader import data as pdr
from colorama import Fore
"""
How to use:

	create the analyser instance:
		Analize = Analyzer(symbol, startData: str, endDate: str)

		data format: year-month-day
		to download:

		analize.downloadData()

"""
class Analyser:
	def __init__(self, symbol: str, start: str, end: str) -> None:
		self.symbol = symbol
		self.start = start
		self.end = end
		self.data = pdr.get_data_yahoo(self.symbol, start=self.start, end=self.end)
		print(self.data)
	def downloadData(self):
		self.data.to_csv(f"./{self.symbol}.csv")
		print(f"{Fore.GREEN}Downloaded!")



analize = Analyser("ETH-USD", "2021-11-01", "2021-11-24")
analize.downloadData()