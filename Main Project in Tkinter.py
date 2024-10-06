from tkinter import *
from tkinter import messagebox
import time

class student:
   def __init__(self, name,father_name,age,class_name,roll_no):
    self.name = name
    self.father_name = father_name
    self.age = age
    self.class_name = class_name
    self.roll_no = roll_no

class StudentManager:
    def __init__(self):
        self.student=[]

    def add_student(self,student):
        self.student.append(student)

    def remove_student(self,name,roll_no):
        for student in self.student:
            if student.name == name and student.roll_no == roll_no:
                self.student.remove(student)
                return True
        return False
    def get_student(self):
        for student in self.student:
            print(f"Name:{student.name},Father:{student.father_name},Age:{student.age},Class:{student.class_name},Roll No:{student.roll_no}")

class teacher:
   def __init__(self,name,address,contact,salary,class_name):
      self.name = name
      self.address = address
      self.contact = contact
      self.salary = salary
      self.class_name = class_name

class teacherManager:
   def __init__(self):
      self.teacher=[]

   def add_teacher(self,teacher):
      self.teacher.append(teacher)

   def remove_teacher(self,name,class_name):
      for teacher in self.teacher:
         if teacher.name == name and teacher.class_name == class_name:
            self.teacher.remove(teacher)
            return True
      return False

   def get_teacher(self):
      for teacher in self.teacher:
         print(f"Name:{teacher.name},address:{teacher.address},contact:{teacher.contact},salary:{teacher.salary},class_name:{teacher.class_name}")

class fee_voucher:
   def __init__(self, name,roll_no,date,month,amount):
    self.name = name
    self.roll_no = roll_no
    self.date = date
    self.month = month
    self.amount = amount

class fee_Manager:
    def __init__(self):
        self.fee_voucher=[]

w=Tk()

# using center position
width=500
height=250
sys_width=w.winfo_screenwidth()
sys_height=w.winfo_screenheight()
c_x=int(sys_width/2-width/2)
c_y=int(sys_height/2-height/2)
w.geometry(f"{width}x{height}+{c_x}+{c_y}")
w.config(bg="sky blue")
w.overrideredirect(1)
photo2=PhotoImage(file="resize2.png")
lb = Label(w,image=photo2)
lb.place(x=0,y=0)


label1=Label(w, text='Welcome to \nSchool Management system',fg='dark blue',bg='white',font=('Time new Roman',24,"bold"))
label1.place(x=30,y=80)

label2=Label(w, text='Loading...',fg='black',bg='white',font=('Calibri',11))
label2.place(x=10,y=215)

def new_win():
    w.destroy()

    
    root=Tk()
    root.title('main window')
    root.geometry("500x500")
    root.config(bg="cyan4")
    
    photo=PhotoImage(file="sms logo.png")
    #we use in compund top ,bottom,right,left
    lb = Label(root,image=photo,bg='cyan4')
    lb.place(x=40,y=100,height=500,width=500)
    
    global entry1
    global entry2

    

    label_1 = Label(root, text= 'Login Page', bg='cyan4',fg='cyan', font=('Time new roman',30,'bold'))
    label_1.place(x=850,y=80)

    label_2 = Label(root,text= "UserName :",font=('Time new roman',20),bg='cyan4',fg='white')
    label_2.place(x=700,y=200)

    label_3 = Label(root,text=' Password :',font=('Time new roman',20),bg='cyan4',fg='white')
    label_3.place(x=700,y=340)

    entry1 = Entry(root, font=('Areal',15))
    entry1.place(x=900,y=210)

    entry2 = Entry(root, font=('Areal',15),show='*')
    entry2.place(x=900,y=350)


    # Login function
    def login():
        username = entry1.get()
        password = entry2.get()
        if username == '' and password == '':
             messagebox.showerror('login', 'Blanks are not allowed')
        elif username == 'dua' and password == '00':
            messagebox.showinfo("Login", "Login Successful!")
            root.destroy()  # Close login window
            open_main_menu()  # Open main menu
        else:
            messagebox.showerror("Error", "Incorrect Username or Password")



    button = Button(root, text='login',bg='cyan3',font=('Areal',20),bd=5, command=login)
    button.place(x=860,y=450,width=100,height=50)

    root.state('zoomed')
    
    root.mainloop()

