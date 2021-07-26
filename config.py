#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM= "https://radioindia.net/radio/mirchi98/icecast.audio"
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = '1154348892 1594887298 1097301839'
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = '1423797'
    CHAT = "-1001349749502"
    LOG_GROUP= "-1001509162224"
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY= "Y"
    ARQ_API= "ZWWTBV-XHINQS-QWTBAJ-AAZRUG-ARQ"
    REPLY_MESSAGE= None
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    DURATION_LIMIT= 15
    DELAY = 10
    API_HASH = "25b825e1ab5ec075d8e07e6e598bd017"
    BOT_TOKEN = "1902307421:AAGad3r9Txl2MjPHiEewmsgksQJ6Ea6ar4s"
    SESSION = "AQCldtOmCqh_tx83FHQ91-FGZbb8Du059_bNF_Jk_trqZ-YplE2MjU8YKtw48qpkEwg_y0istZBt-OwydVnnESSsEb7dU4-3MHjA14QtqpwBS4WusKVNLIipetV1vghD6XvkUIRgEyIUpKfG5zGaK1HN6qXmxR87HJFXQd02gHYBP3bL_YugfFYa_K62Cm7OY6fQ6a8sIVzU0oGkzjQLXS69Y41r3ZHl9qilXQ-k9Tt3Ue8bgPRH1rseOV4oaHn5blgfSyOphTHhd5p3jkrwCC3By0mVOdNJfj6vIituXfJYtF56H187GreGX7ScawghCHMvsmc2xCpizvXSYrQ1sSnvXxAMggA"
    playlist=[]
    msg = {}

