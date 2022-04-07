

class YTVideoDownloader:
    def __init__(self,link,quality):
        self.link=link
        self.quality=quality
        self.result='Success'
        
    def downVideo(self):
        import subprocess,sys
        try:
            from pytube import YouTube
            
        except Exception:
            subprocess.check_call([sys.executable,'-m','pip','install','pytube'])
            from pytube import YouTube
            
        try:
            self.YTObj=YouTube(self.link)
            self.videoTitle=self.YTObj.title.split('|')

        except Exception:
            self.result='Fail-1'
            
        else:
            try:
                self.fileName=self.videoTitle[0]+self.quality+'.mp4'
                self.userReqFile=self.YTObj.streams.filter(res=self.quality,progressive=True)
                self.userReqFileItag=list(self.userReqFile.itag_index)[0]
                self.fileDownload=self.YTObj.streams.get_by_itag(self.userReqFileItag)
            except Exception:
                self.result='Fail-2'
            else:
                self.fileDownload.download(r'D:\YtDownloader',filename=self.fileName)


        
        
        
        
        
# yt1=YTVideoDownloader('https://youtu.be/V-LahAhQzHA','360p')   
# yt1.downVideo()  
        
        
        
            
            
            
        

    
    
    
    
    