#Author: Nasrudin Bin Salim
#Copyright (C) Nasrudin B Salim 2018


#What this does:
#Gets input from hardcoded parameters
#google searches that input and downloads those images into a folder(based on input)


import time  # Importing the time library to check the time of code execution
import os
from imagewebscraper import download_page #the function to open the download page
from imagewebscraper import _images_get_all_items #function to get all links



#parameters
search_keyword = ['Burning Cars']
keywords = [' high resolution']
save_directory = "data/downloads/"


if __name__ == "__main__":

    t0 = time.time()  # start the timer


    i = 0
    while i < len(search_keyword):
        items = []
        iteration = "Item no.: " + str(i + 1) + " -->" + " Item name = " + str(search_keyword[i])
        print(iteration)
        print("Evaluating...")
        search_keywords = search_keyword[i]
        search = search_keywords.replace(' ', '%20')

        # make a search keyword  directory
        try:
            os.makedirs(search_keywords)
        except OSError as e:
            if e.errno != 17:
                raise
                # time.sleep might help here
            pass

        j = 0
        while j < len(keywords):
            pure_keyword = keywords[j].replace(' ', '%20')
            url = 'https://www.google.com/search?q=' + search + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html = (download_page(url))
            time.sleep(0.1)
            items = items + (_images_get_all_items(raw_html))
            j = j + 1
        # print ("Image Links = "+str(items))
        print("Total Image Links = " + str(len(items)))
        print("\n")

        # This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
        info = open(save_directory+'output.txt', 'a')  # Open the text file called database.txt
        info.write(str(i) + ': ' + str(search_keyword[i - 1]) + ": " + str(items) + "\n\n\n")  # Write the title of the page
        info.close()  # Close the file

        t1 = time.time()  # stop the timer
        total_time = t1 - t0  # Calculating the total time required to crawl, find and download all the links of 60,000 images
        print("Total time taken: " + str(total_time) + " Seconds")
        print("Starting Download...")

        ## To save imges to the save_directory
        # IN this saving process we are just skipping the URL if there is any error

        #links of images are saved in items variable, hence we will loop through items and download that into a folder
        #this part is bugged and hence will have to be rewritten for python3


        # k = 0
        # errorCount = 0
        # while (k < len(items)):
        #     from urllib import request
        #     from urllib.error import URLError, HTTPError
        #
        #     try:
        #         req = request.Request(items[k], headers={
        #             "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        #         response = request.urlopen(req, None, 15)
        #         output_filename = (save_directory+(str(search_keywords)) + "/" + str(k + 1) + ".jpg")
        #         print (output_filename)
        #         #output_file = open(save_directory+(str(search_keywords)) + "/" + str(k + 1) + ".jpg", 'wb')
        #
        #         data = response.read()
        #         output_file.write(data)
        #         response.close()
        #
        #         print("completed ====> " + str(k + 1))
        #
        #         k +=1
        #
        #     except IOError:  # If there is any IOError
        #
        #         errorCount += 1
        #         print("IOError on image " + str(k + 1))
        #         k +=1
        #
        #     except HTTPError as e:  # If there is any HTTPError
        #
        #         errorCount += 1
        #         print("HTTPError" + str(k))
        #         k = k + 1;
        #     except URLError as e:
        #
        #         errorCount += 1
        #         print("URLError " + str(k))
        #         k = k + 1;
        #
        # i = i + 1

    print("\n")
    print("Everything downloaded!")
    print("\n" + str(errorCount) + " ----> total Errors")

