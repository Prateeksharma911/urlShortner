from django.test import TestCase

# Create your tests here.

import pyshorteners
shortener = pyshorteners.Shortener()
shortened_url = shortener.chilpit.short('http://www.google.com')
print(shortened_url)