import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = Tk()
window.title("Letter of Recommendation Analysis")

batch_label = Label(window, text="Batch:")
batch_label.grid(row=0, column=0)

batch_options = ["2024", "2025", "2026"]
batch_variable = StringVar(window)
batch_variable.set(batch_options[0])


batch_menu = OptionMenu(window, batch_variable, *batch_options)
batch_menu.grid(row=0, column=1)

department_label = Label(window, text="Department:")
department_label.grid(row=1, column=0)

department_options = ["COMPS", "MECHANICAL", "EXTC"]
department_variable = StringVar(window)
department_variable.set(department_options[0])

department_menu = OptionMenu(window, department_variable, *department_options)
department_menu.grid(row=1, column=1)

def submit_action():
    batch = batch_variable.get()
    department = department_variable.get()
    file_path = '/Dataset.csv'

    df = pd.read_csv(file_path)
    
    filtered_data = df[(df["Department"] == department) & (df["Batch"] == int(batch))]

    student_names = filtered_data["Student Name"].tolist()
    colleges = filtered_data["Colleges Applied"].tolist()

    result_label = Label(window, text="Student Names and Applied Colleges:")
    result_label.grid(row=2, column=0)

    result_text = Text(window, width=50, height=10)
    result_text.grid(row=3, column=0, columnspan=2)

    for name, college in zip(student_names, colleges):
        result_text.insert(END, f"{name} - {college}\n")

    fig, ax = plt.subplots(figsize=(6, 4))
    datasets = ['Applied', 'Got', 'Used']
    values = [
    df[(df["Batch"] == int(batch)) & (df["Department"] == department)]["Applied"].sum(),
    df[(df["GotRecommendation"] == 1) & (df["Department"] == department) & (df["Batch"] == int(batch))]["GotRecommendation"].sum(),
    df[(df["Used Recommendation"] == 1) & (df["Department"] == department) & (df["Batch"] == int(batch))]["Used Recommendation"].sum()
    ]


    ax.bar(datasets, values)
    ax.set_ylabel('Number of Students')
    ax.set_title('Recommendation Status')
    ax.set_ylim(0, 6)  #

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

submit_button = Button(window, text="Submit", command=submit_action)
submit_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
