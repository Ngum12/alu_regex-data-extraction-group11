#!/usr/bin/python3
import re

#  event dates and times
event_data = """
Event: Conference - Sep 15, 2023 - 10:00 AM,
Event: Workshop - Oct 20, 2023 - 02:30 PM,
Event: Seminar - Nov 5, 2023 - 09:15 AM,
Event: Concert - Dec 10, 2023 - 07:00 PM,
Event: Exhibition - Jan 15, 2024 - 11:30 AM,
Event: Webinar - Feb 25, 2024 - 03:45 PM,
Event: Festival - Mar 5, 2024 - 06:30 PM,
Event: Charity Gala - Apr 10, 2024 - 08:00 PM,
"""

# Regular expression pattern for event dates and times
pattern = r'Event: (.*) - (\w{3} \d{2}, \d{4}) - (\d{2}:\d{2} [APM]+)'

# Extract event dates and times
event_dates = re.findall(pattern, event_data)

# Print the extracted event dates and times
for match in event_dates:
    event_type = match[0]
    event_date = match[1]
    event_time = match[2]
    print(f"Event Type: {event_type}, Date: {event_date}, Time: {event_time}")
