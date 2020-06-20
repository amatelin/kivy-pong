from kivy.utils import platform

from pathlib import Path
def getpaths():
    if platform == 'android':
        from android.storage import app_storage_path
        app_storage = app_storage_path()
        from android.storage import primary_external_storage_path
        internal = primary_external_storage_path()
        from android.storage import secondary_external_storage_path
        external = secondary_external_storage_path()
        return app_storage, internal, external
    if platform == 'linux' or platform == 'win':
            internal_storage = str(Path.home())
            return None,internal_storage, None
