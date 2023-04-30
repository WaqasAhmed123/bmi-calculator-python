import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")

#def function
def calculate_bmi():
    Height = float(entry_Height.get())
    Weight = float(entry_Weight.get())
    Height = Height/100
    BMI = Weight/(Height**2)
    BMI = round(BMI,2)
    if (BMI>0):
        if (BMI<=16):
            print("Your BMI is is:",BMI,"You are severely underweight.")
        elif (BMI <=18.5):
                print("Your BMI is is:",BMI,"You are underweight.")

        elif(BMI<=25):
                    print("Your BMI is is:",BMI,"You are healthy.")
        elif(BMI<=30):
                        print("Your BMI is is:",BMI,"You are overeweight.")
        else:print("You are severely overweight.")   
    else: print("Enter valid datails.")     
    Label_result ['text'] = f"BMI: {BMI}"


# create gui
Label_Height = tkinter.Label(root, text="Height:")
Label_Height.grid(column=0, row=0)

entry_Height = tkinter.Entry(root)
entry_Height.grid(column=1, row=0)

Label_Weight = tkinter.Label(root, text="Weight")
Label_Weight.grid(column=0, row=1)

entry_Weight = tkinter.Entry(root)
entry_Weight.grid(column=1, row=1)

button_Calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_Calculate.grid(column=0, row=2)

Label_result = tkinter.Label(root, text="BMI:")
Label_result.grid(column=1, row=2)

root.mainloop()
