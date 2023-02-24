import json
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

root = Tk()
root.title('- Reactor Simulator -DESPA1-')
root.config(background="gray")


class Databases_TRIGA():
    def __init__(self, path):
        self.path = path

    def read_data(self):
        '''
        This method can read database
        :return: dictionary
        '''
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data

    def save_data(self, new_data):
        '''
        this method can save the new information in databases
        :param new_data: database
        :return: none
        '''
        with open(self.path, "w") as file:
            json.dump(new_data, file, indent=3)


data1 = Databases_TRIGA("C:/Users/Gabi/PycharmProjects/despa/Aplicatie_reactor\database.json")
data_info = data1.read_data()


def extract(item, label, rod):
    if data_info["rod_position"][item] < 100:
        data_info["rod_position"][item] += 1
        label.config(text=data_info["rod_position"][item])
        excess1 = str(data_info["rod_position"]["rod1_position"])
        excess2 = str(data_info["rod_position"]["rod2_position"])
        excess3 = str(data_info["rod_position"]["rod3_position"])
        excess4 = str(data_info["rod_position"]["rod4_position"])
        excess5 = str(data_info["rod_position"]["rod5_position"])
        excess6 = str(data_info["rod_position"]["rod6_position"])
        excess7 = str(data_info["rod_position"]["rod7_position"])
        excess8 = str(data_info["rod_position"]["rod8_position"])
        x1 = data_info["control_rod1"][excess1]
        x2 = data_info["control_rod2"][excess2]
        x3 = data_info["control_rod3"][excess3]
        x4 = data_info["control_rod4"][excess4]
        x5 = data_info["control_rod5"][excess5]
        x6 = data_info["control_rod6"][excess6]
        x7 = data_info["control_rod7"][excess7]
        x8 = data_info["control_rod8"][excess8]
        negative_excess = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)
        print(x1, x2, x3, x4, x5, x6, x7, x8)
        if negative_excess < 1:
            negative_excess = 1 - negative_excess
            reactivity = (-negative_excess) * 0.007
            data_info["reactor power"] = 1 * 10 ** (reactivity / 0.13)
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            data_info["reactor period"] = 0.13 / reactivity
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
        else:
            reactivity = ((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) - 1) * 0.007
            data_info["reactor power"] = data_info["reactor power"] * 10 ** ((reactivity) / 0.13)
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            print(f'power = {data_info["reactor power"]}')
            data_info["reactor period"] = 0.13 / reactivity
            print(f' "reactor period": {data_info["period_reactor"]}')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
    else:
        data_info["rod_position"][item] = 100
    print(f'POWER: {round(float(data_info["reactor power"]), 3)} W')
    data1.save_data(data_info)


def scram():
    '''
    This function can insert very quickly all control rods in the  reactor core
    :return: dictionary
    '''
    for item in data_info["rod_position"].keys():
        data_info["rod_position"][item] = 0
        reactivity = -0.007
        data_info["reactor power"] = 1 * 10 ** (reactivity / 0.13)
    label1.config(text=data_info["rod_position"]["rod1_position"])
    label2.config(text=data_info["rod_position"]["rod2_position"])
    label3.config(text=data_info["rod_position"]["rod3_position"])
    label4.config(text=data_info["rod_position"]["rod4_position"])
    label5.config(text=data_info["rod_position"]["rod5_position"])
    label6.config(text=data_info["rod_position"]["rod6_position"])
    label7.config(text=data_info["rod_position"]["rod7_position"])
    label8.config(text=data_info["rod_position"]["rod8_position"])
    label_power.config(text=f'POWER: {round(float(data_info["reactor power"]), 3)} W')
    reactivity = -0.007
    perioad = 0.13 / reactivity
    print(f' the reactor period: {perioad}')
    label_period.config(text=f' T = {round((float(perioad)), 3)} s')
    data1.save_data(data_info)


