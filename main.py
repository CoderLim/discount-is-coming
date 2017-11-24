#!/usr/bin/python
# vim: set fileencoding=utf-8
import re
import time
import json
import urllib
import requests
from wxpy import *

bot = Bot()
pre_msg = None

pt_key = 'app_openAAFaFskoADCkcV5Fj9xb5BrEKok-3JQBQ9ZEiGnzuYzBwr3LtftuU_28nEs5WsrPzrsHoHto-pM'
rbuy_url = r'https?://union-click.jd.com/jdc\?d=\w+'
cookies = {'pt_key': pt_key, 'pt_pin':'15201590338_p'}
transform_url_tpl = 'https://api.m.jd.com/?functionId=switchPushUrl&client=JingFenApp&clientVersion=2.1.0&body=%s'

def get_group_by_name(name):
    global bot
    groups = bot.groups()
    target = groups.search(name)
    while not target:
        print('%s Not Found, Wait 10 Seconds' % name)
        time.sleep(10)
        target = groups.search(name)
    return target

def get_transformed_url(origin_url):
    global transform_url_tpl
    global cookies
    body = '{%22promotionUrl%22:%22' + urllib.parse.quote_plus(origin_url) + '%22}'
    url = transform_url_tpl % body
    res = requests.get(url, cookies=cookies)
    result = json.loads(res.content)
    print(result)
    if result['success']:
        return result['data']['pushUrl']
    return None

# print all groups
print(bot.groups())

source_group = [get_group_by_name('A京东内购'), get_group_by_name('京东内部优惠抢购群')]
target_group = get_group_by_name('网购内部优惠群')
target = bot.self

@bot.register(source_group)
def forward_source_message(msg):
    global pre_msg
    global rbuy_url
    msg_text = msg.text
    # original buy url 
    origin_url = re.search(rbuy_url, msg_text).group()
    if origin_url:
        new_url = get_transformed_url(origin_url)
        if new_url:
            print('origin_url' % origin_url)
            print('new_url=%s' % new_url)
            # replace original buy url with new buy url 
            msg.text = re.sub(rbuy_url, new_url, msg_text)
            # retweet this message
            msg.forward(target, prefix='buy buy buy:')
        else:
            print('Transform Failed!')
            pre_msg = None

        # if previous message is a PICTURE, then retweet
        # and make pre_msg=None to prevent retweeting again
        if pre_msg and pre_msg.type == PICTURE:
            msg.forward(target)
            pre_msg = None

    # if previous message exists and is a goods detail, then current message should be a PICTURE, retweet it
    if pre_msg and re.match(rbuy_url, pre_msg.text) and msg.type == PICTURE:
        msg.forward(target)
    pre_msg = msg


@bot.register()
def print_others(msg):
    current_msg = msg
    print(msg)

# go into python repl
embed()

