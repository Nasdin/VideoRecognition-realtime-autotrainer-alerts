#Author: Nasrudin Bin Salim
#Copyright (C) Nasrudin B Salim 2018


#What this does:
#A module containing functions to assist in downloading images from google search

import time  # Importing the time library to check the time of code execution
import sys  # Importing the System Library


# Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3, 0)
    cur_version = sys.version_info
    if cur_version >= version:  # If the Current Version of Python is 3.0 or above
        import urllib.request  # urllib library for Extracting web pages
        try:
            headers = {}
            headers[
                'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))



# Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:  # If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"', start_line + 1)
        end_content = s.find(',"ow"', start_content + 1)
        content_raw = str(s[start_content + 6:end_content - 1])
        return content_raw, end_content


# Getting all links with the help of '_images_get_next_item'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)  # Append all the links in the list named 'Links'
            time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

#replace spaces in string with %20
def clean_search(word):
    ''' replaces spaces in string with %20'''
    return word.replace(" ","%20")

#remove duplicates from a dictionary across all keys and elements
def remove_duplicates(dictionary):
    output = {}
    seen = set()
    for keys in dictionary:
        output.update({keys:[]})
        for value in dictionary[keys]:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if value not in seen:
                output[keys].append(value) #add it to the list
                seen.add(value)
    return output

#get the filetype of of a url
def getfiletype(url):
    possibletypes = ['.jpg','.png','.gif','.jpeg','.mp4','.avi','.tif','.wmv','.flv']
    url = url.lower() #case insensitive
    for i in possibletypes:
        if i in url:
            return i
    return "?"




#TODO download an image with input of image url into a directory( another input) using requests




