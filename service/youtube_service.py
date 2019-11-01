import subprocess
from datetime import datetime
class youtube_service:
    def __init__(self):
        self.time_format = "%H:%M:%S"

    def download_cut(self,url,start_time,stop_time):
        filename = "abc.mp4"
        duration = (datetime.strptime(stop_time,self.time_format) - datetime.strptime(start_time,self.time_format)).total_seconds()
        command = "ffmpeg -ss " + start_time + " -i $(youtube-dl -g " + url + ") -t "+ str(duration) + " -c copy "+ filename
        subprocess.Popen(command,shell=True)

youtube_service().download_cut("dfs","01:30:30","01:31:30")