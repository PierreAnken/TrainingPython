from win32api import GetSystemMetrics


class ScreenResolution:
    def __init__(self):
        # Screen settings
        self.screen_resolution_width = GetSystemMetrics(0)
        self.screen_resolution_height = GetSystemMetrics(1)

