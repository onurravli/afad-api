# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from bs4 import BeautifulSoup

response = requests.get('https://deprem.afad.gov.tr/last-earthquakes.html')
response.encoding = 'utf-8'
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser', from_encoding="utf-8")
table = soup.find_all('table')[0]
table_rows = table.find_all('tr')


class Earthquake:
    def __init__(self, tarih, enlem, boylam, derinlik, tip, buyukluk, yer, id) -> None:
        self.tarih = tarih
        self.enlem = enlem
        self.boylam = boylam
        self.derinlik = derinlik
        self.tip = tip
        self.buyukluk = buyukluk
        self.yer = yer
        self.id = id


earthquakes = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if row:
        earthquakes.append(Earthquake(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]).__dict__)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/depremler/')
def depremler():
    return earthquakes  

@app.route('/depremler/<string:yer>')
def depremler_yer(yer):
    return [i for i in earthquakes if yer in i['yer']]

@app.route('/')
def home():
    return {"error": "Herhangi bir endpointe istek atmadınız. Lütfen /depremler veya /depremler/<yer> endpointlerinden birine istek atınız."}

@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Sayfa bulunamadı."}, 404