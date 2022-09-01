'''


A class that creates canvases that are able to mirror the contents of another canvas



Example From:

https://stackoverflow.com/questions/7214054/tkinter-making-a-second-canvas-display-the-contents-of-another
'''

import tkinter as tk

class mirrorCanvas(tk.Canvas):
    '''A class that duplicates all objects on one or more peer canvases'''
    def __init__(self, *args, **kwargs):
        self.peers = []
        tk.Canvas.__init__(self, *args, **kwargs)

    def add_peer(self, peer):
        if self.peers is None:
            self.peers = []
        self.peers.append(peer)

    def move(self, *args, **kwargs):
        tk.Canvas.move(self, *args, **kwargs)
        for peer in self.peers:
            peer.move(*args, **kwargs)

    def itemconfigure(self, *args, **kwargs):
        tk.Canvas.itemconfigure(self, *args, **kwargs)
        for peer in self.peers:
            peer.itemconfigure(*args, **kwargs)

    def delete(self, *args, **kwargs):
        tk.Canvas.delete(self, *args)
        for peer in self.peers:
            peer.delete(*args)

    def create_oval(self, *args, **kwargs):
        tk.Canvas.create_oval(self, *args, **kwargs)
        for peer in self.peers:
            peer.create_oval(*args, **kwargs)
