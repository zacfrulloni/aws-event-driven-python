import json
import csv
import io
import boto3
import json
import urllib3
import itertools
import logging
import os

def lambda_handler(event, context):
    try:
        dyndb.put_item(TableName='covidstatstable',
                Item={
                'date': {'S': '55'},
                'cases': {'N': 'one'},
                'deaths': {'N': 'two'},
                'recoveries': {'N': 'three'},
                })
    except:
        e = "You have tried to put invalid data into covidstatstable. Unittest has succeeded!"
        print(e)