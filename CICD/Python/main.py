import json

def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    
    # Opening JSON file
    f = open('Tweets.json')
 
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    value = data.get(key)

    value = max(tweets['away_team_events'], key=lambda ev: ev['id'])
    return value