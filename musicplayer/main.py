from kivymd.app import MDApp
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.recycleview import RecycleView
from kivymd.uix.button import MDRectangleFlatButton
import getpath
import getsongs
import threading
from songnode import songnode


sm = ScreenManager()
songpaths = {}
songs = []


node = songnode()


class actionbar():
    pass


class songlist(RecycleView):
    def __init__(self, **kwargs):
        super(songlist, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in songs]


class MyButton(MDRectangleFlatButton):

    def getitem(self):
        return self.parent.get_view_index_at(self.center)

    def on_release(self):
        song = songs[self.getitem()]
        path = songpaths[song]
        global node
        node.load(path)
        node.play()


class Index(MDScreen):
    def thread(self):

        threading.Thread(target=self.callback).start()

    def callback(self, *args):
        global songpaths
        app, internal, external = getpath.getpaths()

        songdict = getsongs.getsonglist(internal, external)
        songpaths = songdict
        global songs
        songs = [x for x in songdict.keys()]
        print('got songs')
        self.changewidget()

    def menu(self):
        pass

    def changewidget(self):
        s = songlist()
        self.ids.box.remove_widget(self.ids.load)
        self.ids.box.add_widget(s, 1)

    def rplay(self, *args):
        global node
        if not node.isplaying:
            self.ids.pp.icon = 'pause-circle'
            song = songs[0]
            path = songpaths[song]
            node.load(path)
            node.play()
        else:
            self.ids.pp.icon = 'play-circle'
            node.pause()

    def change(self):
        self.ids.pp.icon = 'pause-circle'

    def left(self):
        pass


class main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE], [
                                Permission.READ_EXTERNAL_STORAGE])
        self.front = Index()
        sm.add_widget(self.front)
        sm.current = 'index'
        self.front.thread()
        return sm

    def changeico(self):
        self.front.change()


main().run()
