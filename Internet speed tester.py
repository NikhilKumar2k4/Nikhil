from tkinter import *  # Importing the tkinter module for GUI
import speedtest  # Importing the speedtest module for internet speed testing

def speedcheck():
    # Function to check internet speed
    sp = speedtest.Speedtest()  # Creating a Speedtest object
    sp.get_servers()  # Fetching a list of available servers
    down = str(round(sp.download()/(10**6),3)) + " Mbps"  # Measuring download speed and converting to Mbps
    up = str(round(sp.upload()/(10**6),3)) + " Mbps"  # Measuring upload speed and converting to Mbps
    lab_down.config(text=down)  # Updating the download speed label
    lab_up.config(text=up)  # Updating the upload speed label

sp = Tk()  # Creating a Tkinter window
sp.title("Internet Speed Test")  # Setting window title
sp.geometry("500x700")  # Setting window dimensions
sp.config(bg="Blue")  # Setting window background color

# Creating labels to display text
lab = Label(sp,text="Internet speed Test", font=("Time New Roman",30,"bold"),bg="Blue",fg="White")
lab.place(x=60,y=40,height=50,width=380)  # Placing the label on the window

lab = Label(sp,text="Download Speed", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

# Creating label to display download speed
lab_down = Label(sp,text="00", font=("Time New Roman",30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text="Upload Speed", font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

# Creating label to display upload speed
lab_up = Label(sp,text="00", font=("Time New Roman",30,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)

# Creating a button to trigger the speed check function
button= Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()  # Starting the main event loop to display the GUI and listen for events
