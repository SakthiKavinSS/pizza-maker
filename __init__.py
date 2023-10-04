from PizzaFactory import PizzaFactory

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
          print('Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price()))