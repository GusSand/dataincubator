from urllib2 import Request, urlopen
import time
import traceback
import itertools
import json
import random
import os
from collections import namedtuple
from pandas.io.json import json_normalize


# Create a mappint of legislator to government id
# thesea are on https://www.govtrack.us
candidates = {
    'Bernie': 400357

#
#     'Hillary': 300022,
#     'Cruz': 412573,
#     'Kasich':400590
 }

# to help with json conversion
# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

for name, gov_id in candidates.items():

    # First get all the data and store it in files
    raw = urlopen('https://www.govtrack.us/api/v2/bill?sponsor=%d' % gov_id)

    # filename = '%s.csv' % name
    # f = open(filename, 'w')
    # f.truncate()
    # print 'writing %s' % filename
    # data = response.read()
    # json.dump(data, f)
    # f.write('\n')
    # f.close()

    response = raw.read()
    data = json.loads(response)
    json_normalize(data['objects'])

    print data.head()


    # extract the title


    # create wordmap
