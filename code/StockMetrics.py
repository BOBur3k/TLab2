
import statistics as stats

from code.StockData import StockData

class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        averages = []
        for row in self.data:
            values = []
            for val in row[0:]: 
                try: 
                    num = float(val)
                    values.append(num)
                except ValueError:
                    pass
            if values: 
                avg = round(sum(values)/len(values), 3)
                averages.append(avg)  
        return averages

      
    def median02(self):
        
        medians = []
        for row in self.data[0:]:
            values = []
            for val in row: 
                try: 
                    num = float(val)
                    values.append(num)
                except ValueError:
                    pass
            if values: 
                data = sorted(values)
                data1 = len(data)
                middle = (data1 - 1) // 2
                if data1 % 2 == 1: 
                    median = round(data[middle], 6)
                else:
                    median = round((data[middle] + data[middle + 1]) / 2, 6)
                medians.append(median)
            else:
                medians.append(0.0)
        return medians
                

    def stddev03(self):
        """pt3
        """
        stdev3 = []
        for row in self.data[0:]:
            values = []
            for val in row: 
                try: 
                    num = float(val)
                    values.append(num)
                except ValueError:
                    pass
            if len(values):
                n = len(values)
                mean = sum(values) / n
                deviations = [(x - mean) ** 2 for x in values]
                variance = sum(deviations) / (n - 1)
                stdev = (variance ** 0.5)
                stdev3.append(round(stdev, 3))
            else: 
                stdev3.append(0.0)
        return stdev3