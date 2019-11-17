import os
import os.path as path
from ui import ui_config as UC


class AuthenticationPage():

    def authenticate(self):
        exe_filename = UC.AUTH_SCRIPT
        exe_folder = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', '..', '..', 'utilities'))
        exe_full_path = path.normpath(path.join(exe_folder, exe_filename))
        os.system(exe_full_path)
