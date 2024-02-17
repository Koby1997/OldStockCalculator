from RangeDiffAnalyzer import RangeDiffAnalyzer
from scipy import stats


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol

        self._xdates = []           #Array of ex-dividend dates. May want to differ between old and new.
        self._all_range_diffs = []  #This will be an array of objects from RangeDiffAnalyzer
        self._highest_perc_increase = None


    def add_xdate(self, xdate):
        # Perform any necessary formatting changes if we need to in the future
        self._xdates.append(xdate)


    def add_range_diff(self, range_diff):
        self._all_range_diffs.append(range_diff)


    def finalize_stock(self):
        if self._all_range_diffs:

            #find what range has the highest average percent increase
            highest = 0
            for range_diff in self._all_range_diffs:
                if range_diff.avg_perc_change > highest:
                    highest = range_diff.avg_perc_change




#Below are all the property methods to correctly call the private attributes if needed
    @property
    def xdates(self):
        return self._xdates
    
    @property
    def all_range_diffs(self):
        return self._all_range_diffs
    
    @property
    def highest_perc_increase(self):
        return self._highest_perc_increase