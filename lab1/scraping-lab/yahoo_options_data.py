import json
import sys
import re
import urllib 
from bs4 import BeautifulSoup
import string

def contractAsJson(filename):
  jsonQuoteData = "[]"
  soup = BeautifulSoup(open(filename),"html.parser")
  ### scrape the stock_price
  span_list = soup.find_all('span')
  for elem in span_list:
    if not ('class' in elem.attrs): continue
    if elem['class'] == ['time_rtq_ticker']:
      stock_price = elem.children.next().string
      print stock_price
      break

  ### scrape the data urls
  ## data host
  div_list = soup.find_all('div')
  for elem in div_list:
    if ('data-host' in elem.attrs):
      url_host = str(elem['data-host'])
      print url_host
      break
  ## urls
  tr_list = soup.find_all('tr')
  for elem in tr_list:
    if not ('valign' in elem.attrs): continue
    data_start = elem
    break
  a_list = data_start.find_all('a')
  url_list = list()
  for elem in a_list:
    if not ('href' in elem.attrs): continue
    url_string = str(elem['href'])
    if -1 == (string.find(url_string,'m=')): continue
    url_list.append(url_string)
    print url_string
  
  ###scrape the contracts 
  ##find the starting point
  for elem in tr_list:
    if not ('table' == elem.parent.name): continue
    if ('th' == elem.children.next().name):
      item_start = elem
      break
  ##scrape the data
  data_list = list()
  for elem in item_start.next_siblings:
    item_list = elem.find_all('td')
    data = list()
    for item in item_list:
      tmp = item
      while not (None == getattr(tmp, 'name', None)):
        tmp = tmp.contents[-1]
      data.append(tmp.replace(',',''))
    tmp_groups = re.match(r"([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)",data[1],re.I).groups()
    pos = data[1].rfind(tmp_groups[2])
    data_dict = dict({'Ask':data[5],
            'Bid':data[4],
            'Change':data[3],
            'Date':data[1][pos-6:pos],
            'Last':data[2],
            'Open':data[7],
            'Strike':data[0],
            'Symbol':data[1][:pos-6],
            'Type':tmp_groups[2],
            'Vol':data[6]})
    for key in data_dict:
      print key,
      print ':',
      print data_dict[key]
    data_list.append(data_dict)
    print '\n'
  quit()
  return jsonQuoteData


