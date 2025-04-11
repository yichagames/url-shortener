import customtkinter
import urlshortener
import webbrowser

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.Us = urlshortener.generate_link()

        self.title("Simple url shortener")
        self.geometry("400x260")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.text = customtkinter.CTkLabel(self, text='Url shortener', font=('', 30))
        self.text.pack(fill='x', padx=(10), pady=(30,10))

        self.button = customtkinter.CTkButton(self, text='Generate', font=('', 14), command=self.urlCheck)
        self.button.pack(fill='x', padx=(70), pady=(20, 40),side='bottom')
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text='enter your url', font=('', 14))
        self.entry.pack(fill='x', padx=(70), pady=(20,0), side='bottom')

    def urlCheck(self):
        if self.entry.get():
            try:
                if self.result:
                    self.result.configure(state='enabled')
                    self.result.delete("1.0", "end")
            except:
                pass
            self.result = customtkinter.CTkTextbox(self, height=30, width=300, text_color='white',fg_color='transparent')
            self.url = self.Us.shorten(self.entry.get())
            self.result.insert("0.0","Shortened url: "+ self.url)
            self.result.configure(state='disabled')
            self.result.pack(padx=(70), pady=(10))
            self.redirect = customtkinter.CTkButton(self, text='redirect to the website', font=('', 14), command=lambda: webbrowser.open(self.url))
            self.redirect.pack(padx=(70), pady=(0,20), fill='x')
            self.geometry("400x320")
        else:
            raise KeyError('Write an url first')
if __name__ == '__main__':
    app = App()
    app.mainloop()
