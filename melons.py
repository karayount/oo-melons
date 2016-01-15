"""This file should have our order classes in it."""

import random
import datetime

class AbstractMelonOrder(object):
    """A melon order abstract with attributes, methods common to all orders."""

    def __init__(self, species, qty):
        self.species = species        
        # try:
        #     if qty <= 100:
        #         self.qty = qty
        # except TooManyMelonsError:
        #     raise TooManyMelonsError
        if qty > 100:
            raise TooManyMelonsError()
        else:
            self.qty = qty
        self.shipped = False
        self.order_type = None


    def get_base_price(self):
        """Randomly chooses base price from 5 to 9"""

        base_price = random.randint(5,9)
        now = datetime.datetime.now()

        if now.hour in range(8,11) and now.weekday() in range(0,5): 
            base_price += 4
        
        return base_price


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price
        
        if self.species == "Christmas":
            total *= 1.5
        
        if self.qty < 10 and self.order_type == "international":
            total += 3
        
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0
        self.order_type = "government" 
        self.passed_inspection = False


    def inspect_melons(self, passed):
        """Takes in boolean of ispection passed, returns boolen for inspection passed."""

        if passed == True:
            self.passed_inspection = True


class TooManyMelonsError(ValueError):
    """ Too Many Melons!"""

    def __init__(self):
        super(TooManyMelonsError, self).__init__("No more than 100 melons!")
