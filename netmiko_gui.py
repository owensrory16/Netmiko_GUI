import tkinter
import customtkinter
from pytube import YouTube

 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        
        customtkinter.set_appearance_mode("Dark")
        
        self.geometry("600x500")
        self.title("Netmiko GUI")
        self.minsize(400, 300)
        

        self.header = customtkinter.CTkLabel(master=self, text="NetMiko GUI")
        self.header.pack(pady=12, padx=10)
        
        
        self.name_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Device Names (Seperate with ' ; ')", width=245)
        self.name_entry.pack(pady=12, padx=20, anchor=tkinter.N)
        
        self.device_options = customtkinter.CTkOptionMenu(master=self,
                                       values=["Choose A Device Type","cisco_ios", "arista_eos","juniper_junos","forti_os"])
        self.device_options.pack(pady=12, padx=20, anchor=tkinter.N)
    
        self.ip_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter IP Addresses (Seperate with ' ; ')", width=245)
        self.ip_entry.pack(pady=12, padx=20, anchor=tkinter.N)
        
        self.command_label = customtkinter.CTkLabel(master=self, text="Please Enter Commands Below, Seperate with Semicolon ' ; '")
        self.command_label.pack(pady=12, padx=20, anchor=tkinter.N)
        
        self.command_input = customtkinter.CTkTextbox(master=self, width=400, height=400, fg_color ="grey", text_color="white")
        self.command_input.pack(pady=12, padx=20, anchor=tkinter.N)
        

        
    def button_callback(self):
        print("button pressed")    
        
    
        
    

if __name__ == "__main__":
    app = App()
    app.mainloop()



#def saveInfo():
 #   IP = ipaddress_entry.get()
  #  messagebox = tkinter.messagebox.Message(IP)