def insert(item, label, rod):
    '''
    This function can insert a control rod into the reactor core, this can be done if
    rod position is greater than 0.Else the rod_position will remain 0.

    :param item:"rod1_position"
    :param label:label
    :param rod:"control_rod"
    :return: dictionary with new values
    '''
    excess1 = str(data_info["rod_position"]["rod1_position"])
    excess2 = str(data_info["rod_position"]["rod2_position"])
    excess3 = str(data_info["rod_position"]["rod3_position"])
    excess4 = str(data_info["rod_position"]["rod4_position"])
    excess5 = str(data_info["rod_position"]["rod5_position"])
    excess6 = str(data_info["rod_position"]["rod6_position"])
    excess7 = str(data_info["rod_position"]["rod7_position"])
    excess8 = str(data_info["rod_position"]["rod8_position"])
    x1 = data_info["control_rod1"][excess1]
    x2 = data_info["control_rod2"][excess2]
    x3 = data_info["control_rod3"][excess3]
    x4 = data_info["control_rod4"][excess4]
    x5 = data_info["control_rod5"][excess5]
    x6 = data_info["control_rod6"][excess6]
    x7 = data_info["control_rod7"][excess7]
    x8 = data_info["control_rod8"][excess8]
    print(f'the negative excess is: {x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8}')
    reactivity_past = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)
    reactivity_past = reactivity_past * 0.007
    print(f'reactivity in $ = {reactivity_past}')
    if data_info["rod_position"][item] > 0:
        data_info["rod_position"][item] -= 1
        label.config(text=data_info["rod_position"][item])
        excess1 = str(data_info["rod_position"]["rod1_position"])
        excess2 = str(data_info["rod_position"]["rod2_position"])
        excess3 = str(data_info["rod_position"]["rod3_position"])
        excess4 = str(data_info["rod_position"]["rod4_position"])
        excess5 = str(data_info["rod_position"]["rod5_position"])
        excess6 = str(data_info["rod_position"]["rod6_position"])
        excess7 = str(data_info["rod_position"]["rod7_position"])
        excess8 = str(data_info["rod_position"]["rod8_position"])
        x1 = data_info["control_rod1"][excess1]
        x2 = data_info["control_rod2"][excess2]
        x3 = data_info["control_rod3"][excess3]
        x4 = data_info["control_rod4"][excess4]
        x5 = data_info["control_rod5"][excess5]
        x6 = data_info["control_rod6"][excess6]
        x7 = data_info["control_rod7"][excess7]
        x8 = data_info["control_rod8"][excess8]
        reactivity = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
        if reactivity < 1:
            reactivity = 1 - reactivity
            reactivity = (-reactivity) * 0.007
            real_reactivity = reactivity - reactivity_past
            data_info["reactor power"] = data_info["reactor power"] * 10 ** (real_reactivity / 0.13)
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            print(f'power = {round(float(data_info["reactor power"]), 3)}')
            data_info["reactor period"] = 0.13 / reactivity
            print(f' the reactor period is: {data_info["reactor period"]}')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
        else:
            reactivity = 1 - reactivity
            reactivity = (reactivity) * 0.007
            real_reactivity = reactivity - reactivity_past
            data_info["reactor power"] = data_info["reactor power"] * 10 ** (real_reactivity / 0.13)
            label_power.config(text=f' POWER : {round(float(data_info["reactor power"]), 3)} W')
            print(f'power = {data_info["reactor power"]}')
            data_info["reactor period"] = 0.13 / reactivity
            print(f' the reactor period is: {data_info["reactor period"]}')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')

    else:
        data_info["rod_position"][item] = 0
    print(f'POWER: {round(float(data_info["reactor power"]), 3)} W')
    data1.save_data(data_info)


