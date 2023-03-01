class Stock:
    def __init__(self, symbol):
        self._symbol = symbol

        #single date range gets added to the list        
        self._single_price_change = []
        self._single_perc_change = []

        #once all the date ranges have been calculated, find the average and save them here
        self._single_avg_price_change = 0
        self._single_avg_perc_change = 0

        #Once the average is found for a single date range, put it in here, reset the variables above
        self._multiple_price_change = []
        self._multiple_perc_change = []



    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value



#single
    @property
    def single_avg_price_change(self):
        return self._single_avg_price_change

    @single_avg_price_change.setter
    def single_avg_price_change(self, value):
        self._single_avg_price_change = value


    @property
    def single_avg_perc_change(self):
        return self._single_avg_perc_change

    @single_avg_perc_change.setter
    def single_avg_perc_change(self, value):
        self._single_avg_perc_change = value

    

    @property
    def single_price_change(self):
        return self._single_price_change

    @single_price_change.setter
    def single_price_change(self, value):
        self._single_price_change = value


    @property
    def single_perc_change(self):
        return self._single_perc_change

    @single_perc_change.setter
    def single_perc_change(self, value):
        self._single_perc_change = value



#multiple
    @property
    def multiple_avg_price_change(self):
        return self._multiple_avg_price_change

    @multiple_avg_price_change.setter
    def multiple_avg_price_change(self, value):
        self._multiple_avg_price_change = value


    @property
    def multiple_avg_perc_change(self):
        return self._multiple_avg_perc_change

    @multiple_avg_perc_change.setter
    def multiple_avg_perc_change(self, value):
        self._multiple_avg_perc_change = value



    @property
    def multiple_price_change(self):
        return self._multiple_price_change

    @multiple_price_change.setter
    def multiple_price_change(self, value):
        self._multiple_price_change = value


    @property
    def multiple_perc_change(self):
        return self._multiple_perc_change

    @multiple_perc_change.setter
    def multiple_perc_change(self, value):
        self._multiple_perc_change = value

    




    
    def calculate_avg_single_price_change(cls):
        average = sum(cls.single_price_change) / len(cls.single_price_change)
        cls._single_avg_price_change = average
        return average

    
    def calculate_avg_single_perc_change(cls):
        average = sum(cls.single_perc_change) / len(cls.single_perc_change)
        cls._single_avg_perc_change = average
        return average

    # @classmethod
    # def calculate_single_price_decrease_chance(cls):
    #     count_negative = 0
    #     if len(cls.single_price_change) > 0:
    #         for number in cls.single_price_change:
    #             if number < 0:
    #                 count_negative += 1
    #         perc_negative = (count_negative / len(cls.single_price_change)) * 100

    #     cls._single_price_decrease_chance = perc_negative


    


##just realized I don't need these
    
    def calculate_avg_multiple_price_change(cls):
        average = sum(cls.multiple_price_change) / len(cls.multiple_price_change)
        cls._multiple_avg_price_change = average
        return average

    
    def calculate_avg_multiple_perc_change(cls):
        average = sum(cls.multiple_perc_change) / len(cls.multiple_perc_change)
        cls._multiple_avg_perc_change = average
        return average




    
    def clean_single_data(cls):
        #If the averages haven't been calculated for some reason, calculate them
        if cls.single_avg_price_change == 0:
            cls.calculate_avg_single_price_change(cls)
        
        if cls.single_avg_perc_change == 0:
            cls.calculate_avg_single_perc_change(cls)
        
        #add the averages from the singles to the multiples
        cls.multiple_price_change.append(cls.single_avg_price_change)
        cls.single_avg_price_change = 0

        cls.multiple_perc_change.append(cls.single_avg_perc_change)
        cls.single_avg_perc_change = 0

        #clear the singles lists
        cls.single_price_change.clear()
        cls.single_perc_change.clear()


