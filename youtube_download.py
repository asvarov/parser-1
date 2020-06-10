from pytube import YouTube

video = 'https://www.youtube.com/watch?v=sXQxhojSdZM'
playlist = 'https://www.youtube.com/watch?v=cdTe3ec2MdM&list=PLve9Z4J4Fbojj-Oy2ll1x-GNynMRx_56I'

ytfd = YouTube(video)
print(ytfd.title)

