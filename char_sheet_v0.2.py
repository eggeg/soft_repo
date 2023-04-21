from tkinter import *
import tkinter as tk


root = Tk()
root.title('Full Window Scrolling X Y Scrollbar Example')
root.geometry("800x400")

# Create A Main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

# Create Frame for X Scrollbar
sec = Frame(main_frame)
sec.pack(fill=X,side=BOTTOM)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

# Add A Scrollbars to Canvas
x_scrollbar = tk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
x_scrollbar.pack(side=BOTTOM,fill=X)
y_scrollbar = tk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)



# Configure the canvas
my_canvas.configure(xscrollcommand=x_scrollbar.set)
my_canvas.configure(yscrollcommand=y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

# Create Another Frame INSIDE the Canvas
m = Frame(my_canvas)

# Add that New Frame a Window In The Canvas
my_canvas.create_window((0,0),window= m, anchor="nw")

blockFrame = tk.Frame(master = m, width=500, height= 500, highlightbackground='maroon', highlightthickness=2)
items = tk.Frame(master=m, width=500, height=500, highlightbackground='blue', highlightthickness=2)
attr = tk.Frame(master=blockFrame, width=500, height=500,  highlightbackground='orange', highlightthickness=2)
stats = tk.Frame(master=blockFrame, width=500, height=500,  highlightbackground='red', highlightthickness=2)
notes = tk.Frame(master=m, width=500, height=500,  highlightbackground='yellow', highlightthickness=2)
skills = tk.Frame(master=m, width=500, height=500,  highlightbackground='purple', highlightthickness=2)
hpBlock = tk.Frame(master=blockFrame, width=500, height=500,  highlightbackground='green', highlightthickness=2)
speedBlock = tk.Frame(master=blockFrame, width=500, height=500,  highlightbackground='brown', highlightthickness=2)

logo = tk.Frame(master=m, width=500, height=500,  highlightbackground='lavender', highlightthickness=2)



blockFrame.grid(row = 2, column = 0)

items.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
notes.grid(row = 40, column = 0)
#attr.place(anchor= NE)
attr.grid(row = 0, column = 1)

stats.grid(row = 2, column = 0)

hpBlock.grid(row = 2, column = 1)
speedBlock.grid(row = 2, column = 2)




gear = Label(items, text='GEAR', bg='black', fg='white')

gear.grid(row=0, column = 0)

itemLabel = Label(items, text='ITEM')
itemLabel.grid(row = 1, column = 0)

weightLabel = Label(items, text='WT.')
weightLabel.grid(row=1, column=1) 
for x in range(2, 26):
   for y in range(2):
       if y == 1:
           text = Text(items, width=3, height=2)
           text.grid(row=x, column=y)
       else:
        text = Text(items, width=20, height=2)
        text.grid(row=x,column=y)
     


''' 
widgets are added here 
'''



#character attributes block


Label(attr, text='Character', fg="white", bg="black").grid(row=0)
Label(attr, text='Alignment', fg="white", bg="black").grid(row=0, column=2)
Label(attr, text='Player', fg="white", bg="black").grid(row=0, column=4)

Label(attr, text='Class', fg="white", bg="black").grid(row=1)
Label(attr, text='Level', fg="white", bg="black").grid(row=1, column=2)
Label(attr, text='Diety', fg="white", bg="black").grid(row=1, column=4)
Label(attr, text='Homeland', fg="white", bg="black").grid(row=1, column=6)

Label(attr, text='Race', fg="white", bg="black").grid(row=2)
Label(attr, text='Size', fg="white", bg="black").grid(row=2, column=2)
Label(attr, text='Gender', fg="white", bg="black").grid(row=2, column=4)
Label(attr, text='Age', fg="white", bg="black").grid(row=2, column=6)
Label(attr, text='Height', fg="white", bg="black").grid(row=2, column=8)
Label(attr, text='Weight', fg="white", bg="black").grid(row=2, column=10)
Label(attr, text='Hair', fg="white", bg="black").grid(row=2, column=12)
Label(attr, text='Eyes', fg="white", bg="black").grid(row=2, column=14)


#character stats block
Label(stats, text='Ability Name', fg="white", bg="black").grid(row=4)
Label(stats, text='Ability Score', fg="white", bg="black").grid(row=4, column=1)
Label(stats, text='Ability Modifier', fg="white", bg="black").grid(row=4, column=2)
Label(stats, text='Temporary Modifier', fg="white", bg="black").grid(row=4, column=3)


################################################         HPBLOCK    #############################################################
HP = Label(hpBlock, text='HP', fg="white", bg="black")
HP.grid(row=0, column = 0)

total= Label(hpBlock, text='total')
total.grid(row = 0, column = 1)

hpTotalEntry = Entry(hpBlock, width = 3)
hpTotalEntry.grid(row = 0, column = 2)

DR= Label(hpBlock, text='DR')
DR.grid(row = 0, column = 3)

drEntry = Entry(hpBlock, width = 2)
drEntry.grid(row = 0, column = 4)

wounds = Label(hpBlock, text='wounds/current HP')
wounds.grid(row=1, column = 2, sticky = W)

woundsEntry = tk.Text(hpBlock, width= 20, height=5)
woundsEntry.grid(row = 2, column = 2)

nonlethal = Label(hpBlock, text='nonlethal damage')
nonlethal.grid(row=3, column = 2, sticky = W)

nonlethalEntry = tk.Text(hpBlock, width= 20, height=3)
nonlethalEntry.grid(row=4, column = 2)








#speed block
speedLabel = Label(speedBlock, text='SPEED', fg="white", bg="black")
speedLabel.grid(row = 0, column = 0)

baseSpeed = Label(speedBlock, text= 'base speed')
baseSpeed.grid(row= 0, column = 3)

armorSpeed = Label(speedBlock, text= 'with armor')
armorSpeed.grid(row = 0, column = 6)

ftEntry = Entry(speedBlock, width = 3)
ftEntry.grid(row = 1, column = 2)

ftLabel = Label(speedBlock, text='FT.')
ftLabel.grid(row = 1, column = 3)

sqEntry = Entry(speedBlock, width = 3)
sqEntry.grid(row=1, column = 4)

sqLabel = Label(speedBlock, text='SQ.')
sqLabel.grid(row = 1, column = 5)

armorftEntry = Entry(speedBlock, width = 3)
armorftEntry.grid(row = 1, column = 6)

armorftLabel = Label(speedBlock, text='FT.')
armorftLabel.grid(row = 1, column = 7)

armorsqEntry = Entry(speedBlock, width = 3)
armorsqEntry.grid(row=1, column = 8)

armorsqLabel = Label(speedBlock, text='SQ.')
armorsqLabel.grid(row = 1, column = 9)

#flyftLabel = Label(speedBlock,text= 'FT' )
#flyftLabel.grid(row= 3, column = 2)

#flyspeedLabel = Label(speedBlock, text = 'fly')
#flyspeedLabel.grid(row=3, column=0)

#flyEntry = Entry(width = 2)
#flyEntry.grid(row = 3, column = 1)

swimLabel = Label(speedBlock, text='swim')
swimLabel.grid(row=3, column = 2)

swimEntry = Entry(speedBlock, width = 2)
swimEntry.grid(row=3, column=3)

#swimftLabel = Label(speedBlock, "FT")
#swimftLabel.grid(row=3, column = 4)

climbspeedLabel = Label(speedBlock, text = 'climb')
climbspeedLabel.grid(row = 3, column = 5)

climbftLabel = Label(speedBlock,text= 'FT' )
climbftLabel.grid(row = 3, column = 6)


climbEntry = Entry(speedBlock, width = 2)
climbEntry.grid(row = 3, column = 7)


burrowspeedLabel = Label(speedBlock, text = 'burrow')
burrowftLabel = Label(speedBlock,text= 'FT' )


Label(stats, text='STR', fg="white", bg="black").grid(row=5)
Label(stats, text='DEX', fg="white", bg="black").grid(row=6)
Label(stats, text='CON', fg="white", bg="black").grid(row=7)
Label(stats, text='INT', fg="white", bg="black").grid(row=8)
Label(stats, text='WIS', fg="white", bg="black").grid(row=9)
Label(stats, text='CHA', fg="white", bg="black").grid(row=10)


#character notes block
Label(notes, text='Notes', fg="white", bg="black").grid(row=30)

#character attribute input block
characterEntry = Entry(attr)
alignmentEntry = Entry(attr, width = 2)
playerEntry = Entry(attr)

classEntry = Entry(attr)
levelEntry = Entry(attr, width = 2)
dietyEntry = Entry(attr, width = 7)
homelandEntry = Entry(attr, width = 7)

for child in attr.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
sizeEntry = Entry(attr, width = 3)
raceEntry = Entry(attr)
genderEntry = Entry(attr, width = 1)
ageEntry = Entry(attr, width=2)
heightEntry = Entry(attr, width=4)
weightEntry = Entry(attr, width=3)
hairEntry = Entry(attr, width = 6)
eyesEntry = Entry(attr, width = 6)

#character stats input block
strEntry = Entry(stats, width=2)
dexEntry = Entry(stats, width=2)
conEntry = Entry(stats, width=2)
intEntry = Entry(stats, width=2)
wisEntry = Entry(stats, width=2)
chaEntry = Entry(stats, width=2)

strModEntry = Entry(stats, width=2)
dexModEntry = Entry(stats, width=2)
conModEntry = Entry(stats, width=2)
intModEntry = Entry(stats, width=2)
wisModEntry = Entry(stats, width=2)
chaModEntry = Entry(stats, width=2)

strTempEntry = Entry(stats, width=2)
dexTempEntry = Entry(stats, width=2)
conTempEntry = Entry(stats, width=2)
intTempEntry = Entry(stats, width=2)
wisTempEntry = Entry(stats, width=2)
chaTempEntry = Entry(stats, width=2)





#large text box for notes
notesTextBox = tk.Text(notes, width=50, height=10)



#page placement for character attributes
characterEntry.grid(row=0, column=1)
alignmentEntry.grid(row=0, column=3)
playerEntry.grid(row=0, column =5)

classEntry.grid(row=1, column=1)
levelEntry.grid(row=1, column=3)
dietyEntry.grid(row=1, column=5)
homelandEntry.grid(row=1, column= 7)

raceEntry.grid(row=2, column=1)
sizeEntry.grid(row=2, column = 3)
genderEntry.grid(row=2, column=5)
ageEntry.grid(row=2, column=7)
heightEntry.grid(row=2, column=9)
weightEntry.grid(row=2, column=11)
hairEntry.grid(row=2, column=13)
eyesEntry.grid(row=2, column=15)

#page placement for character stats
strEntry.grid(row=5, column=1, sticky='W', padx=30)
dexEntry.grid(row=6, column=1, sticky='W', padx=30)
conEntry.grid(row=7, column=1, sticky='W', padx=30)
intEntry.grid(row=8, column=1, sticky='W', padx=30)
wisEntry.grid(row=9, column=1, sticky='W', padx=30)
chaEntry.grid(row=10, column=1, sticky='W', padx=30)

strModEntry.grid(row=5, column=2, sticky='W')
dexModEntry.grid(row=6, column=2, sticky='W')
conModEntry.grid(row=7, column=2, sticky='W')
intModEntry.grid(row=8, column=2, sticky='W')
wisModEntry.grid(row=9, column=2, sticky='W')
chaModEntry.grid(row=10, column=2, sticky='W')

strTempEntry.grid(row=5, column=3, sticky='W', padx=15)
dexTempEntry.grid(row=6, column=3, sticky='W', padx=15)
conTempEntry.grid(row=7, column=3, sticky='W', padx=15)
intTempEntry.grid(row=8, column=3, sticky='W', padx=15)
wisTempEntry.grid(row=9, column=3, sticky='W', padx=15)
chaTempEntry.grid(row=10, column=3, sticky='W', padx=15)




#notes text box placement
notesTextBox.grid(row=31, rowspan=10, columnspan=10, stick='W')





#padding to space everything apart
for child in m.winfo_children():
    child.grid_configure(padx=5, pady=5)



root.mainloop()