import wx
import os

def search(event):  # searches for patient

    dname = ['Name: ','Admission date: ','Date_Of_Birth: ','SL_No: ','Married: ','Residence: ','City: ','State: ','Zip: ','Phone: ','Symptoms: ','Spouse/Parent: ','Insurance: ','Policy: ','Medication(current): ','Allergy: ']
    try:
        global userInput
        userInput = fileName.GetValue()
        file = open("outputfile.txt")
        file2 = open("indexfile.txt")
        if userInput not in file2:
            contents.SetValue("%s not available\nSearch for another name" % (userInput))
            return
        te = ""
        for line in file:  # read output file
            if userInput in line:
                te = te + line
                break
        te_list = []
        te_list = te.split('|')
        count = -1
        te_print = None
        count2 = 0
        i = None
        for i in dname:  # store output in string and print it
            if te_print == None:
                te_print = i + te_list[count2] + "\n"
                count2 +=1
            else:
                te_print = te_print + i + te_list[count2] + "\n"
                count2 += 1
        contents.SetValue(te_print)
        count = -1
        file.close()
    except(IOError):
        userInput = " "
        contents.SetValue("Patient does not exist\nSearch for another Patient")

def dele(event):  # deletes patient

    try:
        global userInput
        userInput = fileName.GetValue()
        file1 = open("outputfile.txt", "r")
        file2 = open("indexfile.txt", "r")
        if userInput not in file2:
            contents.SetValue("%s not available\nSearch for another name" % (userInput))
            return
        lis = ""
        for l in file1:
            if userInput in l:
                continue
            lis = lis + l
        lis1 = ""
        for k in file2:
            if userInput in k:
                continue
            lis1 = lis1 + k
        file1.close()
        file2.close()
        file1 = open("outputfile.txt", "w")
        file2 = open("indexfile.txt", "w")
        file1.write(lis)
        file2.write(lis1)
        file1.close()
        file2.close()
        contents.SetValue("%s Deleted" % (userInput))
    except(IOError):
        userInput = " "
        contents.SetValue("Paitent does not exist\nSearch for another Patient")

def lis(event):  # list all patient

    try:
        global userInput, listtxt
        fileindex = open("indexfile.txt")
        txtdir = "List of Patient Files:\n\n"
        for i in fileindex:
            txtdir = txtdir + i
        contents.SetValue(txtdir)
    except(IOError):
        userInput = "No Patients To Display"

def save(event):  # modifies patient record
    try:
        global userInput
        userInput = fileName.GetValue()
        file1 = open("outputfile.txt", "r")
        file2 = open("indexfile.txt", "r")
        if userInput not in file2:
            contents.SetValue("%s not available\nSearch for another name" % (userInput))
            return
        lis = ""
        for l in file1:
            if userInput in l:
                continue
            lis = lis + l
        lis1 = ""
        for k in file2:
            if userInput in k:
                continue
            lis1 = lis1 + k
        file1.close()
        file2.close()
        file1 = open("outputfile.txt", "w")
        file2 = open("indexfile.txt", "w")
        file1.write(lis)
        file2.write(lis1)
        file1.close()
        file2.close()
        contents.SetValue("Modifying %s" % (userInput))
        newGUI2 = PatientGUI()
        newGUI2.PatientGUImaker()
    except(IOError):
        userInput = " "
        contents.SetValue("Paitent does not exist\nSearch for another Patient")

def newPatient(event):
    newGUI = PatientGUI()
    newGUI.PatientGUImaker()

