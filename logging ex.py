import logging

logging.basicConfig(level=logging.INFO)

class Apple:   
    def __init__(self, color, weight, size, price):
        self.color = color
        self.weight = weight
        self.size = size
        try:
            self.price = int(price)
        except ValueError as v:
            logging.critical(str(v))
        else:
            logging.info("Successful!!!")

    def __str__(self):
        return "Color: {}, weight: {}, size: {}, price: {}".format(self.color,self.weight,self.size,self.price)

apple1 = Apple("red", 100, 23, 56)
apple2 = Apple("green", 120, 24, 45)
apple3 = Apple("green", 120, 24, '')

print(apple1)
print(apple2)



logging.warning
