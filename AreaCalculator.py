import PySimpleGui as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Filename')]],[sg.Input(), sg.filebrowse()],[sg.OK(), sg.Cancel()]

def calculateArea():
    length = int(input("\nInput Length:"))
    width = int(input("\nInput Width:"))
    height = int(input("\nInput Height:"))
    
    area = int(length) * int(width) * int(height)
        
    print("The total area is", area)
    
calculateArea()
    
