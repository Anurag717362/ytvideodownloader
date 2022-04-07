#!C:\Users\91971\AppData\Local\Programs\Python\Python310\python.exe
print('Content-Type:text/html')
print()
import cgitb,cgi
cgitb.enable()

data=cgi.FieldStorage()

videoLink=data.getvalue('link')
videoQuality=data.getvalue('quality')

from yt_video_download_code import YTVideoDownloader

yt1=YTVideoDownloader(videoLink,videoQuality)   
yt1.downVideo()


if yt1.result=='Success':
    print('<html>')
    print('<head>')
    print('<title>Downloaded</title>')
    print('</head>')
    print('<body>')
    print('<h3>Video Downloaded successfully.</h3>')
    print('</body>')
    print('</html>')

if yt1.result=='Fail-1':
    print('<html>')
    print('<head>')
    print('<title>Download failed</title>')
    print('</head>')
    print('<body>')
    print('<h3>Invalid link. Failed to download video.</h3>')
    print('</body>')
    print('</html>')

if yt1.result=='Fail-2':
    print('<html>')
    print('<head>')
    print('<title>Download failed</title>')
    print('</head>')
    print('<body>')
    print('<h3>It seems like quality choosen by you is not available for this video. Kindly go with other quality.</h3>')
    print('</body>')
    print('</html>')