class mainGUI:
    def mainGUImaker(self):  # Main Interface
        global fileName
        global contents
        dlg = LoginDialog()
        dlg.ShowModal()
        authenticated = dlg.logged_in
        if not authenticated:
            self.Close()
        app = wx.App()
        win = wx.Frame(None, title="Patient Admission System", size=(700, 350))
        bkg = wx.Panel(win)

        searchButton = wx.Button(bkg, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, search)

        modifyButton = wx.Button(bkg, label="Modify")
        modifyButton.Bind(wx.EVT_BUTTON, save)

        deleteButton = wx.Button(bkg, label="Delete")
        deleteButton.Bind(wx.EVT_BUTTON, dele)

        listButton = wx.Button(bkg, label="List")
        listButton.Bind(wx.EVT_BUTTON, lis)

        newPatientButton = wx.Button(bkg, label="Create")
        newPatientButton.Bind(wx.EVT_BUTTON, newPatient)

        fileName = wx.TextCtrl(bkg)
        contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
        contents.SetValue("Welcome to patient record management.\nPlease select the required option.")
        hbox = wx.BoxSizer()
        hbox.Add(fileName, proportion=1, flag=wx.EXPAND)
        hbox.Add(newPatientButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(listButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(searchButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(modifyButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(deleteButton, proportion=0, flag=wx.LEFT, border=5)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.LEFT | wx.LEFT, border=5)
        bkg.SetSizer(vbox)

        win.Show()
        app.MainLoop()

class PatientGUI:
    def PatientGUImaker(self):  # code for record creation(GUI)

        app = wx.App()
        win = wx.Frame(None, title="Patient Details", size=(300, 600))
        bkg = wx.Panel(win)

        # Creating the static texts
        self.nameLabel = wx.StaticText(bkg, label="Patient's  Name:                  ")
        self.dateLabel = wx.StaticText(bkg, label="Admission Date:                  ")
        self.birthLabel = wx.StaticText(bkg, label="Birth Date:                            ")
        self.SSLabel = wx.StaticText(bkg, label="SL No:                                   ")
        self.marryLabel = wx.StaticText(bkg, label="Married:                                ")
        self.streetLabel = wx.StaticText(bkg, label="Street of Residence:            ")
        self.cityLabel = wx.StaticText(bkg, label="City:                                       ")
        self.stateLabel = wx.StaticText(bkg, label="State:                                     ")
        self.zipLabel = wx.StaticText(bkg, label="Zip Code:                              ")
        self.teleLabel = wx.StaticText(bkg, label="Home Telephone:               ")
        self.symptomLabel = wx.StaticText(bkg, label="Symptoms:                           ")
        self.spouseLabel = wx.StaticText(bkg, label="Spouse or Parent Name:     ")
        self.priLabel = wx.StaticText(bkg, label="Primary Insurance:              ")
        self.polLabel1 = wx.StaticText(bkg, label="Policy:                                   ")
        self.mediLabel = wx.StaticText(bkg, label="Current Medication:            ")
        self.alleLabel = wx.StaticText(bkg, label="Allergies:                               ")

        # Creating the CtrlTexts
        self.nameText = wx.TextCtrl(bkg)
        self.dateText = wx.TextCtrl(bkg)
        self.birthText = wx.TextCtrl(bkg)
        self.SSText = wx.TextCtrl(bkg)
        self.marryText = wx.TextCtrl(bkg)
        self.streetText = wx.TextCtrl(bkg)
        self.cityText = wx.TextCtrl(bkg)
        self.stateText = wx.TextCtrl(bkg)
        self.zipText = wx.TextCtrl(bkg)
        self.teleText = wx.TextCtrl(bkg)
        self.symptomText = wx.TextCtrl(bkg)
        self.spouseText = wx.TextCtrl(bkg)
        self.priText = wx.TextCtrl(bkg)
        self.polText1 = wx.TextCtrl(bkg)
        self.mediText = wx.TextCtrl(bkg)
        self.alleText = wx.TextCtrl(bkg)
        # Creating the Buttons
        self.finishButton = wx.Button(bkg, label="Finish")
        self.finishButton.Bind(wx.EVT_BUTTON, self.finish)

        # Creating sizers
        b1 = wx.BoxSizer(wx.HORIZONTAL)
        b1.Add(self.nameLabel, proportion=0, flag=wx.LEFT, border=5)
        b1.Add(self.nameText, proportion=0, flag=wx.LEFT, border=5)
        box1 = wx.BoxSizer(wx.VERTICAL)
        box1.Add(b1, proportion=0, flag=wx.LEFT, border=5)

        b4 = wx.BoxSizer(wx.HORIZONTAL)
        b4.Add(self.dateLabel, proportion=0, flag=wx.LEFT, border=5)
        b4.Add(self.dateText, proportion=0, flag=wx.LEFT, border=5)
        box4 = wx.BoxSizer(wx.VERTICAL)
        box4.Add(b4, proportion=0, flag=wx.LEFT, border=5)

        b2 = wx.BoxSizer(wx.HORIZONTAL)
        b2.Add(self.birthLabel, proportion=0, flag=wx.LEFT, border=5)
        b2.Add(self.birthText, proportion=0, flag=wx.LEFT, border=5)
        box2 = wx.BoxSizer(wx.VERTICAL)
        box2.Add(b2, proportion=0, flag=wx.LEFT, border=5)

        b3 = wx.BoxSizer(wx.HORIZONTAL)
        b3.Add(self.SSLabel, proportion=0, flag=wx.LEFT, border=5)
        b3.Add(self.SSText, proportion=0, flag=wx.LEFT, border=5)
        box3 = wx.BoxSizer(wx.VERTICAL)
        box3.Add(b3, proportion=0, flag=wx.LEFT, border=5)

        b5 = wx.BoxSizer(wx.HORIZONTAL)
        b5.Add(self.marryLabel, proportion=0, flag=wx.LEFT, border=5)
        b5.Add(self.marryText, proportion=0, flag=wx.LEFT, border=5)
        box5 = wx.BoxSizer(wx.VERTICAL)
        box5.Add(b5, proportion=0, flag=wx.LEFT, border=5)

        b6 = wx.BoxSizer(wx.HORIZONTAL)
        b6.Add(self.streetLabel, proportion=0, flag=wx.LEFT, border=5)
        b6.Add(self.streetText, proportion=0, flag=wx.LEFT, border=5)
        box6 = wx.BoxSizer(wx.VERTICAL)
        box6.Add(b6, proportion=0, flag=wx.LEFT, border=5)

        b7 = wx.BoxSizer(wx.HORIZONTAL)
        b7.Add(self.cityLabel, proportion=0, flag=wx.LEFT, border=5)
        b7.Add(self.cityText, proportion=0, flag=wx.LEFT, border=5)
        box7 = wx.BoxSizer(wx.VERTICAL)
        box7.Add(b7, proportion=0, flag=wx.LEFT, border=5)

        b8 = wx.BoxSizer(wx.HORIZONTAL)
        b8.Add(self.stateLabel, proportion=0, flag=wx.LEFT, border=5)
        b8.Add(self.stateText, proportion=0, flag=wx.LEFT, border=5)
        box8 = wx.BoxSizer(wx.VERTICAL)
        box8.Add(b8, proportion=0, flag=wx.LEFT, border=5)

        b9 = wx.BoxSizer(wx.HORIZONTAL)
        b9.Add(self.zipLabel, proportion=0, flag=wx.LEFT, border=5)
        b9.Add(self.zipText, proportion=0, flag=wx.LEFT, border=5)
        box9 = wx.BoxSizer(wx.VERTICAL)
        box9.Add(b9, proportion=0, flag=wx.LEFT, border=5)

        b10 = wx.BoxSizer(wx.HORIZONTAL)
        b10.Add(self.teleLabel, proportion=0, flag=wx.LEFT, border=5)
        b10.Add(self.teleText, proportion=0, flag=wx.LEFT, border=5)
        box10 = wx.BoxSizer(wx.VERTICAL)
        box10.Add(b10, proportion=0, flag=wx.LEFT, border=5)

        b11 = wx.BoxSizer(wx.HORIZONTAL)
        b11.Add(self.symptomLabel, proportion=0, flag=wx.LEFT, border=5)
        b11.Add(self.symptomText, proportion=0, flag=wx.LEFT, border=5)
        box11 = wx.BoxSizer(wx.VERTICAL)
        box11.Add(b11, proportion=0, flag=wx.LEFT, border=5)

        b13 = wx.BoxSizer(wx.HORIZONTAL)
        b13.Add(self.spouseLabel, proportion=0, flag=wx.LEFT, border=5)
        b13.Add(self.spouseText, proportion=0, flag=wx.LEFT, border=5)
        box13 = wx.BoxSizer(wx.VERTICAL)
        box13.Add(b13, proportion=0, flag=wx.LEFT, border=5)

        b14 = wx.BoxSizer(wx.HORIZONTAL)
        b14.Add(self.priLabel, proportion=0, flag=wx.LEFT, border=5)
        b14.Add(self.priText, proportion=0, flag=wx.LEFT, border=5)
        box14 = wx.BoxSizer(wx.VERTICAL)
        box14.Add(b14, proportion=0, flag=wx.LEFT, border=5)

        b15 = wx.BoxSizer(wx.HORIZONTAL)
        b15.Add(self.polLabel1, proportion=0, flag=wx.LEFT, border=5)
        b15.Add(self.polText1, proportion=0, flag=wx.LEFT, border=5)
        box15 = wx.BoxSizer(wx.VERTICAL)
        box15.Add(b15, proportion=0, flag=wx.LEFT, border=5)

        b20 = wx.BoxSizer(wx.HORIZONTAL)
        b20.Add(self.mediLabel, proportion=0, flag=wx.LEFT, border=5)
        b20.Add(self.mediText, proportion=0, flag=wx.LEFT, border=5)
        box20 = wx.BoxSizer(wx.VERTICAL)
        box20.Add(b20, proportion=0, flag=wx.LEFT, border=5)

        b21 = wx.BoxSizer(wx.HORIZONTAL)
        b21.Add(self.alleLabel, proportion=0, flag=wx.LEFT, border=5)
        b21.Add(self.alleText, proportion=0, flag=wx.LEFT, border=5)
        box21 = wx.BoxSizer(wx.VERTICAL)
        box21.Add(b21, proportion=0, flag=wx.LEFT, border=5)

        final = wx.BoxSizer(wx.VERTICAL)
        final.Add(box1, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box4, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box2, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box3, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box5, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box6, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box7, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box8, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box9, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box10, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box11, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box13, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box14, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box15, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box20, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box21, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(self.finishButton, proportion=1, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, border=5)
        bkg.SetSizer(final)
        win.Show()
        app.MainLoop()

    def finish(self, event):
        default = open("Patient_Template.txt")
        output = open("outputfile.txt", 'a')
        indexfile = open("indexfile.txt", 'a')
        info = []
        index = []
        if self.nameText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
            index.append("Unspecified")
        else:
            info.append(self.nameText.GetValue())
            info.append("|")
            index.append(self.nameText.GetValue())
        if self.dateText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.dateText.GetValue())
            info.append("|")
        if self.birthText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.birthText.GetValue())
            info.append("|")
        if self.SSText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.SSText.GetValue())
            info.append("|")
        # info.append(self.singleText.GetValue())
        if self.marryText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.marryText.GetValue())
            info.append("|")
        if self.streetText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.streetText.GetValue())
            info.append("|")
        if self.cityText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.cityText.GetValue())
            info.append("|")
        if self.stateText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.stateText.GetValue())
            info.append("|")
        if self.zipText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.zipText.GetValue())
            info.append("|")
        if self.teleText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.teleText.GetValue())
            info.append("|")
        if self.symptomText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.symptomText.GetValue())
            info.append("|")
        # info.append(self.posText.GetValue())
        if self.symptomText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.spouseText.GetValue())
            info.append("|")
        if self.priText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.priText.GetValue())
            info.append("|")
        if self.polText1.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.polText1.GetValue())
            info.append("|")
        if self.mediText.IsEmpty():
            info.append("Unspecified")
            info.append("|")
        else:
            info.append(self.mediText.GetValue())
            info.append("|")
        if self.alleText.IsEmpty():
            info.append("Unspecified")
        else:
            info.append(self.alleText.GetValue())
        info.append("\n")
        index.append("\n")
        str1=''.join(info)
        output.write(str1)
        str2=''.join(index)
        indexfile.write(str2)
        default.close()
        output.close()
        contents.SetValue("Patient record created!!")

class LoginDialog(wx.Dialog):#Class to define login dialog
    def __init__(self):#Constructor
        wx.Dialog.__init__(self, None, title="Login", size=(250, 250))
        self.logged_in = False
        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)
        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
        p_sizer.Add(self.password, 0, wx.ALL, 5)
        # comment info
        c_sizer = wx.BoxSizer(wx.HORIZONTAL)
        c_lbl = wx.StaticText(self, label="")
        c_sizer.Add(c_lbl, 0, wx.ALL | wx.CENTER, 5)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(c_sizer, 0, wx.ALL, 5)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)
        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    def onLogin(self, event):# Check credentials and login
        stupid_user = "admin"
        stupid_password = "admin"
        user_id = self.user.GetValue()
        user_password = self.password.GetValue()
        if user_password == stupid_password and user_id == stupid_user:
            self.logged_in = True
            self.Close()
        else:
            com_lbl = wx.StaticText(self, wx.ALIGN_BOTTOM, label="    Username or Password Incorrect!")

if __name__ == "__main__":
    app = wx.App(False)
    newGUI = mainGUI()
    newGUI.mainGUImaker()