def bank_insert():
    '''
    This function can insert all control rods into the reactor core, this can be done if
    rods position is greater than 0.Else the rod_position will remain 0.
    :return: will be update all reactor parameters which are storage in databases
    '''
    position1 = str(data_info["rod_position"]["rod1_position"])
    position2 = str(data_info["rod_position"]["rod2_position"])
    position3 = str(data_info["rod_position"]["rod3_position"])
    position4 = str(data_info["rod_position"]["rod4_position"])
    position5 = str(data_info["rod_position"]["rod5_position"])
    position6 = str(data_info["rod_position"]["rod6_position"])
    position7 = str(data_info["rod_position"]["rod7_position"])
    position8 = str(data_info["rod_position"]["rod8_position"])
    x1 = data_info["control_rod1"][position1]
    x2 = data_info["control_rod2"][position2]
    x3 = data_info["control_rod3"][position3]
    x4 = data_info["control_rod4"][position4]
    x5 = data_info["control_rod5"][position5]
    x6 = data_info["control_rod6"][position6]
    x7 = data_info["control_rod7"][position7]
    x8 = data_info["control_rod8"][position8]
    reactivity_past = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)
    reactivity_past = reactivity_past * 0.007
    for item in data_info["rod_position"].keys():
        if data_info["rod_position"][item] > 0:
            data_info["rod_position"][item] -= 1
        label1.config(text=data_info["rod_position"]["rod1_position"])
        label2.config(text=data_info["rod_position"]["rod2_position"])
        label3.config(text=data_info["rod_position"]["rod3_position"])
        label4.config(text=data_info["rod_position"]["rod4_position"])
        label5.config(text=data_info["rod_position"]["rod5_position"])
        label6.config(text=data_info["rod_position"]["rod6_position"])
        label7.config(text=data_info["rod_position"]["rod7_position"])
        label8.config(text=data_info["rod_position"]["rod8_position"])
        excess1 = str(data_info["rod_position"]["rod1_position"])
        excess2 = str(data_info["rod_position"]["rod2_position"])
        excess3 = str(data_info["rod_position"]["rod3_position"])
        excess4 = str(data_info["rod_position"]["rod4_position"])
        excess5 = str(data_info["rod_position"]["rod5_position"])
        excess6 = str(data_info["rod_position"]["rod6_position"])
        excess7 = str(data_info["rod_position"]["rod7_position"])
        excess8 = str(data_info["rod_position"]["rod8_position"])
        x1 = data_info["control_rod1"][excess1]
        x2 = data_info["control_rod2"][excess2]
        x3 = data_info["control_rod3"][excess3]
        x4 = data_info["control_rod4"][excess4]
        x5 = data_info["control_rod5"][excess5]
        x6 = data_info["control_rod6"][excess6]
        x7 = data_info["control_rod7"][excess7]
        x8 = data_info["control_rod8"][excess8]
        reactivity = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
        if reactivity < 1:
            reactivity = 1 - reactivity
            reactivity = (-reactivity) * 0.007
            real_reactivity = reactivity - reactivity_past
            data_info["reactor power"] = data_info["reactor power"] * 10 ** (real_reactivity / 0.13)
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            print(f'power = {data_info["reactor power"]}')
            data_info["reactor period"] = 0.13 / reactivity
            print(f' the reactor period is: {data_info["reactor period"]}')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
        else:
            reactivity = 1 - reactivity
            reactivity = (reactivity) * 0.007
            real_reactivity = reactivity - reactivity_past
            data_info["reactor power"] = data_info["reactor power"] * 10 ** (real_reactivity / 0.13)
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            print(f'power = {data_info["reactor power"]}')
            data_info["reactor period"] = 0.13 / reactivity
            print(f' the reactor period is: {data_info["reactor period"]}')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
    # else:
    #     data_info["rod_position"][item] = 0
    #     print(f'POWER: {data_info["power_reactor"]} W')
    #     label_power.config(text=f' POWER: {round(float(data_info["power_reactor"]), 3)} W')
    #     label_period.config(text=f' T = {round(float(data_info["period_reactor"]), 3)} s')
    #     data1.save_data(data_info)


