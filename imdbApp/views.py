from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import re
from bs4 import BeautifulSoup
import requests
from imdb import IMDb
from urllib.parse import quote

imdbpy_library = IMDb()

# Create your views here.
@api_view(["POST"])
def MovieTitle(moviedata):
   
    try:       
       
        movieUnicode = moviedata.body.decode('utf-8')
        movieData = json.loads(movieUnicode) 

        movieSearchResult = imdbpy_library.search_movie(movieData['title'])
        
         # batman begins -> batman+begins
        filterMovieName = quote(movieSearchResult[0]['title'].replace(" ", "+"))
        url = 'https://www.imdb.com/search/title?title={}&title_type=feature&sort=year,asc'.format(
          filterMovieName)

        # get movie link
        response = requests.get(url)


        try:
           html_soup = BeautifulSoup(response.text, 'html.parser')
        except ConnectionError as e:
           print(e)

         # (find_all) method extracts all the div containers that have assigned class
        movie_containers = html_soup.find_all(
            'div', class_='lister-item mode-advanced')








        movieID = getID(movieSearchResult)
        title = movieSearchResult[0]['title']
        year = getYear(movieSearchResult)
        genre = getGenre(movie_containers)
        rating = getRating(movie_containers)
        

        listAllDetail = [movieID, title , year, genre, rating ]
        getMovieTitleSerialized = json.dumps(listAllDetail)
        print(getMovieTitleSerialized)
        return JsonResponse(getMovieTitleSerialized, safe=False)
    except ValueError as e:
        return Response(e.args[0].status.HTTP_400_BAD_REQUEST)

def getID(getMovie):
    return getMovie[0].movieID

def getYear(getMovie):
    return getMovie[0]['year']

def getGenre(movieContainers):
    genre = movieContainers[0].p.find('span', class_='genre').text
    return ''.join(genre.split()) # convert list to string

def getRating(movieContainers):
    rating = movieContainers[0].find('strong', class_='').text
    return rating

# def getSoundtrack():
#     # get soundtrack of movies as url
#     songUrl = 'https://www.imdb.com/title/tt{}/soundtrack'.format(getID())
#     responseSoundtrack = requests.get(songUrl)

#     try:
#         html_soundtrack_soup = BeautifulSoup(
#             responseSoundtrack.text, 'html.parser')
#     except ConnectionError as e:
#         print(e)

#     movie_song_containers = html_soundtrack_soup.find_all(
#         'div', class_='header')

#     # soundtrack soda {even} {odd} -> regex for this discrimination
#     regexSongsClass = re.compile("^soundTrack soda.*")

#     songs = movie_song_containers[0].find_all(
#         'div', class_=regexSongsClass)
#     songList = []
#     for i in range(0, len(songs)):
#         songList.append(songs[i].text)
#     if songList == []:
#         return "No soundtrack found"
#     return ''.join(songList)




