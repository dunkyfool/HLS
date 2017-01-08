#!/bin/bash

url="http://www.tripadvisor.com/Attraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html"

if [ "$1" = "run" ];then
  scrapy crawl tripData_CentralPark
elif [ "$1" = "shell" ];then
  scrapy shell $url
elif [ "$1" = "progress" ];then
  echo -e "Number of parsed review:\n>> $(cat items.json|wc -l)"
  echo -e "Current URL:\n>> $(cat currentURL)"
else
  echo "(run|shell|progress)"
fi
