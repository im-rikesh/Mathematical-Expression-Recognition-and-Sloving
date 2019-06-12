#A major Project on MATHEMATICAL EXPRESSION RECOGNITION AND SOLVING

from tkinter import *
from PIL import Image
import pytesseract
import re
import math
import numpy as np  
import matplotlib.pyplot as plt


#MAIN
window = Tk()
window.title("Home : Mathematical Expression Recognition and Solving")
window.configure(background = "light blue")

#Photo
photo1=PhotoImage(file="group.gif")
Label (window, image=photo1, bg="light blue") .grid(row=0, column=0, sticky=N)

#Create Label
Label (window, text=">>> TECH MINER <<<", bg="light blue", fg="black",font="none 56 bold") .grid(row=4, column=0, sticky=S)

#Exit Function
def close_window():
    window.destroy()
    exit()

#Create a Exit button
Button(window, text="Exit", width=34, command=close_window) .grid(row=7, column=0, sticky=E)


##################################        ---->>>>                  WINDOW -2            <<<<----                     ##########################################################


def window2(): # new window definition
    newwin = Toplevel(window)
    newwin.title("Select Image : Mathematical Expression Recognition and Solving")
    Label (newwin, text="For Mathematical Result:", fg="gray",font="none 12") .grid(row=1, column=0, sticky=W) #we put  bg="gray", ahead of 'fg'
    Label (newwin, text="Please write the image name.        ", fg="gray",font="none 12") .grid(row=2, column=0, sticky=W) #we put bg="gray", ahead of 'fg'

    Label (newwin, text="To plot the graph of any equation (in the form 'y = m*x+c') : ", fg="gray",font="none 12") .grid(row=1, column=1, sticky=W) #we put  bg="gray", ahead of 'fg'
    Label (newwin, text="Please write the image name.", fg="gray",font="none 12") .grid(row=2, column=1, sticky=W) #we put bg="gray", ahead of 'fg'

    Label (newwin, text="To find the value of x in any equation (k1*x+k2=k3): ", fg="gray",font="none 12") .grid(row=1, column=2, sticky=W) #we put  bg="gray", ahead of 'fg'
    Label (newwin, text="Please write the image name.", fg="gray",font="none 12") .grid(row=2, column=2, sticky=W) #we put bg="gray", ahead of 'fg'

    Label (newwin, text="For Logarathmic Result:", fg="gray",font="none 12") .grid(row=1, column=3, sticky=W) #we put  bg="gray", ahead of 'fg'
    Label (newwin, text="Please write the image name.", fg="gray",font="none 12") .grid(row=2, column=3, sticky=W) #we put bg="gray", ahead of 'fg'


#########################################    ---->>>>    FOR MATHEMATICAL EXPRESSION     <<<<----              #######################################################


    #Create a text entry box for mathematical expression
    textentry =Entry(newwin, width=20, bg="white")
    textentry.grid(row=3, column=0, sticky=W)
    

    #Click Function for submit button 1
    def click():
        entered_text = textentry.get() #collects the text written in text box
        output.delete(0.0,END)
        
        im = Image.open(entered_text)
        text = pytesseract.image_to_string(im, lang = 'eng')

        
        output.insert(END,'The expression in the image is : ')
        output.insert(END,text)
        output.insert(END,'\n')
        output.insert(END,'\n')
        output.insert(END,'Solution \n')
        output.insert(END,'\n')


        count = 1

        def solver(op=None):
            
            
            op = op.replace(',','.')
            op = op.replace('^','**')
            op = op.replace('{', '(') 
            op = op.replace('}', ')')
            op = op.replace('[', '(')
            op = op.replace(']', ')')

            pattern = r'(\d+\(|\)\(|\)\d+)'
            i = 0
            for match in re.finditer(pattern, op):
                end = match.end()-1+i
                op = op[:end]+'*'+op[end:]
                i+=1
                
            i = 1

            #Integrity check

            try:
                eval(op)
            except:
                print('Error. Check the expression.\n')
                output.insert(END,'Error. Check the expression.\n')
            else:
            
                while op.count('(') > 0:

                    pre = op.split(')')[0]
                    calc = pre.split('(')[-1]
                    res = str(eval(calc))
                    op = op.replace('('+calc+')', res)

                    
                    print(f'Step {i} : ',op)
                    output.insert(END, f'Step {i} : ')
                    output.insert(END, op)
                    output.insert(END, '\n')
                    i+=1
                
                print('Result : ',eval(op))
                output.insert(END, 'Result : ')
                output.insert(END, eval(op))
                output.insert(END, '\n')



                
        while count == 1 :

            count = count + 1
            
            inp = text
            if inp.count('(') != inp.count(')'):
                 print('Parenthesis error, check the expression.\n')
                 output.insert(END, 'Parenthesis error, check the expression.\n')
            else:
                solver(inp)

        
        

    #Create a Submit button
    Button(newwin, text="Submit", width=12, command=click) .grid(row=4, column=0, sticky=W)

    Label (newwin, text="The output of the image selected above is: ", fg="gray",font="none 12") .grid(row=5, column=1, sticky=W) #we put  bg="gray", ahead of 'fg'