def bank_extract():
    '''
    This function can extract all control rods from the reactor core, this can be done if
    rods position is smaller than 100.Else the rod_position will remain 100.
    :return: will be update all reactor parameters which are storage in databases
    '''
    for item in data_info["rod_position"].keys():
        if data_info["rod_position"][item] < 100:
            data_info["rod_position"][item] += 1
            label1.config(text=data_info["rod_position"]["rod1_position"])
            label2.config(text=data_info["rod_position"]["rod2_position"])
            label3.config(text=data_info["rod_position"]["rod3_position"])
            label4.config(text=data_info["rod_position"]["rod4_position"])
            label5.config(text=data_info["rod_position"]["rod5_position"])
            label6.config(text=data_info["rod_position"]["rod6_position"])
            label7.config(text=data_info["rod_position"]["rod7_position"])
            label8.config(text=data_info["rod_position"]["rod8_position"])
            excess1 = str(data_info["rod_position"]["rod1_position"])
            excess2 = str(data_info["rod_position"]["rod2_position"])
            excess3 = str(data_info["rod_position"]["rod3_position"])
            excess4 = str(data_info["rod_position"]["rod4_position"])
            excess5 = str(data_info["rod_position"]["rod5_position"])
            excess6 = str(data_info["rod_position"]["rod6_position"])
            excess7 = str(data_info["rod_position"]["rod7_position"])
            excess8 = str(data_info["rod_position"]["rod8_position"])
            x1 = data_info["control_rod1"][excess1]
            x2 = data_info["control_rod2"][excess2]
            x3 = data_info["control_rod3"][excess3]
            x4 = data_info["control_rod4"][excess4]
            x5 = data_info["control_rod5"][excess5]
            x6 = data_info["control_rod6"][excess6]
            x7 = data_info["control_rod7"][excess7]
            x8 = data_info["control_rod8"][excess8]
            negative_excess = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) * 8
            print(f' negative excess  {negative_excess}')
            if negative_excess < 1:
                negative_excess = 1 - negative_excess
                print(f'1-negative excess {negative_excess}')
                reactivity = -(negative_excess) * 0.007
                print(f'reactivity is {reactivity}')
                data_info["reactor power"] = 1 * 10 ** (reactivity / 0.13)
                label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
                print(f'reactor power is: {data_info["reactor power"]} W')
                print("*************************")
                data_info["reactor period"] = 0.13 / reactivity
                print(f' the reactor period is: {data_info["reactor period"]}')
                label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
            else:
                reactivity = ((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) - 1) * 0.007
                data_info["reactor power"] = data_info["reactor power"] * 10 ** ((reactivity) / 0.13)
                label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
                print(f'power = {data_info["reactor power"]}')
                data_info["reactor period"] = 0.13 / reactivity
                print(f' the reactor period is: {data_info["reactor period"]}')
                label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
        else:
            print(f'POWER: {round(float(data_info["reactor power"]), 3)} W')
            label_power.config(text=f' POWER: {round(float(data_info["reactor power"]), 3)} W')
            label_period.config(text=f' T = {round(float(data_info["reactor period"]), 3)} s')
            data_info["rod_position"][item] = 100

    data1.save_data(data_info)


plt.style.use('fivethirtyeight')
# values for first graph
x_vals = []
y_vals = []
index1 = count()


def animate(i):
    """
    this function is used for update the graph values in real time

    :return: none
    """
    x_vals.append(next(index1))
    y_vals.append(data_info["reactor power"])
    plt.cla()  # clear the current axes
    plt.plot(x_vals, y_vals)
    # x_vals.label("Reactor Power (W)")
    # y_vals.label("Time (s)")
    # time.sleep(1)


# graph1
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.get_tk_widget().grid(column=3, row=5, columnspan=4)
ani1 = FuncAnimation(plt.gcf(), animate, interval=10)

