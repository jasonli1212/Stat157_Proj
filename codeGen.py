import pandas
import random
from itertools import permutations

def toCode(df = None, num = 200, path = None):
	f = open(path, "a")
	leng = len(df)
	orders = list(range(leng))
	random.shuffle(orders)
	for i in range(num):
		df.iat[0,0]
		name = df2.iat[i,0]
		image = df2.iat[i, 1]
		price = df2.iat[i, 2].replace('$', '')
		label = '\n\t\t*Name of the product: ' + name + '*' + '\n\t\t*image: ' + image
		out = '\t*group\n' + '\t\t>>price = ' + price + label +\
		 '\n' + '\t\t*question: My 80% confidence interval for LOWER bound is ... ' + \
		  '\n\t\t\t*tip: the LOWER BOUND.' + '\n\t\t\t*save: L' + '\n\t\t\t*type: number' + '\n' + \
		 label + '\n' +  \
		 '\t\t*question: My 80% confidence interval for UPPER bound is ... ' + \
		 '\n\t\t\t*tip: the UPPER BOUND. ' + '\n\t\t\t*save: U' + '\n\t\t\t*type: number' + '\n'

		f.write(out)
	f.close()

df = pandas.read_csv('out2.csv')


df2 = df.loc[:, ["Product Name", "Image", "Selling Price"]]



f = "the_Code.txt"
toCode(df2, 200, f)
# df.sample(frac=1).to_csv('./out.csv')


