from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Intrest Calculator')
root.configure(background='black')
messagebox.showinfo("Information", """What unit should I use?

1. Enter the principal in any currency,
you'll get the answer in the same
currency.

2. Enter the time in years

3. Enter the rate of interest in
percentage.""")

# Defining functions
def intrest_calculator(p, t, r):
    """
Returns simple interest
    """
    return (p * t * r) / 100


def Submit():
"""
Creates final window with interest displayed
"""
    try:
        int_ = intrest_calculator(int(principal.get()), int(time.get()), int(rate.get()))
        display_value = f'{principal.get()} becomes {int(int_) + int(principal.get())} after {time.get()} years at a rate of {rate.get()}%'
        principal_.destroy()
        time_.destroy()
        rate_.destroy()
        rate.destroy()
        time.destroy()
        intrest_display = Label(root, text=display_value, font=('Helveltica', 22), background='black', fg='white')
        intrest_display.grid(row=0, column=0)
        principal.destroy()
        submit.destroy()
    except:
        messagebox.showerror("ERROR!", """Sorry, an error occured.
1. Try entering all three fields.
2. Try using only numbers, not letters or symbols to fill the
fields.
""")

# Defining widgets
principal_ = Label(root, text='Principal', font=('Helveltica', 22), background='black', fg='white')
time_ = Label(root, text="Years", font=('Helveltica', 22), bg='black', fg='white')
rate_ = Label(root, text="Rate of Interest", font=('Helveltica', 22), background='black', fg='white')
principal = Entry(root, bd=5, font=('Helveltica', 22), fg='black')
time = Entry(root, bd=5, font=('Helveltica', 22), fg='black')
rate = Entry(root, bd=5, font=('Helveltica', 22), fg='black')
submit = Button(root, text='Calculate Interest', padx=50, font=('Helveltica', 22), command=Submit, background='black', fg='white')

# Packing widgets
principal_.grid(row=0, column=0)
time_.grid(row=1, column=0)
rate_.grid(row=2, column=0)
principal.grid(row=0, column=1)
time.grid(row=1, column=1)
rate.grid(row=2, column=1)
submit.grid(row=3, column=0, columnspan=2)

root.mainloop()
