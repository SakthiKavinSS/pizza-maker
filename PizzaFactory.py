from DeluxePizza import DeluxePizza
from HamAndMushroomPizza import HamAndMushroomPizza
from HawaiianPizza import HawaiianPizza

class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()