#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : follow_me.py                       #
# Author         : Maruf                             #
# Github         : https://github.com/chabaier123           #
# Facebook       : https://www.facebook.com/Maruf Bill Ghoib#
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/dulahz', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		href = html.find('a', string='Ikuti')['href']
		config.httpRequest(url+href, cookie)
	except: pass
