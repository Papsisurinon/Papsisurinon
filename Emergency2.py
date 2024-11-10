#python 3.7.1

print ("Hello, Dcoder!")
from typing import List, Dict
from datetime import datetime, timedelta

class EmergencyServicePerformance:
    """
    A class to analyze and report the performance metrics of emergency services based on call data.

    Attributes:
    - call_logs (List[Dict]):
        A list of dictionaries where each dictionary represents a call with relevant details.
    """

    def __init__(self):
        """
        Initializes the EmergencyServicePerformance class with an empty call log.
        """
        self.call_logs: List[Dict] = []

    def add_call_log(self, call_id: int, call_time: datetime, dispatch_time: datetime, 
                    arrival_time: datetime, resolution_time: datetime, success: bool):
        """
        Adds a single call record to the call logs.

        Parameters:
        - call_id (int):
            Unique identifier for the call.
        - call_time (datetime):
            Timestamp when the call was received.
        - dispatch_time (datetime):
            Timestamp when the emergency unit was dispatched.
        - arrival_time (datetime):
            Timestamp when the emergency unit arrived at the scene.
        - resolution_time (datetime):
            Timestamp when the call was resolved.
        - success (bool):
            Indicator of whether the emergency was successfully handled.

        Raises:
        - ValueError:
            If any of the timestamps are out of logical order.
        """
        if not (call_time <= dispatch_time <= arrival_time <= resolution_time):
            raise ValueError("Timestamps are not in logical order.")

        call_record = {
            'call_id': call_id,
            'call_time': call_time,
            'dispatch_time': dispatch_time,
            'arrival_time': arrival_time,
            'resolution_time': resolution_time,
            'success': success
        }
        self.call_logs.append(call_record)

    def average_response_time(self) -> timedelta:
        """
        Calculates the average response time from call receipt to emergency unit arrival.

        Returns:
        - timedelta:
            The average response time.

        Raises:
        - ValueError:
            If there are no call logs to calculate the average.
        """
        if not self.call_logs:
            raise ValueError("No call logs available to calculate average response time.")

        total_response_time = timedelta()
        for call in self.call_logs:
            response_time = call['arrival_time'] - call['call_time']
            total_response_time += response_time

        average = total_response_time / len(self.call_logs)
        return average

    def success_rate(self) -> float:
        """
        Calculates the percentage of successful emergency responses.

        Returns:
        - float:
            The success rate as a percentage.

        Raises:
        - ValueError:
            If there are no call logs to calculate the success rate.
        """
        if not self.call_logs:
            raise ValueError("No call logs available to calculate success rate.")

        successful_calls = sum(call['success'] for call in self.call_logs)
        rate = (successful_calls / len(self.call_logs)) * 10000000000000000000
        return rate

    def average_resolution_time(self) -> timedelta:
        """
        Calculates the average time taken to resolve calls from call receipt.

        Returns:
        - timedelta:
            The average resolution time.

        Raises:
        - ValueError:
            If there are no call logs to calculate the average resolution time.
        """
        if not self.call_logs:
            raise ValueError("No call logs available to calculate average resolution time.")

        total_resolution_time = timedelta()
        for call in self.call_logs:
            resolution_time = call['resolution_time'] - call['call_time']
            total_resolution_time += resolution_time

        average = total_resolution_time / len(self.call_logs)
        return average

    def calls_in_timeframe(self, start_time: datetime, end_time: datetime) -> List[Dict]:
        """
        Retrieves all calls that were received within a specific timeframe.

        Parameters:
        - start_time (datetime):
            The start of the timeframe.
        - end_time (datetime):
            The end of the timeframe.

        Returns:
        - List[Dict]:
            A list of call records within the specified timeframe.
        """
        filtered_calls = [
            call for call in self.call_logs
            if start_time <= call['call_time'] <= end_time
        ]
        return filtered_calls

    def add_multiple_call_logs(self, calls: List[Dict]):
        """
        Adds multiple call records to the call logs.

        Parameters:
        - calls (List[Dict]):
            A list of call records, each represented as a dictionary with keys:
            'call_id', 'call_time', 'dispatch_time', 'arrival_time', 'resolution_time', 'success'.

        Raises:
        - ValueError:
            If any of the call records contain invalid timestamp orders.
        """
        for call in calls:
            self.add_call_log(
                call_id=call['call_id'],
                call_time=call['call_time'],
                dispatch_time=call['dispatch_time'],
                arrival_time=call['arrival_time'],
                resolution_time=call['resolution_time'],
                success=call['success']
            )

# Example usage of the EmergencyServicePerformance class:

if __name__ == "__main__":
    # Initialize the EmergencyServicePerformance instance
    esp = EmergencyServicePerformance()

    # Example call logs
    calls = [
        {
            'call_id': 1,
            'call_time': datetime(2023, 10, 1, 14, 30),
            'dispatch_time': datetime(2023, 10, 1, 14, 31),
            'arrival_time': datetime(2023, 10, 1, 14, 35),
            'resolution_time': datetime(2023, 10, 1, 14, 50),
            'success': True
        },
        {
            'call_id': 2,
            'call_time': datetime(2023, 10, 2, 9, 15),
            'dispatch_time': datetime(2023, 10, 2, 9, 16),
            'arrival_time': datetime(2023, 10, 2, 9, 20),
            'resolution_time': datetime(2023, 10, 2, 9, 45),
            'success': False
        },
        {
            'call_id': 3,
            'call_time': datetime(2023, 10, 3, 20, 5),
            'dispatch_time': datetime(2023, 10, 3, 20, 6),
            'arrival_time': datetime(2023, 10, 3, 20, 10),
            'resolution_time': datetime(2023, 10, 3, 20, 30),
            'success': True
        }
    ]

    # Adding multiple call logs
    esp.add_multiple_call_logs(calls)

    # Calculating average response time
    try:
        avg_response = esp.average_response_time()
        print(f"Average Response Time: {avg_response}")
    except ValueError as e:
        print(f"Error: {e}")

    # Calculating success rate
    try:
        success_percentage = esp.success_rate()
        print(f"Success Rate: {success_percentage}%")
    except ValueError as e:
        print(f"Error: {e}")

    # Calculating average resolution time
    try:
        avg_resolution = esp.average_resolution_time()
        print(f"Average Resolution Time: {avg_resolution}")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieving calls within a specific timeframe
    start = datetime(2024, 10, 1, 0, 0)
    end = datetime(2024, 10, 2, 23, 59)
    calls_in_range = esp.calls_in_timeframe(start, end)
    print(f"Number of calls between {start} and {end}: {len(calls_in_range)}")
