from functools import reduce
import simplejson as json 
import os 
import operator
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(os.path.abspath(''), 'product_rules.json')) as product_rules_file:
    print(product_rules_file)
    product_rules = json.load(product_rules_file)

def get_from_dict(data_dict, key_list):
    print('key_list ->', key_list)
    return reduce(operator.getitem, key_list, data_dict)

def get_product_rules(setting):
    try:
        if type(setting) == list:
            return get_from_dict(product_rules, setting)
        return get_from_dict(product_rules, [setting])
    except KeyError:
        raise ImproperlyConfigured("No available rule for {}".format(setting))