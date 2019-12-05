import subprocess
import time
class YoutubeService:
    def __init__(self):
        self.time_format = "%H:%M:%S"

    def download_cut(self,url,start_time,stop_time):
        filename = "abc.mp4"
        # duration = (datetime.strptime(stop_time,self.time_format) - datetime.strptime(start_time,self.time_format)).total_seconds()
        duration = stop_time - start_time
        start_time = str(time.strftime('%H:%M:%S',time.gmtime(start_time)))
        print("start_time after convert ",start_time)
        command = "ffmpeg -ss " + start_time + " -i $(youtube-dl -g " + url + ") -t "+ str(duration) + " -c copy "+ filename
        p = subprocess.Popen(command,shell=True)
        p.wait()
        print(p.returncode)


# YoutubeService().download_cut("dfs",1.2,65)