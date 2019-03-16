from string import Template

class MyTemplate(Template):
        delimiter="#"
def Main():
	cart = []
	cart.append(dict(item="Coke", price=8, quality=2))
	cart.append(dict(item="Cake", price=12, quality=1))
	cart.append(dict(item="Fish", price=32, quality=4))
	t = MyTemplate("#quality x #item = #price")
	total = 0
	print("Cart:")
	for data in cart:
		print(t.substitute(data))
		total += data["price"]
	print("Total: "+str(total))

if __name__ == '__main__':
        Main()

		
		