########################################         ---->>>>       END OF MATHEMATICAL EXPRESSION        <<<<----         #######################################
    


########################################         ---->>>>    PLOTTING GRAPH        <<<<----         #######################################


    #Create a text entry box for graph
    textentry2 =Entry(newwin, width=20, bg="white")
    textentry2.grid(row=3, column=1, sticky=W)


    #Click Function for submit button 1
    def click2():
        entered_text2 = textentry2.get() #collects the text written in text box
        output.delete(0.0,END)

        im2 = Image.open(entered_text2)
        text2 = pytesseract.image_to_string(im2, lang = 'eng')

        output.insert(END,'The expression in the image is : ')
        output.insert(END,'y = ')
        output.insert(END,text2)
        output.insert(END,'\n')
        output.insert(END,'\n')
        output.insert(END,'Graph of the above equation is shown now : \n')
        output.insert(END,'\n')

        x = np.linspace(-5,5,100)
        y = eval(text2)
        plt.plot(x, y, '-r', label='y = '+text2)
        plt.title('Grapyh of: y = '+text2)
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()


    #Create a Submit button
    Button(newwin, text="Submit", width=12, command=click2) .grid(row=4, column=1, sticky=W)


########################################         ---->>>>       END OF PLOTTING GRAPH        <<<<----         #######################################



########################################         ---->>>>       FINDING THE VALUE OF 'X'        <<<<----         #######################################


    #Create a text entry box for finding the value of 'x'
    textentry3 =Entry(newwin, width=20, bg="white")
    textentry3.grid(row=3, column=2, sticky=W)


    def click3():

        entered_text3 = textentry3.get() #collects the text written in text box
        output.delete(0.0,END)
        
        im = Image.open(entered_text3)
        text3 = pytesseract.image_to_string(im, lang = 'eng')

        
        output.insert(END,'The expression in the image is : ')
        output.insert(END,text3)
        output.insert(END,'\n')
        output.insert(END,'\n')
        output.insert(END,'Solution \n')
        output.insert(END,'\n')

        exp=text3

        def solve_linear_equation1 (m, c, y):
            #match = re.match(r"(\d+)x\-(\d+)=(\d+)", equ)
            #m, c, y = match1.groups()
            #m, c, y = float(m), float(c), float(y) # Convert from strings to numbers
            x = (y+c)/m
            output.insert(END,'x = ')
            output.insert(END,x)


        match1 = re.match(r"(\d+)x\+(\d+)=(\d+)", exp)
        match2 = re.match(r"(\d+)x\+(\d+)=-(\d+)", exp)
        match3 = re.match(r"(\d+)x\-(\d+)=(\d+)", exp)
        match4 = re.match(r"(\d+)x\-(\d+)=-(\d+)", exp)
        match5 = re.match(r"-(\d+)x\+(\d+)=+(\d+)", exp)
        match6 = re.match(r"-(\d+)x\+(\d+)=-(\d+)", exp)
        match7 = re.match(r"-(\d+)x\-(\d+)=(\d+)", exp)
        match8 = re.match(r"-(\d+)x\-(\d+)=-(\d+)", exp)
        match9 = re.match(r"x\+(\d+)=(\d+)", exp)

        try:
            m, c, y = match1.groups()
            m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

        except:

            try:
                m, c, y = match2.groups()
                m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

            except:

                try:
                    m, c, y = match3.groups()
                    m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                except:

                    try:
                        m, c, y = match4.groups()
                        m, c, y = float(m), float(c), float(y) # Convert from strings to numbers


                    except:

                        try:
                            m, c, y = match5.groups()
                            m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                        except:

                            try:
                                m, c, y = match6.groups()
                                m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                            except:

                                try:
                                    m, c, y = match7.groups()
                                    m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                                except:

                                    try:
                                        m, c, y = match8.groups()
                                        m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                                    except:
                                        c, y = match9.groups()
                                        m = 1
                                        m, c, y = float(m), float(c), float(y) # Convert from strings to numbers

                                        


                        

        if(match1 != None):
            c = -c
            solve_linear_equation1(m, c, y)

        if(match2 != None):
            c = -c
            y = -y
            solve_linear_equation1(m, c, y)

        if(match3 != None):
            solve_linear_equation1(m, c, y)

        if(match4 != None):
            y = -y
            solve_linear_equation1(m, c, y)

        if(match5 != None):
            c = -c
            m = -m
            solve_linear_equation1(m, c, y)

        if(match6 != None):
            solve_linear_equation1(m, c, y)

        if(match7 != None):
            m = -m
            solve_linear_equation1(m, c, y)

        if(match8 != None):
            y = -y
            m = -m
            solve_linear_equation1(m, c, y)

        if(match9 != None):
            c = -c
            solve_linear_equation1(m, c, y)



    #Create a Submit button
    Button(newwin, text="Submit", width=12, command=click3) .grid(row=4, column=2, sticky=W)


