import json
import pandas
import requests

if __name__=="__main__":
    url='http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=9a17ccf8828a53e3a85ff5acf706842b&artist=Cher&album=Believe&format=json'
    url2='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=9a17ccf8828a53e3a85ff5acf706842b&format=json'
    data = requests.get(url2).text
    jData = json.loads(data)
     #   jData2 = json.loads(data)
    
    topArtists = jData['topartists']['artist'][0]
    print topArtists
    print("Hello")
    
    #print jData


