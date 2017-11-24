import requests
import json
import urllib

cookies = {'pt_key':'app_openAAFaFskoADCkcV5Fj9xb5BrEKok-3JQBQ9ZEiGnzuYzBwr3LtftuU_28nEs5WsrPzrsHoHto-pM', 'pt_pin':'15201590338_p'}
transform_url = 'https://api.m.jd.com/?functionId=switchPushUrl&client=JingFenApp&clientVersion=2.1.0&body=%7B%22promotionUrl%22%3A%22https%3A%2F%2Funion-click.jd.com%2Fjdc%3Fd%3DtuyuI6%22%7D'

res = requests.get(transform_url, cookies=cookies)
obj = json.loads(res.content)
print(obj['data']['skuName'])

print(urllib.parse.quote_plus('{"promotionUrl":"https://union-click.jd.com/jdc?d=tuyuI6"}'))
