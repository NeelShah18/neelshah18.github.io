import urllib
import simplejson
import pycountry
import os
import json

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(code, from_sensor=False):
	mapping = {country.name: country.alpha_3 for country in pycountry.countries}
	reversed_mapping = dict(zip(mapping.values(), mapping.keys()))
	query = reversed_mapping.get(code)

	query = query.encode('utf-8')
	params = {
		'address': query,
		'sensor': "true" if from_sensor else "false"
	}
	url = googleGeocodeUrl + urllib.parse.urlencode(params)
	json_response = urllib.request.urlopen(url)
	response = simplejson.loads(json_response.read())
	if response['results']:
		location = response['results'][0]['geometry']['location']
		latitude, longitude = location['lat'], location['lng']
		print(query, latitude, longitude)
	else:
		latitude, longitude = None, None
		print (query, "<no results>")
	return latitude, longitude

def main():
    return None

if __name__=="__main__":
    main()
