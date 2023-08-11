from pytube import Youtube
from sys import argv

#argv is the argument given in the command line on terminal
link = argv[1]
yt = Youtube(link)

print("Title", yt.title)
print("View: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download('/Users/Nicholas/Downloads')

#research pytube dont want to know views maybe time or something like that and i need to put path to folder i want to download it in 
