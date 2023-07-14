import tkinter as tk
from tkinter import messagebox

# Function to handle the mood selection and store the data
def record_mood():
    mood = mood_var.get()  # Get selected mood from dropdown
    if mood:
        # Append the mood to a text file or a database
        with open('mood_data.txt', 'a') as file:
            file.write(mood + '\n')
        messagebox.showinfo('Success', 'Mood recorded successfully!')
    else:
        messagebox.showwarning('Warning', 'Please select a mood.')

# Create the main application window
app = tk.Tk()
app.title('Mood Tracker')

# Create the mood selection dropdown
moods = ['Happy', 'Sad', 'Angry', 'Excited', 'Calm']
mood_var = tk.StringVar(app)
mood_var.set(moods[0])
mood_dropdown = tk.OptionMenu(app, mood_var, *moods)
mood_dropdown.pack(pady=10)

# Create the record button
record_button = tk.Button(app, text='Record Mood', command=record_mood)
record_button.pack(pady=10)

# Run the application
app.mainloop()
