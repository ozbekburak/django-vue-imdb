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

imdbpyLibrary = IMDb()

# Create your views here.
@api_view(["POST"])
def MovieDetail(moviedata):
   
    try:       
       
        movieUnicode = moviedata.body.decode('utf-8')
        movieData = json.loads(movieUnicode) 

        movieSearchResult = imdbpyLibrary.search_movie(movieData['title'])
        
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
        soundtrack = getSoundtrack(movieID)
        location = getLocation((movieID))        

        listAllDetail = [movieID, title , year, genre, rating, soundtrack, location]
        getMovieDetailSerialized = json.dumps(listAllDetail)

        return JsonResponse(getMovieDetailSerialized, safe=False)
    except ValueError as e:
        return Response(e.args[0].status.HTTP_400_BAD_REQUEST)


# detail methods
def getID(getMovie):
  return getMovie[0].movieID

def getYear(getMovie):
  return getMovie[0]['year']

def getGenre(movieContainers):
  genre = movieContainers[0].p.find('span', class_='genre').text
  return ''.join(genre.split())  # convert list to string

def getRating(movieContainers):
  rating = movieContainers[0].find('strong', class_='').text
  return rating

def getSoundtrack(movieID):
  ms = imdbpyLibrary.get_movie(movieID)
  imdbpyLibrary.update(ms, 'soundtrack')
  return (ms['soundtrack'])

def getLocation(movieID):
  locations = imdbpyLibrary.get_movie_locations(movieID)
  return locations['data']['locations']