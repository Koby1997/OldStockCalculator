import statistics
import scipy.stats as stats

class Stock:
    def __init__(self, symbol):
        self._symbol = symbol

        #Which was the best date range
        self._highest_perc_avg = 0

        #single date range gets added to the list        
        self._single_price_change = []
        self._single_perc_change = []

        #Once all the date ranges have been calculated, find the average and save them here
        #Really don't need these but it helps me think
        self._single_avg_price_change = 0
        self._single_avg_perc_change = 0

        #Once the average is found for a single date range, put it in here, reset the variables above
        self._multiple_price_change = []
        self._multiple_perc_change = []

        #How many outliers per date range
        self._low_perc_outliers = []
        self._high_perc_outliers = []

        #Standard Deviation
        self._multiple_SD = []

        #Skewness
        self._multiple_skew = []

        #Kurtosis
        self._multiple_kurt = []

# TODO make a variable to save the highest average

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    @property
    def highest_perc_avg(self):
        return self._highest_perc_avg

    @highest_perc_avg.setter
    def highest_perc_avg(self, value):
        self._highest_perc_avg = value



#Single
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



#Multiple

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

    
    @property
    def multiple_SD(self):
        return self._multiple_SD

    @multiple_SD.setter
    def multiple_SD(self, value):
        self._SD = value

    
    @property
    def multiple_skew(self):
        return self._multiple_skew

    @multiple_skew.setter
    def multiple_skew(self, value):
        self._skew = value


    @property
    def multiple_kurt(self):
        return self._multiple_kurt

    @multiple_kurt.setter
    def multiple_kurt(self, value):
        self._kurt = value




#Outliers

    @property
    def low_perc_outliers(self):
        return self._low_perc_outliers

    @low_perc_outliers.setter
    def low_perc_outliers(self, value):
        self._low_perc_outliers = value


    @property
    def high_perc_outliers(self):
        return self._high_perc_outliers

    @high_perc_outliers.setter
    def high_perc_outliers(self, value):
        self._high_perc_outliers = value

    

#Averages
    def calculate_avg_single_price_change(cls):
        average = sum(cls.single_price_change) / len(cls.single_price_change)
        cls._single_avg_price_change = average
        return average

    
    def calculate_avg_single_perc_change(cls):
        average = sum(cls.single_perc_change) / len(cls.single_perc_change)
        cls._single_avg_perc_change = average
        return average



#Class methods
    def clean_single_data(cls):
        
        #add the averages from the singles to the multiples
        cls.multiple_price_change.append(cls.single_avg_price_change)
        cls.single_avg_price_change = 0

        cls.multiple_perc_change.append(cls.single_avg_perc_change)
        cls.single_avg_perc_change = 0

        #clear the singles lists
        cls.single_price_change.clear()
        cls.single_perc_change.clear()







# Standard deviation
    def standard_deviation(cls):
        sd = statistics.stdev(cls.single_perc_change)
        cls.multiple_SD.append(sd)

# Skewness
    def skewness(cls):
        skew = stats.skew(cls.single_perc_change)
        cls.multiple_skew.append(skew)
    
# Kurtosis
    def kurtosis(cls):
        kurt = stats.kurtosis(cls.single_perc_change)
        cls.multiple_kurt.append(kurt)