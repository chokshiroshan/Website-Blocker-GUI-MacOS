import PySimpleGUI as sg

    # Very basic window.  Return values as a list

layout = [
              [sg.Radio('Block Website','r1'),sg.Radio('Unblock Website','r1')],
              [sg.Text('Website', size=(15, 1)), sg.InputText()],
              [sg.OK(), sg.Cancel()]
             ]

window = sg.Window('Website Blocker', layout)
event, values = window.Read()

print(event, values[0], values[1],values[2])


try:
    f = open('/private/etc/hosts','r+')
    content = f.read()
    finalContent = []
    def getwebsite(w):
        if "www" in w:
            w2 = w[4:]
            return w2
        else:
            w2 = "www."+w
            return w2

    if values[0] == True:
        w = values[2]
        w2 = getwebsite(w)
        if not w in content:
            f.write("127.0.0.1\t"+w+"\n")
            f.write("127.0.0.1\t"+w2+"\n")
        else:
            sg.Popup("Error","Already Blocked")
        f.close()
    elif values[0] == False:
        w = values[2]
        w = w.replace(' ', '')
        if not w == '':
            w2 = getwebsite(w)
            if not w in content:
                sg.Popup("Error", "Already Unblocked")
            else:
                f = open('/private/etc/hosts', 'w+')
                contents = content.split("\n")
                for i in contents:
                    if w in i:
                        pass
                    elif w2 in i:
                        pass
                    else:
                        finalContent.append(i)
                    # print(finalContent)
                for j in finalContent:
                    f.write(j)
                    f.write("\n")
            f.close()
        else:
            print("Enter Valid Website!")

    else:
        print("Invalid Input!")
except:
        print("Error!")
