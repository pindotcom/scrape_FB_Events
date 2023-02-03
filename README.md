# scrape_FB_Events
Scrape Facebook events from local html page


Extract past events data with beautifulsoup from a local HTML page.  This code currently retrieves all the past events <div> tags and pulls out the following fields:
1. event_name
2. event_month
3. event_date
4. event_time
5. event_venue

then export the file as an json or csv file.

Pre-reqs:
- Navigate to events page (i.e. https://www.facebook.com/pg/statefarmarena/events/) and change subdomain from "www" to "m" to get the low complexity mobile html page
- Paginate through desired events and save page as "Webpage, Complete"

Inputs to code:
- Update and reference the locally saved HTML name
- Verify the class values as needed.

Sample Output:
	
[{"event_name": "Falcons vs. Buccaneers", "event_month": "JAN", "event_date": "8", "event_time": "1 PM", "event_venue": "Mercedes-Benz Stadium"}, {"event_name": "Falcons vs. Cardinals", "event_month": "JAN", "event_date": "1", "event_time": "1 PM", "event_venue": "Mercedes-Benz Stadium"},...]
