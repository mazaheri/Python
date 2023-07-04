# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:14:39 2023

@author: Pourya
"""

BASE_LINK = 'https://{}.craigslist.org/search/sss?s={}'
city = 'berlin'
result1 = BASE_LINK.format(city, 'll')
result2 = f'https://{city}.craigslist.org/search/sss?s='
print(result1)
print(result2)