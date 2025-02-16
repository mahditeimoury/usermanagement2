from PresentationLayer.Frames.register import RegisterFrame
from PresentationLayer.window import Window
from PresentationLayer.Frames.login import LoginFrame
from PresentationLayer.Frames.home import HomeFrame
from PresentationLayer.Frames.user_management import UserManagementFrame

class MainView:
    def __init__(self):
        self.frame = {}
        self.window = Window("user Management Application", "500x300")

        self.add_frame("usermanagement", UserManagementFrame(self.window, self))
        self.add_frame("register", RegisterFrame(self.window, self))
        self.add_frame("Home", HomeFrame(self.window, self))
        self.add_frame("login", LoginFrame(self.window, self))


        self.window.mainloop()


    def add_frame(self, name, frame):
        self.frame[name] = frame
        self.frame[name].grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frame[frame_name]
        frame.tkraise()
        return frame