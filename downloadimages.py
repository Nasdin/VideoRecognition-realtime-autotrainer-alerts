#Author: Nasrudin Bin Salim
#Copyright (C) Nasrudin B Salim 2018


#What this does:
#Gets input from hardcoded parameters
#google searches that input and downloads those images into a folder(based on input)


import time  # Importing the time library to check the time of code execution
import os
from data_munging.imagewebscraper import download_page, _images_get_all_items, clean_search, remove_duplicates, getfiletype

# TODO: Take search key words from labels.txt

#parameters
search_keyword = ['Burning Cars', 'flaming car', 'burning car','flaming cars','exploding car','exploding cars'] #a list of strings to search for
save_directory = "data/downloads/"

train_ratio = 0.7 #The ratio of train to the entire data set. Test_ratio will be taken as 1- train_ratio

def download_images(search_keyword=search_keyword,save_directory=save_directory,verification=verification,train_ratio=train_ratio):

    t0 = time.time()  # start the timer
    items = {} #create the items dictionary here

    for index,i in enumerate(search_keyword):
        items.update({i:[]}) #create a list for this search keyword
        iteration = "Item no.: " + str(index + 1) + " -->" + " Item name = " + str(i)
        print(iteration)

        # make a search keyword  directory
        try:
            os.makedirs(save_directory+i)
        except OSError as e:
            if e.errno != 17:
                raise
                # time.sleep might help here
            pass

        #Search for the search_keyword

        search = clean_search(i)
        url = 'https://www.google.com/search?q=' + search + \
              '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        raw_html = download_page(url)
        items[i] = _images_get_all_items(raw_html)

        # print ("Image Links = "+str(items))
        before = len(items[i])
        print("Total Image Links = " + str(before))
        print("\n","Removing Duplicates")

        #remove possible duplicates from searches
        items = remove_duplicates(items)
        after = len(items[i])
        print("Total Image Links = " + str(after))
        print("Duplicates removed = " + str(before-after))


        #Write all the saved linked into a text file
        with open(save_directory+'output.txt', 'a') as info:
            info.write(str(i) + ':' + str(
                items) + "\n\n\n")
            info.close()  # Close the file

        t1 = time.time()  # stop the timer
        total_time = t1 - t0  # Calculating the total time required to crawl
        print("Total time taken: " + str(total_time) + " Seconds")
        print("Starting Download...")

        ## To save imges to the save_directory
        # IN this saving process we are just skip the URL if there is any error

        #links of images are saved in items variable, hence we will loop through items and download that into a folder


        errorCount = 0
        for index,image_link in enumerate(items[i]):
            from urllib import request
            from urllib.error import URLError, HTTPError

            try:
                filetype = getfiletype(image_link)
                if filetype == "?":
                    print ("can't find filetype for file", image_link,"defaulting to .jpg")
                    filetype = '.jpg'
                req = request.Request(image_link, headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                output_filename = (save_directory+(str(i)) + "/" + str(index + 1) + filetype)
                print (output_filename)

                #save the file
                with request.urlopen(req, None, 15) as response:
                    with open(output_filename,'wb') as output_file:
                        output_file.write(response.read())
                        output_file.close()
                    response.close()


                print("completed ====> " + str(index + 1))


            except IOError:  # If there is any IOError

                errorCount += 1
                print("IOError on image " + str(index + 1))

            except HTTPError as e:  # If there is any HTTPError

                errorCount += 1
                print("HTTPError" + str(index))
            except URLError as e:

                errorCount += 1
                print("URLError " + str(index))


    print("\n")
    print("Everything downloaded!")
    print("\n" + str(errorCount) + " ----> total Errors")
if __name__ == "__main__":
    download_images()


