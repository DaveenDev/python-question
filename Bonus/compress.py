import PySimpleGUI as gui

label1 = gui.Text("Select files to compress:")
input1 = gui.Input()
button1 = gui.FileBrowse("Choose")

label2 = gui.Text("Select destination folder:")
input2 = gui.Input()
button2 = gui.FolderBrowse("Choose")
btnCompress = gui.Button("Compress")

window = gui.Window("File Compressor",
                    layout=[[label1,input1,button1],
                            [label2, input2, button2],
                            [btnCompress]]
                    )
window.read()