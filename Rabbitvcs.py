import sublime
import sublime_plugin
import os
import sys
import subprocess
import locale

if os.name == 'nt':
    import _winreg


class NotFoundError(Exception):
    pass

class RabbitCommand():

    def get_path(self, paths):
        if paths:
            return paths[0]
        elif self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.error_message(__name__ + ': No place to open terminal to')
    
    def commit(self, paths):
        path = self.get_path(paths)
        if not path:
            return

        if os.path.isfile(path):
            path = os.path.dirname(path)
        
        subprocess.call("rabbitvcs commit " + path, shell=True) 
    
    def update(self, paths):
        path = self.get_path(paths)
        if not path:
            return


        if os.path.isfile(path):
            path = os.path.dirname(path)
        
        subprocess.call("rabbitvcs update " + path, shell=True)

    def browse(self, paths):
        path = self.get_path(paths)
        if not path:
            return

        if os.path.isfile(path):
            path = os.path.dirname(path)
        
        subprocess.call("rabbitvcs browser " + path, shell=True)

    def status(self, paths):
        path = self.get_path(paths)
        if not path:
            return

        if os.path.isfile(path):
            path = os.path.dirname(path)
        
        subprocess.call("rabbitvcs checkmods " + path, shell=True)

class RabbitCommitCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.commit(paths)

class RabbitUpdateCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.update(paths)

class RabbitBrowseCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.browse(paths)
        
class RabbitStatusCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.status(paths)        