import unittest
from datetime import datetime


# Symbol validation function 

def is_valid_symbol(symbol):
    """
    Validate stock symbol.
    - Capitalized
    - 1-7 alpha characters
    """
    
    
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

## Symbol validation test

class TestSymbolValidation(unittest.TestCase):
    """Test cases for validating stock symbols."""
    def test_symbol(self):
        valid_symbols = ["YHOO", "YUM", "ZMH", "ZION", "MSFT", "WFM"]
        invalid_symbols = ["cole", "000", "COLE0", "COLECAAFGD", ""]

        for symbol in valid_symbols:
            self.assertTrue(is_valid_symbol(symbol), f"Expected {symbol} to be valid.")

        for symbol in invalid_symbols:
            self.assertFalse(is_valid_symbol(symbol), f"Expected {symbol} to be invalid.")


# Chart Type validation function
 
def is_valid_chart_type(chart_type):
    """
    Validate chart type.
    - 1 numeric character
    - 1 or 2
    """
    return chart_type in {"1", "2"}

## Chart type validation test

class TestChartTypeValidation(unittest.TestCase):
    """Test cases for validating chart types."""
    def test_chart_type(self):
        valid_chart_types = ["1", "2"]
        invalid_chart_types = ["3", "0", "bar", "", "12"]

        for chart_type in valid_chart_types:
            self.assertTrue(is_valid_chart_type(chart_type), f"Expected {chart_type} to be valid.")

        for chart_type in invalid_chart_types:
            self.assertFalse(is_valid_chart_type(chart_type), f"Expected {chart_type} to be invalid.")


# Time series validation function 

def is_valid_time_series(time_series):
    """
    Validate time series.
    - 1 nummeric character
    - 1-4
    """
    return time_series in {"1", "2", "3", "4"}

## Time series validation test

class TestTimeSeriesValidation(unittest.TestCase):
    """Test cases for validating time series."""
    def test_time_series(self):
        valid_time_series = ["1", "2", "3", "4"]
        invalid_time_series = ["5", "0", "daily", ""]

        for time_series in valid_time_series:
            self.assertTrue(is_valid_time_series(time_series), f"Expected {time_series} to be valid.")

        for time_series in invalid_time_series:
            self.assertFalse(is_valid_time_series(time_series), f"Expected {time_series} to be invalid.")


# Date Validation Function and Tests
def is_valid_date(date_string):
    """
    Validate date format.
    - date type YYYY-MM-DD
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class TestDateValidation(unittest.TestCase):
    """Test cases for validating dates."""
    def test_start_date(self):
        valid_dates = ["2024-01-01", "2023-12-31"]
        invalid_dates = ["01-01-2024", "2024/01/01", "20240101", ""]

        for date in valid_dates:
            self.assertTrue(is_valid_date(date), f"Expected {date} to be valid.")

        for date in invalid_dates:
            self.assertFalse(is_valid_date(date), f"Expected {date} to be invalid.")


# Date range validation function 
def is_valid_date_range(start_date, end_date):
    """
    Validate that the date range.
    - Must pass date validation test for starting date and end date
    - start date must be before end date
    """
    if not (is_valid_date(start_date) and is_valid_date(end_date)):
        return False
    return datetime.strptime(start_date, "%Y-%m-%d") < datetime.strptime(end_date, "%Y-%m-%d")

 ## Date range validation tests
class TestDateRangeValidation(unittest.TestCase):
    """Test cases for validating date ranges."""
    def test_end_date(self):
        valid_date_ranges = [("2021-03-28", "2021-04-28"), ("2022-02-14", "2023-02-14")]
        invalid_date_ranges = [("2021-04-28", "2021-03-28"), ("2023-02-14", "2022-02-14"), ("2024-03-28", ""), ("", "2024-04-28")]

        for start_date, end_date in valid_date_ranges:
            self.assertTrue(is_valid_date_range(start_date, end_date), f"Expected range {start_date} to {end_date} to be valid.")

        for start_date, end_date in invalid_date_ranges:
            self.assertFalse(is_valid_date_range(start_date, end_date), f"Expected range {start_date} to {end_date} to be invalid.")


# Run Tests
if __name__ == "__main__":
    unittest.main()