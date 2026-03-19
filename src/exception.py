import sys
from src.logger import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #this will give us the info like on which file the exception has occured on which line no all that info will be stored in this v ariable
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message                                                                                      


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    
    
    
    # def __str__(self):
    #     return self.error_message    
    # __str__ = “print hone pe kya dikhana hai”
    
# abey jab function bna diya toh class kyu bnai 
# Function sirf message banata hai
# 👉 Class us message ko proper exception bana ke raise karti hai

# 🔹 Purpose of exception.py:
# This file is used to create custom error messages with detailed information like file name, line number, and actual error.

# ------------------------------------------------------------

# 🔹 import sys:
# The sys module is used to get system-level information.
# It helps us access details about the exception using sys.exc_info().

# ------------------------------------------------------------

# 🔹 error_message_details function:

# This function creates a detailed error message.

# Steps:
# 1. sys.exc_info() returns:
#    - error type
#    - error object
#    - traceback object

# 2. We extract traceback (exc_tb) to find:
#    - file name → exc_tb.tb_frame.f_code.co_filename
#    - line number → exc_tb.tb_lineno

# 3. We combine everything into a readable message:
#    - file name
#    - line number
#    - actual error

# So this function RETURNS a detailed string message.

# ------------------------------------------------------------

# 🔹 CustomException class:

# This is a custom exception class that extends Python's built-in Exception class.

# class CustomException(Exception):

# Why we use this:
# - To raise errors in a structured way
# - To integrate with Python's exception system
# - To make debugging easier

# ------------------------------------------------------------

# 🔹 super().__init__(error_message):

# This calls the parent class (Exception) constructor.
# It ensures that the default exception behavior works properly.

# ------------------------------------------------------------

# 🔹 self.error_message:

# We store the detailed error message created by the function.

# ------------------------------------------------------------

# 🔹 __str__ method:

# This controls what gets printed when we do:
# print(e)

# Instead of default output, it returns our custom error message.

# ------------------------------------------------------------

# 🔹 Why not just use the function?

# The function only returns a string.
# But the class:
# - creates a real exception object
# - allows us to use "raise"
# - keeps error handling structured

# ------------------------------------------------------------

# 🔹 Example usage:

# try:
#     a = 10 / 0
# except Exception as e:
#     raise CustomException(e, sys)

# Output:
# Error occurred in python script [file_name] line number [line_no] error message [division by zero]

# ------------------------------------------------------------

# 🔹 Final Summary:

# Function → creates detailed error message  
# Class → converts that message into a proper exception  

# Both together → powerful error handling system




# 🔹 Overall Flow of Custom Exception Handling

# This system converts a normal Python error into a detailed, structured error message
# that includes file name, line number, and the actual error.

# ------------------------------------------------------------

# 🔹 Step 1: Error Occurs

# Example:
# try:
#     a = 10 / 0

# This creates a ZeroDivisionError.

# ------------------------------------------------------------

# 🔹 Step 2: Error is Caught

# except Exception as e:

# - 'e' stores the original error (e.g., division by zero)

# ------------------------------------------------------------

# 🔹 Step 3: Custom Exception is Raised

# raise CustomException(e, sys)

# - Instead of handling the error normally, we pass it to our custom class
# - This helps us generate a more detailed and useful error

# ------------------------------------------------------------

# 🔹 Step 4: __init__ Method Executes

# CustomException object is created.

# Inputs:
# - error_message → original error (e)
# - error_detail → sys module

# ------------------------------------------------------------

# 🔹 Step 5: super().__init__(error_message)

# - Calls parent (Exception) constructor
# - Ensures default exception behavior is preserved
# - Stores basic error message internally

# ------------------------------------------------------------

# 🔹 Step 6: Call to error_message_details()

# self.error_message = error_message_details(error_message, error_detail)

# - This function generates a detailed error message

# ------------------------------------------------------------

# 🔹 Step 7: Inside error_message_details()

# 1. sys.exc_info() is used:
#    - Returns (type, value, traceback)

# 2. Extract traceback:
#    _, _, exc_tb = sys.exc_info()

# 3. Get file name:
#    exc_tb.tb_frame.f_code.co_filename

# 4. Get line number:
#    exc_tb.tb_lineno

# 5. Combine everything:
#    - file name
#    - line number
#    - actual error

# Example Output:
# "Error occurred in script [main.py] at line [10] error message [division by zero]"

# ------------------------------------------------------------

# 🔹 Step 8: Store Final Message

# self.error_message now contains the detailed error string

# ------------------------------------------------------------

# 🔹 Step 9: Printing the Error

# print(e)

# - Python internally calls:
#   e.__str__()

# ------------------------------------------------------------

# 🔹 Step 10: __str__ Method Executes

# def __str__(self):
#     return self.error_message

# - Returns the custom error message instead of default output

# ------------------------------------------------------------

# 🔹 Final Output

# Error occurred in script [file_name] line number [line_no] error message [actual error]

# ------------------------------------------------------------

# 🔹 Key Concepts Summary

# - try/except → catches error
# - CustomException → wraps error
# - super() → keeps default behavior
# - sys.exc_info() → gives traceback info
# - function → builds detailed message
# - __str__ → controls print output

# ------------------------------------------------------------

# 🔹 Final Understanding

# Normal Error → Captured → Enhanced with details → Raised as Custom Exception → Clean output

# ------------------------------------------------------------

# 🔹 One-Line Summary

# We convert a basic error into a detailed, production-ready error message using OOP and system traceback.