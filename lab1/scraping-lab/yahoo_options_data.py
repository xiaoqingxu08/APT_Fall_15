import json
import sys
import re
import urllib 
from bs4 import BeautifulSoup
import string

def contractAsJson(filename):
  jsonQuoteData = "{\n"
  soup = BeautifulSoup(open(filename),"html.parser")
  ### scrape the stock_price
  span_list = soup.find_all('span')
  for elem in span_list:
    if not ('class' in elem.attrs): continue
    if elem['class'] == ['time_rtq_ticker']:
      stock_price = elem.children.next().string
      #print stock_price
      break
  jsonQuoteData += ('    \"currPrice\": %s,\n' %str(float(stock_price)))

  ### scrape the data urls
  ## data host
  div_list = soup.find_all('div')
  for elem in div_list:
    if ('data-host' in elem.attrs):
      url_host = str(elem['data-host'])
      #print url_host
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
    tmp_string = url_string.split('&')[0]+'&amp;'+url_string.split('&')[1]
    url_list.append(tmp_string)
    #print url_string
  jsonQuoteData += '    \"dateUrls\": [\n'
  for index in xrange(len(url_list)):
    if not (index == 0): jsonQuoteData += ',\n'
    jsonQuoteData += '        \"http://%s%s\"' %(url_host,url_list[index])
  jsonQuoteData += '\n    ],\n'

  ###scrape the contracts 
  ##find the starting point
  item_start_list = list()
  for elem in tr_list:
    if not ('table' == elem.parent.name): continue
    if ('th' == elem.children.next().name):
      item_start_list.append(elem)
  #end for elem

  ##scrape the data
  data_keys = ['\"Ask\"', '\"Bid\"', '\"Change\"', '\"Date\"', '\"Last\"', '\"Open\"', '\"Strike\"', '\"Symbol\"', '\"Type\"', '\"Vol\"'] 
  data_list = list()
  for item_start in item_start_list:
    for elem in item_start.next_siblings:
      #print elem
      item_list = elem.find_all('td')
      data = list()
      for item in item_list:
        tmp = item
        while not (None == getattr(tmp, 'name', None)):
          tmp = tmp.contents[-1]
        #data.append(tmp.replace(',',''))
        data.append(tmp)
      #end for item
      tmp_groups = re.match(r"([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)",data[1],re.I).groups()
      pos = data[1].rfind(tmp_groups[2])
      data_dict = [str(data[5]),str(data[4]),' '+str(data[3]),str(data[1][pos-6:pos]),str(data[2]),str(data[7]),str(data[0]),str(data[1][:pos-6]),str(tmp_groups[2]),str(data[6])]
      #data_dict = [(data[5]),(data[4]),(data[3]),(data[1][pos-6:pos]),(data[2]),(data[7]),(data[0]),(data[1][:pos-6]),(tmp_groups[2]),(data[6])]
      #for key in data_dict:
      #  print key,
      #print '\n'
      data_list.append(data_dict)
    #end for elem
  #end for item_start  
  ##sort data_list
  data_list.sort(key=lambda x: int(x[5].replace(',','')),reverse=True)
  jsonQuoteData += '    \"optionQuotes\": ['
  for index in xrange(len(data_list)):
    if not (index == 0): jsonQuoteData += ','
    jsonQuoteData += '\n        {\n'
    indx = 0
    for key in data_list[index]:
      if not (indx == 0): jsonQuoteData += ',\n'
      jsonQuoteData += '            %s: \"%s\"' %(data_keys[indx],key)
      indx += 1
    jsonQuoteData += '\n        }'
  jsonQuoteData += '\n    ]'
  ###end 
  jsonQuoteData += '\n}'
  #print jsonQuoteData
  return jsonQuoteData


