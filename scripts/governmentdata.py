from urllib2 import Request, urlopen
import time
import traceback
import itertools
import json
import random
import os
from collections import namedtuple
from pandas.io.json import json_normalize
import requests

# Create a mapping of legislator to government id
# thesea are on https://www.govtrack.us
candidates = {
    'Bernie': 400357,
    'Hillary': 300022,
    'Cruz': 412573,
    'Kasich':400590
 }

# The Title of the bill looks like: 'H.R. 1357 (104th): To provide certain employee'
# we want to strip out everything until the space after the colon (:)
def strip_unused(string):
    pos = string.find(':')
    return string[pos+2:]

# gets the bill data for all the legislators and saves it into a csv file
def get_bill_data():
    for gov_name, gov_id in candidates.items():
        url = 'https://www.govtrack.us/api/v2/bill?sponsor=%d' % gov_id

        d = json.loads(requests.get(url).text)

        data = d[u'objects']
        result = json_normalize(data)
        #result['title']

        result['clean_title'] = result.title.apply(strip_unused )

        #save as csv
        # print gov_name
        filename = "bills_" + gov_name + ".csv"
        result.to_csv(filename, encoding="utf-8")
        print "wrote " + filename


if __name__ == '__main__':
	try:

		get_bill_data()

	except:
	    traceback.print_exc()
