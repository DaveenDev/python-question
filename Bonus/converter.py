import PySimpleGUI as gui

input1 = gui.InputText()
input2 = gui.InputText()
button = gui.Button("Conver")

window = gui.Window("Converter",
                    layout=[[gui.Text("Enter Feet:"), input1],
                            [gui.Text("Enter inches"), input2],
                            [button]])
window.read()