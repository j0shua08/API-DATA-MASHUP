
# Create your views here.
import requests
from django.shortcuts import render
from requests.exceptions import RequestException


def search(request):
    q = request.GET.get("q", "")
    result = None
    error = None
    empty = False

    if q:
        try:
            geo_res = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params={"q": q, "format": "json", "limit": 1},
                headers={"User-Agent": "twoapi-student-demo/0.1"},
                timeout=5, 
            )
            if geo_res.status_code == 429:
                error = "Rate limited by Nominatim. Please try again later."
            else:
                geo_res.raise_for_status()
                geo = geo_res.json()

                if not geo:
                    empty = True  
                else:
                    lat = geo[0]["lat"]
                    lon = geo[0]["lon"]

                    wx_res = requests.get(
                        "https://api.open-meteo.com/v1/forecast",
                        params={
                            "latitude": lat,
                            "longitude": lon,
                            "current": "temperature_2m,apparent_temperature",
                            "timezone": "auto",
                        },
                        timeout=5,
                    )
                    if wx_res.status_code == 429:
                        error = "Rate limited by Open-Meteo. Please try again later."
                    else:
                        wx_res.raise_for_status()
                        weather = wx_res.json()

                        temp = weather["current"]["temperature_2m"]
                        feels = weather["current"]["apparent_temperature"]
                        comfort = round(feels - temp, 1)

                        result = {
                            "place": geo[0]["display_name"],
                            "lat": lat,
                            "lon": lon,
                            "temp": temp,
                            "feels": feels,
                            "comfort": comfort,
                        }
        except RequestException:
            error = "Network problem while contacting the API. Please check your internet and try again."
        except Exception as e:
            error = str(e)


    return render(request, "app/search.html", {"q": q, "result": result, "error": error, "empty": empty})
