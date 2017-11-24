#!/usr/bin/python
# vim: set fileencoding=utf-8

import re
import time
import json
import urllib
import requests
from wxpy import *

pre_msg = None
rbuy_url = r'https?://union-click.jd.com/jdc\?d=\w+'
cookies = {'pt_key': 'app_openAAFaFskoADCkcV5Fj9xb5BrEKok-3JQBQ9ZEiGnzuYzBwr3LtftuU_28nEs5WsrPzrsHoHto-pM', 'pt_pin':'15201590338_p'}
transform_url_tpl = 'https://api.m.jd.com/?functionId=switchPushUrl&client=JingFenApp&clientVersion=2.1.0&body=%s'

def get_transformed_url(origin_url):
    global transform_url_tpl
    global cookies
    body = '{%22promotionUrl%22:%22' + urllib.parse.quote_plus(origin_url) + '%22}'
    url = transform_url_tpl % body
    print(url)
    res = requests.get(url, cookies=cookies, verify=False)
    result = json.loads(res.content)
    print(result)
    if result['success']:
        return result['data']['pushUrl']
    return None

print(get_transformed_url('https://union-click.jd.com/jdc?d=8VnPVT'))

