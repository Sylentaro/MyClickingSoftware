from tkinter import *
from tkinter import ttk
import keyboard

geometryX = 900
geometryY = 500
listX = 120
listY = 0
PROGRAM_PAUSED = True
PROGRAM_FOCUS = True
CHILD_WINDOW_FOCUS = False
keys = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n',
        'm', ',', '.', '`', 'esc', 'enter', 'delete', 'ctrl', 'left', 'up', 'down',
        'right', 'space', 'backspace', 'tab', 'scroll lock', 'print screen',
        'insert', 'pause', 'caps lock', 'num lock', 'windows', 'alt', 'page down',
        'page up', 'play/pause media', 'F1', 'F2', 'F3', 'F4',
        'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', '*', '/', '+', '+', '-', '-',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'left windows',
        'right windows', 'left ctrl', 'right ctrl', 'left alt', 'alt gr')


# def releaseKeys(self,Keys=('1', '2', '3')):
#     for key in Keys:
#         keyboard.release(key)
#     print("released")
#     self.root.after(50, self.press)


# def pressKeys(Keys=('1', '2', '3')):
#     # keyboard.write('The quick brown fox jumps over the lazy dog.')
#     for key in Keys:
#         print(key)
#         keyboard.press(key)
#     print("pressed")


class Application:

    def __init__(self):
        self.root = Tk()
        self.root.grab_set()
        self.root.title('Button Clicker by Sylent')
        self.root.geometry("255x280+{}+{}".format(geometryX, geometryY))
        self.root.resizable(0, 0)

        self.btnAddKey = Button(self.root, text="Add key", width=7, command=self.clickAddKey)
        self.btnAddKey.place(height=50, x=listX - 5, y=listY + 165)
        self.btnDelKey = Button(self.root, text="Remove Key", width=9, command=self.clickDelKey)
        self.btnDelKey.place(height=50, x=listX + 55, y=listY + 165)
        self.btnStart = Button(self.root, text='Start!', width=10, command=self.clickStartKey)
        self.btnStart.place(height=90, x=listX - 80, y=listY)
        self.btnStop = Button(self.root, text='Stop!', width=10, command=self.clickStopKey, state="disabled")
        self.btnStop.place(height=70, x=listX - 80, y=listY + 90)
        self.isBtnSpaceChecked = IntVar()
        self.entryInterval = Entry(self.root, bd=3)

        self.checkBtnSpace = Checkbutton(self.root, text="Space", variable=self.isBtnSpaceChecked)
        self.checkBtnSpace.place(x=listX, y=listY+225)

        self.keyList = Listbox(master=self.root)
        self.keyList.place(x=listX)

        self.root.bind("<Key>", self.eventStopPlayKey)
        # self.root.bind("<Map>", self._map)
        # self.root.bind("<Unmap>", self._unmap)
        self.root.bind("<FocusIn>", self._focus)
        self.root.bind("<FocusOut>", self._unfocus)
        # self.root.wm_attributes('-toolwindow', True)
        # self.root.wm_attributes('-disabled', True)
        print(self.root.wm_state())
        print(self.root.wm_protocol())

    def pressKeys(self, Keys=('1', '2', '3')):
        # keyboard.write('The quick brown fox jumps over the lazy dog.')
        for key in Keys:
            print(key)
            keyboard.press(key)
        print("pressed")

    def releaseKeys(self, Keys=('1', '2', '3')):
        for key in Keys:
            keyboard.release(key)
        print("released")
        self.root.after(50, self.press)

    # def press_and_release(self, Keys=('a', 'b', 'c')):
    #     for key in Keys:
    #         keyboard.press_and_release(key)
    #     print("pressed and released list sequence")
    #     self.root.after(50, self.press)

    def _focus(self, event):
        global PROGRAM_FOCUS
        PROGRAM_FOCUS = True
        print(PROGRAM_FOCUS)

    def _unfocus(self, event):
        global PROGRAM_FOCUS
        PROGRAM_FOCUS = False
        print(PROGRAM_FOCUS)
        self.startpauseCheck()

    def startpauseCheck(self):
        if not PROGRAM_FOCUS and not CHILD_WINDOW_FOCUS:
            if PROGRAM_PAUSED:
                if keyboard.is_pressed('Page up'):
                    self.clickStartKey()
            elif not PROGRAM_PAUSED:
                if keyboard.is_pressed('Page down'):
                    self.clickStopKey()
            self.root.after(10, self.startpauseCheck)

    def clickStartKey(self):
        global PROGRAM_PAUSED
        PROGRAM_PAUSED = False
        self.btnStop['state'] = 'normal'
        self.btnStart['state'] = 'disabled'
        self.checkBtnSpace['state'] = 'disabled'
        if self.isBtnSpaceChecked.get() == 1:
            keyboard.press('space')
        self.root.after(1000, self.press)

    def eventStopPlayKey(self, event):
        if event.keycode == 33 and PROGRAM_PAUSED:
            self.clickStartKey()
        elif event.keycode == 34 and not PROGRAM_PAUSED:
            self.clickStopKey()

    def clickStopKey(self):
        global PROGRAM_PAUSED
        PROGRAM_PAUSED = True
        self.btnStart['state'] = 'normal'
        self.btnStop['state'] = 'disabled'
        self.checkBtnSpace['state'] = 'normal'
        if self.isBtnSpaceChecked.get() == 1:
            keyboard.release('space')

    def clickAddKey(self):
        global CHILD_WINDOW_FOCUS
        CHILD_WINDOW_FOCUS = True
        self.root.wm_attributes('-disabled', True)

        def clickInnerAddKey():
            if keys_cb.get() != '':
                self.keyList.insert(END, keys_cb.get())
                windowDispose()

        def windowDispose():
            global CHILD_WINDOW_FOCUS
            CHILD_WINDOW_FOCUS = False
            self.root.wm_attributes('-disabled', False)
            windowKeyAdd.destroy()

        # inner window
        windowKeyAdd = Toplevel()
        windowKeyAdd.grab_set()
        windowKeyAdd.title('Add key')
        windowKeyAdd.geometry("250x200+{}+{}".format(geometryX, geometryY))
        windowKeyAdd.resizable(0, 0)
        windowKeyAdd.wm_attributes('-toolwindow', True)
        windowKeyAdd.focus_set()
        windowKeyAdd.protocol('WM_DELETE_WINDOW', windowDispose)

        labelAddKeyInner = ttk.Label(windowKeyAdd, text="Select Key")
        labelAddKeyInner.pack(fill='x', padx=5, pady=5)

        # combobox
        selected_key = StringVar()
        keys_cb = ttk.Combobox(windowKeyAdd, textvariable=selected_key)
        keys_cb['values'] = keys
        keys_cb['state'] = 'normal'
        keys_cb.pack(fill='x', padx=5, pady=5)
        # inner buttons
        btnAddKeyInner = Button(windowKeyAdd, text='Add !', command=clickInnerAddKey)
        btnAddKeyInner.pack(fill='x', padx=5, pady=5)

    def clickDelKey(self):
        if self.keyList.curselection() != ():
            self.keyList.delete(self.keyList.curselection())
        else:
            self.keyList.delete(END)

    def press(self):
        if not PROGRAM_PAUSED:
            # keyboard.write('The quick brown fox jumps over the lazy dog.')
            self.root.after(1, self.pressKeys(self.keyList.get(0, END)))
            self.root.after(1, self.releaseKeys(self.keyList.get(0, END)))
            # self.root.after(50, self.press)
        else:
            pass

    def start(self):
        self.root.mainloop()
