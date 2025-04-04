import requests
import json

###	Goal:
###	  Let's use the Pokemon API "pokapi" to generate a list of all the Pokemon.
###	  There are a lot of Pokemon so that will require pagination.	

# EXAMPLE OF EXPECTED RESPONSE FROM API
# 	NOTE: 	Results section will differ depending on request.
# 			See https://pokeapi.co/docs/v2#resource-listspagination-section
# {
#   "count": 248,
#   "next": "https://pokeapi.co/api/v2/ability/?limit=20&offset=20",
#   "previous": null,
#   "results": [
#     {
#       "name": "bulbasaur",
#       "url": "https://pokeapi.co/api/v2/pokemon/1/"
#     }
#   ]
# }

# details of what we're going to send and where
url = r'https://pokeapi.co/api/v2/pokemon/'
params = {
	'page': 1,		# starting page
	'per_page':3,	# items per page; not supported by every API 
					# (pokeapi does NOT support this, just here as an example)
}

pokeList = []
requestCount = 1
while url is not None:
	
	print(f"Requesting page {requestCount}...")
	# make the request to the API
	response = requests.get(url, params=params)

	# built-in generic status code check
	response.raise_for_status()
	print(f"Page {requestCount} received.")

	# extract response as a json-like object
	page = response.json()

	# display the entire response as indented JSON
	#print(json.dumps(page, indent=4))

	# print this page of results as indented JSON
	#print(json.dumps(page["results"], indent=4) )

	# the results section is a list of dicts, with 1 dict per Pokemon
	for pokeData in page['results']:
		# add that Pokemon to our list
		pokeList.append( pokeData['name'] )
		#print(pokeData["name"])

	# prep our next request to target the next page of the pagination
	url = page.get('next')
	requestCount += 1

# Now we've got a list of all the Pokemon!
pageNum = requestCount-1
pokeNum = len(pokeList)
print(f"Received {pageNum} pages containing data for {pokeNum} Pokemon:")
input("Press Enter to display the full list.")
for pokemon in pokeList:
	print(pokemon)
