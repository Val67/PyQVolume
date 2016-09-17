PyQVolume
=========

A simple tray volume icon. Made in Python with PySide/Qt.
Requires python-alsaaudio and pyxdg.

What works:

* Setting the volume
* Muting the volume

What doesn't work:

* Changing the icon according to the volume level. Possible pyxdg bug? xdg.Config.icon_theme is always set to "hicolor".
