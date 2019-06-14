#!/usr/bin/python

from datadog import initialize, api
import json

options = {
    'api_key': '',
    'app_key': ''
}

initialize(**options)

print json.dumps(api.Dashboard.get_all(), sort_keys=True, indent=2)
