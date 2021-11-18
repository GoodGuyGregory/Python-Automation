import pyperclip
import re
from pytube import YouTube


def downloadVideoFromClipboard():
    clipboardText = pyperclip.paste()
    ytLinkRegex = re.compile(r'(https://www.youtube.com/\S+youtu.be)')
    listOfLinks = ytLinkRegex.findall(clipboardText)

    for i in range(len(listOfLinks)):
        print(listOfLinks[i])


downloadVideoFromClipboard()

# sextonVideo = YouTube(
#     'https://www.youtube.com/watch?v=8YOfTje05Lk&feature=youtu.be')

# secondSextonVideo = YouTube(
#     'https://www.youtube.com/watch?v=1NvALzdU9PU&feature=youtu.be ')

# #  filter the streams and select the first option
# video = secondSextonVideo.streams.filter(res="720p")[0]

# video.download('./')

# # establish a stream selection by iTag
# stream = sextonVideo.streams.get_by_itag(22)
# # download the selection
# stream.download('./')
