# Quesion 4
Float_No = float (input("enter your floatng No: "))
Interger_part,_,Fractional_part=(str(Float_No)).partition('.')

print("you entered: ",Float_No)
print("The integer part is : ",Interger_part)
print("The fractional part is : ",Fractional_part)
