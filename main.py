#!/usr/bin/python
# vim: set fileencoding=utf-8

from wxpy import *

bot = Bot()

current_msg = False

source_group = ensure_one(bot.groups().search(''))
target_group = ensure_one(bot.groups().search(''))

@bot.register(source_group)
def forward_source_message(msg):
    current_msg = msg
    print(msg.member)
    msg.forward(target_group, prefix='buy buy buy: ')


@bot.register()
def print_others(msg):
    print(msg)

# 进入 Python 命令行、让程序保持运行
embed()

