import statistics
from scipy import stats
from helpers import detect_outliers_iqr
from DateDiff import DateDiff


class RangeDiffAnalyzer:
    def __init__(self, buy_day, sell_day):

        if buy_day <= sell_day:
            raise ValueError("buy_day must be larger than sell_day")
        
        self.buy_day = buy_day          # Days before XDate to buy the Stock
        self.sell_day = sell_day        # Days before XDate to sell the Stock


        #"private" attributes
        self._date_diff_set = []         # This will be an array of DateDiffs
        self._avg_price_change = None
        self._avg_perc_change = None
        self._perc_standard_deviation = None
        self._trimmed_perc_standard_deviation = None #trims outliers
        self._skew = None
        self._kurt = None
        self._date_diff_set_low_outliers = []
        self._date_diff_set_high_outliers = []
        self._data_points = None
        # low streak? high streak? dates in a row that are positive or negative.


    def add_date_diff(self, date_diff):
        self._date_diff_set.append(date_diff)


    def finalize_analyzer(self):
        if self._date_diff_set:

            # Find the average price change
            self._avg_price_change = sum(date_diff.price_change for date_diff in self._date_diff_set) / len(self._date_diff_set)
            # Find the average percentage change
            self._avg_perc_change = sum(date_diff.perc_change for date_diff in self._date_diff_set) / len(self._date_diff_set)

            # Find the Standard Deviation, Skew, and Kurtosis of the percent changes
            perc_changes = [date_diff.perc_change for date_diff in self._date_diff_set]

            self._perc_standard_deviation = statistics.stdev(perc_changes)
            self._trimmed_perc_standard_deviation = stats.tstd(perc_changes)
            self._skew = stats.skew(perc_changes)
            self._kurt = stats.kurtosis(perc_changes)

            # Find the outliers
            self._date_diff_set_low_outliers, self._date_diff_set_high_outliers = detect_outliers_iqr(perc_changes)

            # Find how many data points
            self._data_points = len(self._date_diff_set)



#Below are all the property methods to correctly call the private attributes if needed
    @property
    def date_diff_set(self):
        return self._date_diff_set
    
    @property
    def avg_price_change(self):
        return self.avg_price_change
    
    @property
    def avg_perc_change(self):
        return self.avg_perc_change
    
    @property
    def perc_standard_deviation(self):
        return self._perc_standard_deviation
    
    @property
    def trimmed_perc_standard_deviation(self):
        return self._trimmed_perc_standard_deviation

    @property
    def skew(self):
        return self._skew
    
    @property
    def kurt(self):
        return self._kurt
    
    @property
    def date_diff_set_low_outliers(self):
        return self._date_diff_set_low_outliers
    
    @property
    def date_diff_set_high_outliers(self):
        return self._date_diff_set_high_outliers
    
    @property
    def data_points(self):
        return self._data_points