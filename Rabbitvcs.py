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

    def svncommand(self, paths, command):
        path = self.get_path(paths)
        if not path:
            return

        subprocess.call("rabbitvcs " + command + " " + path, shell=True)


class RabbitCommitCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "commit")

class RabbitUpdateCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "update")

class RabbitBrowseCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "browser")

class RabbitLogCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "log")

class RabbitDiffCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "diff")

class RabbitDeleteCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "delete")

class RabbitAddCommand(sublime_plugin.WindowCommand, RabbitCommand):
    def run(self, paths=[], parameters=None):
        self.svncommand(paths, "add")
