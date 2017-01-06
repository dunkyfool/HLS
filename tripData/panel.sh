#!/bin/bash

url="http://www.tripadvisor.com/Attraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html"

if [ "$1" = "run" ];then
  scrapy crawl tripData_CentralPark
elif [ "$1" = "shell" ];then
  scrapy shell $url
else
  echo "(run|shell)"
fi
