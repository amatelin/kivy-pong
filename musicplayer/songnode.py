class songnode:
    def __init__(self):
        from jnius import autoclass
        MediaPlayer = autoclass('android.media.MediaPlayer')
        self.mplayer = MediaPlayer()
        self.secs = 0
        self.actualsong = ''
        self.length = 0
        self.isplaying = False
        self.pos=0

    def __del__(self):
        self.stop()
        self.mplayer.release()

    def load(self, filename):
        if self.isplaying:
            self.unload()
        try:
            self.actualsong = filename
            self.secs = 0
            self.mplayer.setDataSource(filename)
            self.mplayer.prepare()
            self.length = self.mplayer.getDuration() / 1000
            return True
        except:
            return False

    def unload(self):
        self.mplayer.reset()
        self.pos=0

    def play(self):
        self.mplayer.start()
        self.isplaying = True

    def stop(self):
        self.mplayer.stop()
        self.secs = 0
        self.isplaying = False

    def seek(self):
        self.mplayer.seekTo(self.pos)
        self.mplayer.play()

    def pause(self):
        self.mplayer.pause()
        self.pos=self.mplayer.getCurrentPosition()
        self.isplaying=False
        print(self.pos)