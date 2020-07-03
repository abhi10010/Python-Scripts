import pyshorteners
import validators

url = input('Enter URL to shorten: ')

if validators.url(url) == True:
    print("URL after shortening: ", pyshorteners.Shortener().tinyurl.short(url))
else:
    print("Entered URL is wrong")
