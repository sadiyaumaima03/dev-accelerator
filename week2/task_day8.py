import requests

#Rebuilding Day 7 GET request in python
url = "http://universities.hipolabs.com/search?country=United+States"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    #print just fields we need from the first 3 results
    for uni in data[:3]:
        print(f"University: {uni.get('name')} | Website: {uni.get('web_pages')}[0]")
else:
    print(f"Request failed with status code: {response.status_code}")