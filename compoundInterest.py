def print_math_compound_interest(principle, rate, time):
   totalAmount=principle*(1+(rate/100))**time
   print("Compound Interest: "+ str(round(totalAmount-principle,2)))

def collect_inputs_and_convert_to_float():    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
 client_principal = float(input("Principle (amount): "))
 client_time =      float(input("Time:               "))
 client_rate =      float(input("Rate:               "))

 return client_principal, client_time, client_rate
 #print("Compound Interest: "+str(intrest))
def calculateCompoundInterest():
   line_break = "---"

   client_principal_1, client_time_1, client_rate_1=collect_inputs_and_convert_to_float()
   print_math_compound_interest(client_principal_1,client_rate_1,client_time_1)
   print (line_break)

   client_principal_2, client_time_2, client_rate_2=collect_inputs_and_convert_to_float()
   print_math_compound_interest(client_principal_2,client_rate_2,client_time_2)
   print (line_break)

   client_principal_3,client_time_3, client_rate_3=collect_inputs_and_convert_to_float()
   print_math_compound_interest(client_principal_3,client_rate_3,client_time_3)
    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
