from pytube import YouTube

video = 'https://www.youtube.com/watch?v=sXQxhojSdZM'
playlist = 'https://www.youtube.com/watch?v=cdTe3ec2MdM&list=PLve9Z4J4Fbojj-Oy2ll1x-GNynMRx_56I'

ytfd = YouTube(video)
ytpd = YouTube(playlist)
stream_video = ytfd.streams.first()
# stream_video.download()
stream_audio = ytfd.streams.filter(only_audio=True).first()
stream_audio.download()
stream_playlist = ytpd.streams.all
stream_playlist.download
