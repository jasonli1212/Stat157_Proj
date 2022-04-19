import pandas
import random
from itertools import permutations

def toCode(df = None, num = 200, path = None):
	f = open(path, "a")
	leng = len(df)
	orders = list(range(leng))
	random.shuffle(orders)
	for i in range(num):
		index = orders[i]
		df.iat[0,0]
		name = df2.iat[i,0]
		image = df2.iat[i, 1]
		price = df2.iat[i, 2].replace('$', '')
		out = '\t*group\n' + '\t\t>>price = ' + price + '\n\t\t*image: ' + image + '\n' + '\t\t*question: What is the Price?' + '\n\t\t\t*save: output\n' + '\t\t\t*type: number\n' + '\t\t\t*tip: Name of the product: ' + name + '\n' + '\t\t\t*before: $\n'
		f.write(out)
	f.close()

df = pandas.read_csv('Datas.csv')


df2 = df.loc[:, ["Product Name", "Image", "Selling Price"]]


f = "the_Code.txt"
toCode(df2, 500, f)

