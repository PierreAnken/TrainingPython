import tkinter as tk
from tkinter import filedialog
import ffmpeg  # ffmpeg-python

LARGE_FONT = ("Verdana", 12)
ser = None
file = None


class FFMpegApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # for F in (StartPage):

        #     frame = F(container,self)

        #     self.frames[F] = frame

        #     frame.grid(row = 0, column = 0, sticky = "nsew")
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.from_file = None
        self.to_file = None
        self.mute_list = None
        label = tk.Label(self, text="ffmpeg Python3 Video Converter v1.0", font=LARGE_FONT)
        label.grid(row=0, column=0)

        # definition
        w = 10
        fps_list = []
        for i in range(6):
            fps_list.append(str(i * 10 + 4))
        codec_list = ["x264", "x265"]
        tk_var_codec = tk.StringVar(self)
        tk_var_codec.set(codec_list[0])
        mute_list = ["0", "1"]
        tk_var_mute = tk.StringVar(self)
        tk_var_mute.set(mute_list[0])
        self.tk_var_fps = tk.StringVar(self)
        self.tk_var_fps.set(fps_list[0])

        self.btn_browse = tk.Button(
            self, text="Browse to directory",
            command=lambda: self.load_from_button(),
            height=3,
            width=20
        )

        self.btn_start = tk.Button(
            self, text="Start it!",
            command=lambda: self.start_button(),
            height=3,
            width=20
        )

        self.btn_safe = tk.Button(
            self,
            text="Browse to directory",
            command=lambda: self.save_to_button(),
            height=3,
            width=20
        )

        label.fps = tk.Label(self, text="Frame per seconds")
        label.fps.grid(row=2, column=0)
        label.codec = tk.Label(self, text="Choose your codec")
        label.codec.grid(row=2, column=1)
        label.mute = tk.Label(self, text="Mute the video")
        label.mute.grid(row=4, column=1)

        self.drp_fps = tk.OptionMenu(self, self.tk_var_fps, *fps_list)
        self.drp_codec = tk.OptionMenu(self, tk_var_codec, *codec_list)
        self.drp_mute = tk.OptionMenu(self, tk_var_mute, *mute_list)

        # placement
        self.btn_browse.grid(row=1, column=0)
        self.btn_safe.grid(row=1, column=1)
        self.drp_fps.grid(row=3, column=0)
        self.drp_codec.grid(row=3, column=1)
        self.btn_start.grid(row=5, column=0)
        self.drp_mute.grid(row=5, column=1)

    def load_from_button(self):
        self.from_file = filedialog.askopenfilename()

    def save_to_button(self):
        self.to_file = filedialog.asksaveasfilename()

    def start_button(self):
        ffmpeg.input(self.from_file).filter(  # Video laden
            'fps',
            fps=self.tk_var_fps.get(),
            round='up'
        ).trim(  # Schneiden
            start=0,
            end=5
        ).output(  # Ergebniss schreiben
            self.to_file,
            an=type(self.mute_list)
        ).run(overwrite_output=True)