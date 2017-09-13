# -*- coding: utf-8 -*- use python3
"""
Created on Sun Sep 10 21:37:22 2017

@author: Ting (tina) Sun
"""

import urllib
import json

#'validations': [{'name': {'length': {'min': 5},
#                           'required': True,
#                           'type': 'string'}},
#                 {'email': {'required': True}},
#                 {'age': {'required': False, 'type': 'number'}},
#                 {'newsletter': {'required': True, 'type': 'boolean'}}]}
                 
invalidCustomers={
    "invalid_customers":[]
} 

for i in range(1,5):
    g=urllib.request.urlopen('https://backend-challenge-winter-2017.herokuapp.com/customers.json?page={0}'.format(i))
    results=g.read().decode('utf-8')
    data = json.loads(results)

    for a in data['customers']:
        customer={'id':'','invalid_fields':[]}
        if a['name'] is None or len(a['name'])<5 or not isinstance(a['name'], str):
            if customer['id']!='':
                customer['invalid_fields'].append('name')
            else:
                customer['id']=a['id']
                customer['invalid_fields'].append('name')
            
        if a['email'] is None:
            if customer['id']!='':
                customer['invalid_fields'].append('email')
            else:
                customer['id']=a['id']
                customer['invalid_fields'].append('email')
        
        if a['age']!=None and not isinstance(a['age'], int):
            if customer['id']!='':
                customer['invalid_fields'].append('age')
            else:
                customer['id']=a['id']
                customer['invalid_fields'].append('age')
        
        if a['newsletter'] is None or not isinstance(a['newsletter'], bool):
            if customer['id']!='':
                customer['invalid_fields'].append('newsletter')
            else:
                customer['id']=a['id']
                customer['invalid_fields'].append('newsletter')
        if customer !={'id':'','invalid_fields':[]}:
            invalidCustomers['invalid_customers'].append(customer)
            
invalidCustomers=json.dumps(invalidCustomers,sort_keys=True,indent=2)
print(invalidCustomers)
       
        
        