import pyperclip
import re
from pytube import YouTube
from pytube.exceptions import RegexMatchError


def downloadVideoFromClipboard():
    # extract text from the clipboard
    clipboardText = pyperclip.paste()
    ytLinkRegex = re.compile(r'(https://www.youtube.com/\S+youtu.be)')
    listOfLinks = ytLinkRegex.findall(clipboardText)
    # extract urls from content
    for i in range(len(listOfLinks)):
        # print(listOfLinks[i])
        ytVideoLink = listOfLinks[i]
        # interpolate the yt object with string values
        try:
            desiredVideo = YouTube(ytVideoLink)
        except RegexMatchError:
            print('An RegexMatchError Exception Occured While Parsing The Clipboard Text')
            print(f'{ytVideoLink} appears to have formatting issues')
            if i <= len(listOfLinks):
                print('skipping this entry...')
                print('processing the remaining items found...')
            else:
                print(f'skipping link {ytVideoLink}')
        except Exception as e:
            print(f'An {e} Exception Occured While Parsing The Clipboard Text')
            print(f'{ytVideoLink} appears to have formatting issues')
        else:
            # # establish a stream selection by iTag
            # stream = sextonVideo.streams.get_by_itag(22)
            # # download the selection
            # stream.download('./')
            print(desiredVideo.streams.filter(res="720p")[0])


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
