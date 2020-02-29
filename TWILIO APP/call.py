# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:40:42 2020

@author: Hp
"""

from twilio.rest import Client

account_sid = 'AC6e78f251181c83393249f1c81f1e845c'
auth_token = '7af291156e9fa92d1bb442f8144acaab'
client = Client(account_sid, auth_token)

call = client.calls.create(
                     to='+917382345820',
                     from_='+12058324686',
                     url="http://demo.twilio.com/docs/voice.xml"
                 )

print(call.sid)