# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:58:22 2014

@author: jmalinchak
"""

import win32gui
import re

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name = None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def printresult(self):
        """put the window in the foreground"""
        print(win32gui.GetWindowText(self._handle))
    def get_menutext(self):
        return win32gui.GetWindowText(self._handle)
    def openifclosed(self):
        """put the window in the foreground"""
        print(win32gui.GetWindowText(self._handle))

class check:
    
    def __init__ (self):
        print("running checkifprogramisrunning...")
    def wildcard(wildcardstring):
        w = WindowMgr()
        w.find_window_wildcard(".*"+wildcardstring+".*")       
        if len(w.get_menutext()) > 0:
            return True
        