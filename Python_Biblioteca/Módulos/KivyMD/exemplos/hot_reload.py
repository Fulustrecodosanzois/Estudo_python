from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp


class HotReload(MDApp):
    KV_FILES = ['Python/tela.kv']
    DEBUG = True

    def build_app(self):
        return Builder.load_file('Python/tela.kv')


HotReload().run()