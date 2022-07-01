#This is a development build of a script with the aim to do the following 
# 1. Scrape RSS feeds or news websites for articles and #  print the folllowing to serial
#   - Headline 
#   - Source
#   - Date
#   - Summary  
# 2. Ideas to add include
#   - Auto refresh
#   - Prevent duplicates
#   - Multisource
#   - Other sources
#   - Interactive
# works with e.volpe teletype usb board

# Feedparser entries are  ['summary_detail', 'published_parsed', 'links', 'title', 'summary', 'guidislink', 'title_detail', 'link', 'published', 'id']

import feedparser
import serial

f = open ("news.txt", "w")

ser = serial.Serial('COM5', 38400, timeout=0,)  # open serial port


# NewsFeed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml") #uk news works
# NewsFeed = feedparser.parse("https://www.pipes.digital/feed/1NjYgr9z")#ap works with errors (errant html tag)
# NewsFeed = feedparser.parse("https://www.feedspot.com/infiniterss.php?_src=followbtn&followfeedid=5243733&q=site") #ap does not work


entry = NewsFeed.entries[1]
f.write ("\n") 
f.write("-------------------------------------------------------------------")
f.write ("\n") 
f.write(entry.title)
f.write ("\n") 
f.write(entry.published)
f.write ("\n")  
f.write(entry.summary)
f.write ("\n") 

entry = NewsFeed.entries[2]
f.write("-------------------------------------------------------------------")
f.write ("\n") 
f.write(entry.title)
f.write ("\n") 
f.write(entry.published)
f.write ("\n")  
f.write(entry.summary)
f.write ("\n") 


entry = NewsFeed.entries[3]
f.write("-------------------------------------------------------------------")
f.write ("\n") 
f.write(entry.title)
f.write ("\n") 
f.write(entry.published)
f.write ("\n")  
f.write(entry.summary)
f.write ("\n") 

entry = NewsFeed.entries[4]
f.write("-------------------------------------------------------------------")
f.write ("\n") 
f.write(entry.title)
f.write ("\n") 
f.write(entry.published)
f.write ("\n")  
f.write(entry.summary) 
f.write ("\n") 


entry = NewsFeed.entries[5]
f.write("-------------------------------------------------------------------")
f.write ("\n")
f.write(entry.title)
f.write ("\n") 
f.write(entry.published)
f.write ("\n")  
f.write(entry.summary)
f.write ("\n") 

f.close()

f = open("news.txt", "rb")
# ser.write(f.read()) #turn on to print to tty

# output_file = open(write_to_file_path, "ab");
 
 
ser.close()             # close port
