# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:46:17 2020

@author: Hp
"""

from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid,auth_token)

my_msg= ''.join(['Hello Gaurav\n' for i in range(100)])

message = client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)



