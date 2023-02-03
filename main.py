import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# Read the local html file
with open("Mercedes-Benz Stadium - Events.html", "r") as file:
    contents = file.read()

# Parse the HTML contents
soup = BeautifulSoup(contents, 'html.parser')

# Find all div elements with class="_55ws _5cqg _2x2t _5cqi"
divs = soup.find_all('div', {'class': '_55ws _5cqg _2x2t _5cqi'})

events = []

# Loop through the div elements
for div in divs:
    event = {}
    
    # Try to find h3 or h1 with class="_592p _r-i"
    h3 = div.find('h3', {'class': '_592p _r-i'})
    h1 = div.find('h1', {'class': '_592p _r-i'})
    
    # Get the event name
    if h3:
        event_name = h3.text
    elif h1:
        event_name = h1.text
    else:
        event_name = ""
    
    # Try to find span with class = "_1e39"
    span = div.find('span', {'class': '_1e39'})
    if span:
        event_month = span.text
    else:
        event_month = ""
    
    # Try to find span with class = "_1e3a"
    span = div.find('span', {'class': '_1e3a'})
    if span:
        event_date = span.text
    else:
        event_date = ""
    
    # Try to find span with class = "_592p"
    span = div.find('span', {'class': '_592p'})
    if span:
        event_time = span.text
    else:
        event_time = ""
    
    # Try to find span with class = "_592p"
    span = div.find_all('span', {'class': '_592p'})
    if len(span) > 1:
        event_venue = span[1].text
    else:
        event_venue = ""
    
    # Add the event details to the list
    event['event_name'] = event_name
    event['event_month'] = event_month
    event['event_date'] = event_date
    event['event_time'] = event_time
    event['event_venue'] = event_venue
    
    events.append(event)

# Create a pandas dataframe
df = pd.DataFrame(events)
print(df)

df.to_csv('file1.csv')

# # Dump the event details into a data.json file
# with open("data.json", "w") as file:
#     json.dump(events, file)