def open_main_menu():
    top = Tk()
    top.title('DRM School Management System')
    top.geometry("500x400")
    top.config(bg='white')

    def show_frame(frame):
        frame.tkraise()

    main_menu = Frame(top,bg='white')
    student_data_frame = Frame(top,bg='cyan3')
    teacher_data_frame = Frame(top,bg='cyan3')
    fees_voucher_frame = Frame(top,bg='cyan3')

    for frame in (main_menu,student_data_frame, teacher_data_frame,fees_voucher_frame):
        frame.place(x=0,y=0, width=top.winfo_screenwidth(),height=top.winfo_screenheight())
        
        
    top.photo1=PhotoImage(file="main image.png")
    lb1 = Label(main_menu,image=top.photo1)
    lb1.place(x=0,y=0)

    studentbutton =Button(main_menu,text='Student Data',bg='cyan3',font=('Times new roman', 30),command=lambda:show_frame(student_data_frame))
    studentbutton.place(x=550,y=100,width=250)

    teacherbutton =Button(main_menu,text= 'TeacherData',bg='cyan3',font=('Times new roman', 30),command=lambda: show_frame(teacher_data_frame))
    teacherbutton.place(x=550,y=230,width=250)

    exitbutton =Button(main_menu,text='Exit',bg='cyan3',font=('Times new roman', 30),command=top.destroy)
    exitbutton.place(x=550,y=490,width=250)

    feesvoucher =Button(main_menu,text='Fees Voucher',bg='cyan3',font=('Times new roman', 30),command=lambda:show_frame(fees_voucher_frame))
    feesvoucher.place(x=550,y=360,width=250)

    
    #data Frame
    student_label = Label(student_data_frame, text="Student Data Section",font=('Times new roman',30,'italic'),fg='#0020B0', bg='#FFB853')
    student_label.place(x=550,y=50,width=350)

    # Create the frame
    new_frame = Frame(student_data_frame, bg='white')
    new_frame.place(x=700, y=120, height=500, width=550)

    # Add a label inside the frame with text
    label_in_frame = Label(new_frame, text="Select an option",font=('Times new roman',50),fg='yellow',bg='white')
    label_in_frame.place(x=50, y=200)

    #create print frame
    print_frame = Frame(student_data_frame)
    print_frame.place(x=700,y=170,height=400,width=550)
    print_frame.place_forget()

    #function for print
    def print_student():
       print_frame.place(x=700,y=170,height=400,width=550)
       add_student_form.place_forget()
       remove_student_form.place_forget()

       #clear previous data
       for widget in print_frame.winfo_children():
          widget.destroy()
       #add heading on top
       heading_label=Label(print_frame,text="Student List",font=('Times new roman',20,'bold'),fg='Dark blue',bg='#FFFF00')
       heading_label.pack(pady=10,ipadx=180)

       #create a scrollbar
       canvas=Canvas(print_frame,bg='white')
       scrollbar=Scrollbar(print_frame,orient=VERTICAL,command=canvas.yview)
       scrollable_frame=Frame(canvas,bg='white')

       scrollable_frame.bind(
           "<Configure>",
           lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
       canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
       canvas.configure(yscrollcommand=scrollbar.set)

       #pack the canvas
       canvas.pack(side=LEFT,fill=BOTH,expand=True)
       scrollbar.pack(side=RIGHT,fill=Y)

       #add column headers
       headers=["Name","Father's Name","Age","Class","Roll No"]
       for col, header in enumerate(headers):
          label=Label(scrollable_frame,text=header,font=('times new roman',14,'bold'),bg='white',anchor='w',padx=5,pady=5)
          label.grid(row=0,column=col,padx=10,pady=5,sticky='w')

       #add student data inside
       if len(student_manager.student)==0:
          no_data_label=Label(scrollable_frame,text="No Student Found.",bg='white',font=('Times new roman',16))
          no_data_label.grid(row=1,column=0,columnspan=5,pady=10)
       else:
          for idx, student in enumerate(student_manager.student,start=1):
             student_data=[
                student.name,
                student.father_name,
                student.age,
                student.class_name,
                student.roll_no]

             for col,item in enumerate(student_data):
                data_label=Label(scrollable_frame,text=item,font=('Arial',14),
                                 bg='white',anchor='w',padx=5,pady=5)
                data_label.grid(row=idx,column=col,padx=10,pady=6,sticky='w')

    #function to hide buttons after back
    def stu_hide_button():
       add_student_form.place_forget()
       remove_student_form.place_forget()
       print_frame.place_forget()
       label_in_frame.place(x=50, y=200)
                

    #student data frame
    add_student_form= Frame(student_data_frame, bg='cyan')
    add_student_form.place(x=700,y=170,height=400,width=550)
    add_student_form.place_forget()

    #add student data form
    add_student_detail= Label(add_student_form,text="Add Student's Details",font=('Times new roman',18,'bold'),fg='Dark blue',bg='#FFFF00')
    add_student_detail.place(x=10,y=20,width=530)
    
    add_student_name= Label(add_student_form,text="Student Name:",font=('Times new roman',15),bg='white')
    add_student_name.place(x=30,y=90,width=150)
    entry_student_name= Entry(add_student_form,font=('Arieal',15))
    entry_student_name.place(x=230,y=90)

    add_student_father= Label(add_student_form,text="Father Name:",font=('Times new roman',15),bg='white')
    add_student_father.place(x=30,y=140,width=150)
    entry_student_father= Entry(add_student_form,font=('Arieal',15))
    entry_student_father.place(x=230,y=140)

    add_student_age= Label(add_student_form,text="Student Age:",font=('Times new roman',15),bg='white')
    add_student_age.place(x=30,y=190,width=150)
    entry_student_age= Entry(add_student_form,font=('Arieal',15))
    entry_student_age.place(x=230,y=190)

    add_student_class= Label(add_student_form,text="Student class:",font=('Times new roman',15),bg='white')
    add_student_class.place(x=30,y=240,width=150)
    entry_student_class= Entry(add_student_form,font=('Arieal',15))
    entry_student_class.place(x=230,y=240)

    add_student_rollno= Label(add_student_form,text="Student Roll No:",font=('Times new roman',15),bg='white')
    add_student_rollno.place(x=30,y=290,width=150)
    entry_student_rollno= Entry(add_student_form,font=('Arieal',15))
    entry_student_rollno.place(x=230,y=290)

    #remove student data frame
    remove_student_form= Frame(student_data_frame, bg='cyan')
    remove_student_form.place(x=700,y=170,height=400,width=550)
    remove_student_form.place_forget()

    #remove student data form
    remove_student_detail= Label(remove_student_form,text="Remove Student Details",font=('Times new roman',18,'bold'),fg='Dark blue',bg='#FFFF00')
    remove_student_detail.place(x=10,y=20,width=530)
    
    remove_student_name= Label(remove_student_form,text="Student Name:",font=('Times new roman',15),bg='white')
    remove_student_name.place(x=30,y=90,width=150)
    entry_student_name_re= Entry(remove_student_form,font=('Arieal',15))
    entry_student_name_re.place(x=230,y=90)

    remove_student_rollno= Label(remove_student_form,text="Student Roll No:",font=('Times new roman',15),bg='white')
    remove_student_rollno.place(x=30,y=140,width=150)
    entry_student_rollno_re= Entry(remove_student_form,font=('Arieal',15))
    entry_student_rollno_re.place(x=230,y=140)

    #show frame of student data
    def show_student_form1():
        add_student_form.place(x=700,y=170,height=400,width=550)
        remove_student_form.place_forget()

    #show frame of remove student data
    def show_student_form2():
        remove_student_form.place(x=700,y=170,height=400,width=550)
        add_student_form.place_forget()

    student_manager= StudentManager()

    def add_student():
        name = entry_student_name.get()
        father_name = entry_student_father.get()
        age = entry_student_age.get()
        class_name = entry_student_class.get()
        roll_no = entry_student_rollno.get()

        new_student= student(name,father_name,age,class_name,roll_no)
        student_manager.add_student(new_student)
        messagebox.showinfo("Success", "Student added successfuly!")

        entry_student_name.delete(0, END)
        entry_student_father.delete(0, END)
        entry_student_age.delete(0, END)
        entry_student_class.delete(0, END)
        entry_student_rollno.delete(0, END)

            

    def remove_student():
        name = entry_student_name_re.get()
        roll_no = entry_student_rollno_re.get()

        if student_manager.remove_student(name,roll_no):
               messagebox.showinfo("success", "Student removed successfully!")

        else:
               messagebox.showerror("Error","Student not found!")

        entry_student_name_re.delete(0, END)
        entry_student_rollno_re.delete(0, END)

   #student submit button
    student_submit=Button(add_student_form,text="Submit",font=('Times new roman',20),bg='white',command=add_student)
    student_submit.place(x=295,y=330)

    #student remove button
    student_remove=Button(remove_student_form,text="Submit",font=('Times new roman',20),bg='white',command=remove_student)
    student_remove.place(x=295,y=330)

    
    

    #add students buttons
    add_student_button = Button(student_data_frame,text="Add Student",font=('Times new roman',30),bg='cyan4',command= show_student_form1)
    add_student_button.place(x=100,y=150,width=350)

    remove_student_button = Button(student_data_frame,text="Remove Student",font=('Times new roman',30),bg='cyan4',command= show_student_form2)
    remove_student_button.place(x=100,y=250,width=350)

    print_student_button = Button(student_data_frame,text="Student Details",font=('Times new roman',30),bg='cyan4',command=print_student)
    print_student_button.place(x=100,y=350,width=350)

    student_back_button = Button(student_data_frame,text="Back to Main Menu",font=('Times new roman',30),bg='cyan4', command=lambda:(stu_hide_button(),show_frame(main_menu)))
    student_back_button.place(x=100,y=450,width=350)

    # Create teacher frame
    new_frame2 = Frame(teacher_data_frame, bg='white')
    new_frame2.place(x=700, y=120, height=500, width=550)

    #data Frame
    teacher_label = Label(teacher_data_frame, text="Teacher Data Section",font=('Times new roman',30,'italic'),fg='#0020B0', bg='#FFB853')
    teacher_label.place(x=550,y=50,width=350)

    # Add a label inside the frame with text
    label_in_frame2 = Label(new_frame2, text="Select an option",font=('Times new roman',50),fg='yellow',bg='white')
    label_in_frame2.place(x=50, y=200)

    #create teacher print frame
    print_frame2 =Frame(teacher_data_frame)
    print_frame2.place(x=700,y=170,height=400,width=550)
    print_frame2.place_forget()

    #function for print
    def print_teacher():
       print_frame2.place(x=700,y=170,height=400,width=550)
       add_teacher_form.place_forget()
       remove_teacher_form.place_forget()

       #clear previous data
       for widget in print_frame2.winfo_children():
          widget.destroy()
       #heading on top
       heading_label2=Label(print_frame2,text="Teacher List",font=('Times new roman',20,'bold'),fg='dark blue',bg='#FFFF00')
       heading_label2.pack(pady=10,ipadx=180)

       #create scrollbar
       canvas2=Canvas(print_frame2,bg='white')
       scrollbar2=Scrollbar(print_frame2,orient=VERTICAL,command=canvas2.yview)
       scrollable_frame2=Frame(canvas2,bg='white')

       scrollable_frame2.bind(
          "<Configure>",
          lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
       canvas2.create_window((0,0),window=scrollable_frame2,anchor='nw')
       canvas2.configure(yscrollcommand=scrollbar2.set)
       canvas2.pack(side=LEFT,fill=BOTH,expand=True)
       scrollbar2.pack(side=RIGHT,fill=Y)

       #add column header
       headers2=["Name   ","Address       ","Contact    ","Salary","Class"]
       for col,header in enumerate(headers2):
          label2=Label(scrollable_frame2,text=header,font=('Times new roman',14,
                                                         'bold'),bg='white',
                      anchor='w',padx=5,pady=5)
          label2.grid(row=0,column=col,padx=10,pady=5,sticky='w')

       #add teacher data inside
       if len(teacher_manager.teacher)==0:
          no_data_label2=Label(scrollable_frame2,text="No Teacher Found.",
                               bg='white',font=('Times new roman',16))
          no_data_label2.grid(row=1,column=0,columnspan=5,pady=10)
       else:
          for idx,teacher in enumerate(teacher_manager.teacher,start=1):
             teacher_data=[
                teacher.name,
                teacher.address,
                teacher.contact,
                teacher.salary,
                teacher.class_name]
             for col,item in enumerate(teacher_data):
                data_label2=Label(scrollable_frame2,text=item,font=('Arial',14),
                                  bg='white',anchor='w',padx=5,pady=5)
                data_label2.grid(row=idx,column=col,padx=10,pady=6,sticky='w')

    #function to hide buttons after back
    def tea_hide_button():
       add_teacher_form.place_forget()
       remove_teacher_form.place_forget()
       print_frame2.place_forget()
       label_in_frame2.place(x=50, y=200)
       
          
    
       
    

    #add teacher data form
    add_teacher_form= Frame(teacher_data_frame, bg='cyan')
    add_teacher_form.place(x=700,y=170,height=400,width=550)
    add_teacher_form.place_forget()
   
    add_teacher_detail= Label(add_teacher_form,text="Add Teacher's Details",font=('Times new roman',18,'bold'),fg='Dark blue',bg='#FFFF00')
    add_teacher_detail.place(x=10,y=20,width=530)

    add_teacher_name= Label(add_teacher_form,text="Teacher Name:",font=('Times new roman',15),bg='white')
    add_teacher_name.place(x=30,y=90,width=200)

    entry_teacher_name= Entry(add_teacher_form,font=('Arieal',15))
    entry_teacher_name.place(x=260,y=90)

    add_teacher_address= Label(add_teacher_form,text="Teacher Address:",font=('Times new roman',15),bg='white')
    add_teacher_address.place(x=30,y=140,width=200)

    entry_teacher_address= Entry(add_teacher_form,font=('Arieal',15))
    entry_teacher_address.place(x=260,y=140)

    add_teacher_contact= Label(add_teacher_form,text="Teacher Contact No:",font=('Times new roman',15),bg='white')
    add_teacher_contact.place(x=30,y=190,width=200)

    entry_teacher_contact= Entry(add_teacher_form,font=('Arieal',15))
    entry_teacher_contact.place(x=260,y=190)

    add_teacher_salary= Label(add_teacher_form,text="Teacher Salary:",font=('Times new roman',15),bg='white')
    add_teacher_salary.place(x=30,y=240,width=200)

    entry_teacher_salary= Entry(add_teacher_form,font=('Arieal',15))
    entry_teacher_salary.place(x=260,y=240)

    add_teacher_class= Label(add_teacher_form,text="Assign class:",font=('Times new roman',15),bg='white')
    add_teacher_class.place(x=30,y=290,width=200)

    entry_teacher_class= Entry(add_teacher_form,font=('Arieal',15))
    entry_teacher_class.place(x=260,y=290)

    #remove teacher data form
    remove_teacher_form= Frame(teacher_data_frame, bg='cyan')
    remove_teacher_form.place(x=700,y=170,height=400,width=550)
    remove_teacher_form.place_forget()

    remove_teacher_detail= Label(remove_teacher_form,text="Remove Teacher's Details",font=('Times new roman',18,'bold'),fg='Dark blue',bg='#FFFF00')
    remove_teacher_detail.place(x=10,y=20,width=530)

    remove_teacher_name= Label(remove_teacher_form,text="Teacher Name:",font=('Times new roman',15),bg='white')
    remove_teacher_name.place(x=30,y=90,width=150)
    entry_teacher_name_remove= Entry(remove_teacher_form,font=('Arieal',15))
    entry_teacher_name_remove.place(x=230,y=90)

    remove_teacher_class= Label(remove_teacher_form,text="Teacher's Class:",font=('Times new roman',15),bg='white')
    remove_teacher_class.place(x=30,y=140,width=150)
    entry_teacher_class_remove=Entry(remove_teacher_form,font=('Arieal',15))
    entry_teacher_class_remove.place(x=230,y=140)

    
    #show teacher frame
    def show_teacher_form1():
       add_teacher_form.place(x=700,y=170,height=400,width=550)
       remove_teacher_form.place_forget()
       print_frame2.place_forget()

   #show frame of remove teacher data
    def show_teacher_form2():
        remove_teacher_form.place(x=700,y=170,height=400,width=550)
        add_teacher_form.place_forget()
        print_frame2.place_forget()

    teacher_manager= teacherManager()

    def add_teacher():
       name =entry_teacher_name.get()
       address =entry_teacher_address.get()
       contact =entry_teacher_contact.get()
       salary =entry_teacher_salary.get()
       class_name =entry_teacher_class.get()

       new_teacher= teacher(name,address,contact,salary,class_name)
       teacher_manager.add_teacher(new_teacher)
       messagebox.showinfo("Success","Teacher added successfuly!")

       entry_teacher_name.delete(0,END)
       entry_teacher_address.delete(0,END)
       entry_teacher_contact.delete(0,END)
       entry_teacher_salary.delete(0,END)
       entry_teacher_class.delete(0,END)

    def remove_teacher():
       name =entry_teacher_name_remove.get()
       class_name =entry_teacher_class_remove.get()

       if teacher_manager.remove_teacher(name,class_name):
          messagebox.showinfo("Success","Teacher Removed successfuly!")
       else:
          messagebox.showerror("Error","Teacher not Found!")

       entry_teacher_name_remove.delete(0,END)
       entry_teacher_class_remove.delete(0,END)




    def fee_voucher():
       generate_frame.place(x=700,y=170,height=450,width=550)
       fees_paid_frame.place_forget()
       
    



# Function to calculate the total and display it
    def calculate_total():
       try:
           # Retrieve values from Entry widgets, convert them to integers
           amount1 = int(entry_amount.get()) if entry_amount.get() else 0
           amount2 = int(entry_amount2.get()) if entry_amount2.get() else 0
           amount3 = int(entry_amount3.get()) if entry_amount3.get() else 0

           # Calculate the total
           total = amount1 + amount2 + amount3
           
           # Display the total in the total_entry widget
           total_entry.delete(0, 'end')  # Clear previous total
           total_entry.insert(0, str(total))  # Insert new total
       except ValueError:
           # Handle case where conversion to int fails (not necessary if you validate input)
           total_entry.delete(0, 'end')
           total_entry.insert(0, "Invalid Input")

    #fees Voucher
    generatevoucher=Button(fees_voucher_frame,text="Generate Fee Voucher",font=('Times new roman',30),bg='cyan4',command=fee_voucher)
    generatevoucher.place(x=100,y=150,width=380)

        # Create the frame
    new_frame3 = Frame(fees_voucher_frame, bg='white')
    new_frame3.place(x=700, y=120, height=500, width=550)

    # Add a label inside the frame with text
    label_in_frame3 = Label(new_frame3, text="Fee Voucher",font=('Times new roman',50),fg='yellow',bg='white')
    label_in_frame3.place(x=50, y=200)

    #create print frame
    generate_frame = Frame(fees_voucher_frame,bg='#FFE5B4')
    generate_frame.place(x=700,y=170,height=450,width=550)
    generate_frame.place_forget()

    feelabel=Label(generate_frame,text="Generate Fee Voucher",font=('Times new roman',20),fg='black',bg='#FFB935')
    feelabel.place(x=150,y=10)

    feename=Label(generate_frame,text="Student Name",font=('Times new roman',15),fg='black',bg='#F0A18A')
    feename.place(x=10,y=60)
    entry_student= Entry(generate_frame,font=('Arieal',15))
    entry_student.place(x=150,y=60,width=100)

    feeroll=Label(generate_frame,text="Student Roll No",font=('Times new roman',15),fg='black',bg='#F0A18A')
    feeroll.place(x=10,y=100)
    entry_roll= Entry(generate_frame,font=('Arieal',15))
    entry_roll.place(x=150,y=100,width=100)

    feedate=Label(generate_frame,text="Date:",font=('Times new roman',15),fg='black',bg='#F0A18A')
    feedate.place(x=330,y=60)
    entry_date= Entry(generate_frame,font=('Arieal',15))
    entry_date.place(x=400,y=60,width=100)

    feerow=Label(generate_frame,text="_____________________________________________________",font=('Times new roman',15),bg='#FFE5B4',fg='black')
    feerow.place(x=10,y=150,width=530)
    feerow2=Label(generate_frame,text="_____________________________________________________",font=('Times new roman',15),bg='#FFE5B4',fg='black')
    feerow2.place(x=10,y=190,width=530)
    header1=Label(generate_frame,text="Fees Details",font=('Times new roman',15),fg='black',bg='#F0A18A')
    header1.place(x=140,y=180)

    header2=Label(generate_frame,text="Amount",font=('Times new roman',15),fg='black',bg='#F0A18A')
    header2.place(x=430,y=180)

    

    entry_month= Entry(generate_frame,font=('Arieal',15))
    entry_month.place(x=50,y=230,width=250)
    entry_month2= Entry(generate_frame,font=('Arieal',15))
    entry_month2.place(x=50,y=270,width=250)
    entry_month3= Entry(generate_frame,font=('Arieal',15))
    entry_month3.place(x=50,y=310,width=250)

    entry_amount= Entry(generate_frame,font=('Arieal',15))
    entry_amount.place(x=400,y=230,width=100)
    entry_amount2= Entry(generate_frame,font=('Arieal',15))
    entry_amount2.place(x=400,y=270,width=100)
    entry_amount3= Entry(generate_frame,font=('Arieal',15))
    entry_amount3.place(x=400,y=310,width=100)

    feerow3=Label(generate_frame,text="_____________________________________________________",font=('Times new roman',15),bg='#FFE5B4',fg='black')
    feerow3.place(x=10,y=340,width=530)

    # Create a button to calculate the total
    calculate_button = Button(generate_frame, text="Calculate Total",bg='#FFB935', command=calculate_total)
    calculate_button.place(x=200, y=370)

   # Create an Entry widget to display the total
    total_entry = Entry(generate_frame, font=('Arial', 15))
    total_entry.place(x=390, y=370, width=130)

    canvas = Canvas(generate_frame, height=220, width=1,bg='black')
    canvas.place(x=350,y=170)

    paid =Button(generate_frame,text="Paid Fees",font=('Times new roman',10),bg='#FFB935')
    paid.place(x=420,y=410)

    fees_paid_frame = Frame(fees_voucher_frame,bg='white')
    fees_paid_frame.place(x=700,y=170,height=450,width=550)
    fees_paid_frame.place_forget()

    def show_paid_fees():
    # Clear the previous frame or create a new frame to display data
       #paid_fees_frame = Frame(fees_voucher_frame, bg='white')
        fees_paid_frame.place(x=700, y=120, height=500, width=550)
        generate_frame.place_forget()

        feerow4=Label(fees_paid_frame,text="_____________________________________________________",font=('Times new roman',15),bg='white',fg='black')
        feerow4.place(x=10,y=170,width=530)
        feerow5=Label(fees_paid_frame,text="_____________________________________________________",font=('Times new roman',15),bg='white',fg='black')
        feerow5.place(x=10,y=210,width=530) 

        # Adding Labels for the Fee Voucher details
        Label(fees_paid_frame, text="Fee Voucher", font=('Times new roman', 30), fg='yellow', bg='white').place(x=150, y=10)
        Label(fees_paid_frame, text="Student Name:", font=('Times new roman', 15), fg='black', bg='white').place(x=10, y=80)
        Label(fees_paid_frame, text=entry_student.get(), font=('Arial', 15), fg='black', bg='white').place(x=150, y=80)

        Label(fees_paid_frame, text="Student Roll No:", font=('Times new roman', 15), fg='black', bg='white').place(x=10, y=120)
        Label(fees_paid_frame, text=entry_roll.get(), font=('Arial', 15), fg='black', bg='white').place(x=150, y=120)

        Label(fees_paid_frame, text="Date:", font=('Times new roman', 15), fg='black', bg='white').place(x=10, y=160)
        Label(fees_paid_frame, text=entry_date.get(), font=('Arial', 15), fg='black', bg='white').place(x=150, y=160)

        # Fee details (Months and Amount)
        Label(fees_paid_frame, text="Fees Details", font=('Times new roman', 15), fg='black', bg='cyan').place(x=50, y=200)
        Label(fees_paid_frame, text="Amount", font=('Times new roman', 15), fg='black', bg='cyan').place(x=350, y=200)

        Label(fees_paid_frame, text=entry_month.get(), font=('Arial', 15), fg='black', bg='white').place(x=50, y=240)
        Label(fees_paid_frame, text=entry_amount.get(), font=('Arial', 15), fg='black', bg='white').place(x=350, y=240)

        Label(fees_paid_frame, text=entry_month2.get(), font=('Arial', 15), fg='black', bg='white').place(x=50, y=280)
        Label(fees_paid_frame, text=entry_amount2.get(), font=('Arial', 15), fg='black', bg='white').place(x=350, y=280)

        Label(fees_paid_frame, text=entry_month3.get(), font=('Arial', 15), fg='black', bg='white').place(x=50, y=320)
        Label(fees_paid_frame, text=entry_amount3.get(), font=('Arial', 15), fg='black', bg='white').place(x=350, y=320)

        # Total Amount
        Label(fees_paid_frame, text="Total:", font=('Times new roman', 15), fg='black', bg='white').place(x=50, y=380)
        Label(fees_paid_frame, text=total_entry.get(), font=('Arial', 15), fg='black', bg='white').place(x=350, y=380)


        feerow6=Label(fees_paid_frame,text="_____________________________________________________",font=('Times new roman',15),bg='white',fg='black')
        feerow6.place(x=10,y=350,width=530)

        canvas2 = Canvas(fees_paid_frame, height=220, width=1,bg='black')
        canvas2.place(x=320,y=190)
   


       
       

    fee_paid=Button(fees_voucher_frame,text="Show Fee Voucher",font=('Times new roman',30),bg='cyan4',command=show_paid_fees)
    fee_paid.place(x=100,y=300,width=380)
        
    #teacher submit button
    teacher_submit=Button(add_teacher_form,text="Submit",font=('Times new roman',20),bg='white',command=add_teacher)
    teacher_submit.place(x=315,y=330)

    teacher_remove=Button(remove_teacher_form,text="Submit",font=('Times new roman',20),bg='white',command=remove_teacher)
    teacher_remove.place(x=300,y=330)
    

    #add teacher buttons
    add_teacher_button = Button(teacher_data_frame,text="Add Teacher",font=('Times new roman',30),bg='cyan4',command= show_teacher_form1)
    add_teacher_button.place(x=100,y=150,width=350)

    remove_teacher_button = Button(teacher_data_frame,text="Remove Teacher",font=('Times new roman',30),bg='cyan4',command= show_teacher_form2)
    remove_teacher_button.place(x=100,y=250,width=350)

    print_teacher_button = Button(teacher_data_frame,text="Teacher Details",font=('Times new roman',30),bg='cyan4',command= print_teacher)
    print_teacher_button.place(x=100,y=350,width=350)


    teacher_back_button = Button(teacher_data_frame,text="Back to Main Menu",font=('Times new roman',30),bg='cyan4', command=lambda:(tea_hide_button(),show_frame(main_menu)))
    teacher_back_button.place(x=100,y=450,width=350)

    fee_back_button = Button(fees_voucher_frame,text="Back to Main Menu",font=('Times new roman',30),bg='cyan4', command=lambda:(tea_hide_button(),show_frame(main_menu)))
    fee_back_button.place(x=100,y=450,width=380)

    #raise the main menu frame
    show_frame(main_menu)

    top.state('zoomed')
    top.mainloop()
    


w.after(3000,new_win)


w.mainloop()
