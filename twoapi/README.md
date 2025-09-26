Project Description
This project is a simpe Django app that connects two public APIs. If you type a location, for example a city, the app look up its coordinates (latitude and longtitude), and then gets the current weather for that location. 

APIs Used
**Nominatim (OpenStreetMap)** – used to search for a place and get lat/lon  
   https://nominatim.org/release-docs/latest/api/Search/  

**Open-Meteo** – used to get the current weather using the lat/lon  
   https://open-meteo.com/  


How to Run Locally
Since this is Django, you can create a virtual environmemt, install the needed packages like pip install django requests, start the project and app, which are already included in this repo, then run the server. After running, open http://127.0.0.1:8000/ in the browser.

How the data join works
Nominatim gives back the coordinates for a place, for example, cagayan de oro (lat:  8.4756417, Lon: 124.6421532), these coordinates are then used in Open-Mateo to get the weather. Example result could be like = 30C, feels like 33C. There is also a computed field for comfort = 33 - 30 = 3. This is basically subtracting what it feels like by the current temperature

Limitations
if you search too much, Nominatim or Open-Meteo might slow down or block due to rate limiting. 
The comfort value also is just simple subtraction and not scientific
The project also only works with exact names, no auto complete or matching. There is also no history or saving results. 
Nominatim gives very detailed names that are too long. The results also vary depending on the API updates and it works online only, so it work offline

AI USAGE NOTE
I used AI to:

show me how to connect two different APIs together in Django
example: 
      geo = requests.get("https://nominatim.openstreetmap.org/search",
      params={"q": q, "format": "json", "limit": 1}).json()

 show examples of APIs that could be combined, and from there I used Nominatim and Open-Mateo.

 Tell me what packages to install like 'requests' so I could explain APIs, for example it it explained that without the 'requests' library I can’t fetch data in Django

Give me a sample of how to write the HTML template that displays the results from the API call like showing the place, and temperature

example
<p><b>Temp:</b> {{ result.temp }} °C</p>
<p><b>Feels Like:</b> {{ result.feels }} °C</p>
<p><b>Comfort:</b> {{ result.comfort }}</p>




