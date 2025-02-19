import unittest
from api_call import schedule_calls, call_api

class TestAPICall(unittest.TestCase):
#Test scheduling API calls for future timestamps
    def test_schedule_calls_future(self): 
        timestamps = ["19:35:00", "19:36:00"]
        schedule_calls(timestamps)

#Test  past timestamps raise an error
    def test_schedule_calls_past(self):
        timestamps = ["00:00:01", "00:00:02"] 
        with self.assertRaises(ValueError) as context:
            schedule_calls(timestamps)
        self.assertIn("is in the past", str(context.exception))

##Test timestamps with invalid format
    def test_schedule_calls_invalid_format(self):
        timestamps = ["12:61:00", "abc"]
        with self.assertRaises(ValueError) as context:
            schedule_calls(timestamps)
        self.assertIn("Invalid timestamp format", str(context.exception))

  

if __name__ == "__main__":
    unittest.main()