button_extract1 = Button(root, padx=20, pady=20, text="Extract CR1", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod1_position", label1, "control_rod1"))
button_insert1 = Button(root, padx=20, pady=20, text=" Insert  CR1 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod1_position", label1, "control_rod1"))
button_extract2 = Button(root, padx=20, pady=20, text="Extract CR2", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod2_position", label2, "control_rod2"))
button_insert2 = Button(root, padx=20, pady=20, text=" Insert  CR2 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod2_position", label2, "control_rod2"))
button_extract3 = Button(root, padx=20, pady=20, text="Extract CR3", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod3_position", label3, "control_rod3"))
button_insert3 = Button(root, padx=20, pady=20, text=" Insert  CR3 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod3_position", label3, "control_rod3"))
button_extract4 = Button(root, padx=20, pady=20, text="Extract  CR4", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod4_position", label4, "control_rod4"))
button_insert4 = Button(root, padx=20, pady=20, text=" Insert  CR4 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod4_position", label4, "control_rod4"))
button_extract5 = Button(root, padx=20, pady=20, text="Extract CR5", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod5_position", label5, "control_rod5"))
button_insert5 = Button(root, padx=20, pady=20, text=" Insert  CR5 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod5_position", label5, "control_rod5"))
button_extract6 = Button(root, padx=20, pady=20, text="Extract CR6", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod6_position", label6, "control_rod6"))
button_insert6 = Button(root, padx=20, pady=20, text=" Insert  CR6 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod6_position", label6, "control_rod6"))
button_extract7 = Button(root, padx=20, pady=20, text="Extract CR7", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod7_position", label7, "control_rod7"))
button_insert7 = Button(root, padx=20, pady=20, text=" Insert  CR7 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod7_position", label7, "control_rod7"))
button_extract8 = Button(root, padx=20, pady=20, text="Extract CR8", font=30, bg='blue', fg='white',
                         borderwidth=15, command=lambda: extract("rod8_position", label8, "control_rod8"))
button_insert8 = Button(root, padx=20, pady=20, text=" Insert  CR8 ", font=30, bg='blue', fg='white',
                        borderwidth=15, command=lambda: insert("rod8_position", label8, "control_rod8"))
button_BANK_EXTRACT = Button(root, padx=20, pady=20, text="  BANK  \n   EXTRACT  ", font=20, bg='yellow', fg='black',
                             borderwidth=10, command=bank_extract)
button_BANK_INSERT = Button(root, padx=20, pady=20, text="   BANK   \n      INSERT     ", font=20, bg='yellow',
                            fg='black',
                            borderwidth=10, command=bank_insert)

button_scram = Button(root, padx=20, pady=20, text="   SCRAM \n  REACTOR  ", font=30, bg='red', fg='yellow',
                      borderwidth=10,
                      command=scram)

label1 = Label(root, text=data_info["rod_position"]["rod1_position"])
label1.grid(row=1, column=1)
label2 = Label(root, text=data_info["rod_position"]["rod2_position"])
label2.grid(row=1, column=2)
label3 = Label(root, text=data_info["rod_position"]["rod3_position"])
label3.grid(row=1, column=3)
label4 = Label(root, text=data_info["rod_position"]["rod4_position"])
label4.grid(row=1, column=4)
label5 = Label(root, text=data_info["rod_position"]["rod5_position"])
label5.grid(row=1, column=5)
label6 = Label(root, text=data_info["rod_position"]["rod6_position"])
label6.grid(row=1, column=6)
label7 = Label(root, text=data_info["rod_position"]["rod7_position"])
label7.grid(row=1, column=7)
label8 = Label(root, text=data_info["rod_position"]["rod8_position"])
label8.grid(row=1, column=8)

label_power = Label(root, font=30, bg="black", fg="red", text=f'POWER: {round(float(data_info["reactor power"]), 3)} W')
label_power.grid(row=0, column=3, columnspan=4)
label_period = Label(root, font=30, bg="black", fg="red", text=f'T =  {round(float(data_info["reactor period"]), 3)} W')
label_period.grid(row=0, column=2, columnspan=2)

button_extract1.grid(row=2, column=1)
button_insert1.grid(row=3, column=1)
button_extract2.grid(row=2, column=2)
button_insert2.grid(row=3, column=2)
button_extract3.grid(row=2, column=3)
button_insert3.grid(row=3, column=3)
button_extract4.grid(row=2, column=4)
button_insert4.grid(row=3, column=4)
button_extract5.grid(row=2, column=5)
button_insert5.grid(row=3, column=5)
button_extract6.grid(row=2, column=6)
button_insert6.grid(row=3, column=6)
button_extract7.grid(row=2, column=7)
button_insert7.grid(row=3, column=7)
button_extract8.grid(row=2, column=8)
button_insert8.grid(row=3, column=8)

button_scram.grid(row=4, column=3)
button_BANK_EXTRACT.grid(row=4, column=4)
button_BANK_INSERT.grid(row=4, column=5)
root.mainloop()
