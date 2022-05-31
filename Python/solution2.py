
import os
from mutagen.mp3 import MP3
os.chdir('D:\Music\Songs IV\low')
dir = os.listdir()

audios = [x for x in dir if x[-4:]=='.mp3']
for file in audios:
    f = MP3(file)
    bitrate = f.info.bitrate / 1000
    print(bitrate)
    # if bitrate <= 200:
    #     print(bitrate)
    #     os.rename(file, 'low\\'+file)
    #     print('Moved', file)
    # name = re.sub("[\/:,*<?>|\"n.]", '', audiofile.tag.title[:200]).replace('\n', '')
    # print(audiofile.tag.title, '->', name)
    # try:
    #     os.rename(file, name+'.mp3')
    # except FileExistsError:
    #     if not os.path.exists('dups\\'+name+'.mp3'):
    #         os.rename(file, 'dups\\'+name+'.mp3')