########################################         ---->>>>      END OF FINDING THE VALUE OF 'X'        <<<<----         #######################################



#########################################    ---->>>>    FOR LOGARATHMIC EXPRESSION     <<<<----              #######################################################


    #Create a text entry box for logarathmic expression
    textentry4 =Entry(newwin, width=20, bg="white")
    textentry4.grid(row=3, column=3, sticky=W)

    #Click Function for submit button 1
    def click4():

        entered_text4 = textentry4.get() #collects the text written in text box
        output.delete(0.0,END)
        
        im = Image.open(entered_text4)

        text4 = pytesseract.image_to_string(im, lang = 'eng')

        output.insert(END,'The expression in the image is : ')
        output.insert(END,text4)
        output.insert(END,'\n')
        output.insert(END,'\n')
        output.insert(END,'Solution: \n')
        output.insert(END,'\n')

        text4 = re.sub('Log', '', text4)


        count = 1

        def solver(op=None):
                    
                    
            op = op.replace(',','.')
            op = op.replace('^','**')
            op = op.replace('{', '(') 
            op = op.replace('}', ')')
            op = op.replace('[', '(')
            op = op.replace(']', ')')

            pattern = r'(\d+\(|\)\(|\)\d+)'
            i = 0
            for match in re.finditer(pattern, op):
                end = match.end()-1+i
                op = op[:end]+'*'+op[end:]
                i+=1
                        
            i = 1

            #Integrity check

            try:
                eval(op)
            except:
                print('Error. Check the expression.\n')
                output.insert(END,'Error. Check the expression.\n')
            else:
                    
                while op.count('(') > 0:

                    pre = op.split(')')[0]
                    calc = pre.split('(')[-1]
                    res = str(eval(calc))
                    op = op.replace('('+calc+')', res)

                            
                    print(f'Step {i} : ',op)
                    output.insert(END, f'Step {i} : ')
                    output.insert(END, op)
                    output.insert(END, '\n')
                    i+=1
                    
                result = eval(op)
                        
                print('Result of expression before performing logarathmic function: ',result)
                output.insert(END, 'Result of expression before performing logarathmic function: ')
                output.insert(END, result)
                output.insert(END, '\n')

                print('Final Result: ', math.log10(result))        
                output.insert(END, 'Final Result: ')
                output.insert(END, math.log10(result))



                        
        while count == 1 :

            count = count + 1
                    
            inp = text4
            if inp.count('(') != inp.count(')'):
                    print('Parenthesis error, check the expression.\n')
                    output.insert(END, 'Parenthesis error, check the expression.\n')
            else:
                solver(inp)


    #Create a Submit button
    Button(newwin, text="Submit", width=12, command=click4) .grid(row=4, column=3, sticky=W)

           

#########################################    ---->>>>    END OF LOGARATHMIC EXPRESSION     <<<<----              #######################################################




########################################         ---->>>>       OUTPUT BOX        <<<<----         #######################################


    #Create a output text box
    output = Text(newwin, width=93, height=16, wrap=WORD, background='white')
    output.grid(row=6, column=1, columnspan=2, sticky=W)

########################################         ---->>>>    END OF OUTPUT BOX        <<<<----         #######################################


    #Exit Function
    def close_newwin():
        newwin.destroy()

    #Create a newwin Exit button
    Button(newwin, text="Exit", width=12, command=close_newwin) .grid(row=7, column=1, sticky=E)
    

################################################################                END OF WINDOW - 2                    ########################################################


#Create a Next button
Button(window, text="Next", width=32, command=window2) .grid(row=7, column=0, sticky=W)

#run the main loop
window.mainloop()
 
