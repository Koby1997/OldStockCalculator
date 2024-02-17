class DateDiff:
    def __init__(self, buy_date, sell_date, price_change, perc_change, is_weekend): #may need to change this since the dates are 'private'

        # TODO change how dates are compared. I don't know how Python does that yet
        if buy_date <= sell_date:
            raise ValueError("buy_date must be before sell_date")
        
        # "private" attributes
        self._buy_date = buy_date
        self._sell_date = sell_date

        self.price_change = price_change
        self.perc_change = perc_change
        self.is_weekend = is_weekend


    @property
    def buy_date(self, value):
        # Perform any necessary formatting changes if we need to in the future
        self._buy_date = value


    @property
    def sell_date(self, value):
        # Perform any necessary formatting changes if we need to in the future
        self._sell_date = value




#Below are all the property methods to correctly call the private attributes if needed
    @property
    def buy_date(self):
        return self._buy_date
    
    @property
    def sell_date(self):
        return self._sell_date