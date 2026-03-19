import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s ",
    level=logging.INFO,


)

if __name__=="__main__":
    logging.info("logging has started")





#     🔹 Purpose of logger.py:
# Used to store logs (messages, errors, events) in a file instead of printing on console.

# ------------------------------------------------------------

# 🔹 Logging vs Print:
# print() → console output  
# logging → file + structured output (production use)

# ------------------------------------------------------------

# 🔹 Steps:

# 1. Create log file name using datetime
#    → ensures unique file every run

# 2. Create logs folder using os.makedirs()
#    → stores all log files in one place

# 3. Define full file path
#    → combine folder + file name

# 4. Configure logging using logging.basicConfig()

# ------------------------------------------------------------

# 🔹 Important parameters:

# filename → where logs are stored  
# format → structure of log message  
# level → minimum level to log (INFO, ERROR)

# ------------------------------------------------------------

# 🔹 Format explanation:

# %(asctime)s → time  
# %(lineno)d → line number  
# %(name)s → module name  
# %(levelname)s → log level  
# %(message)s → actual message  

# ------------------------------------------------------------

# 🔹 Example:

# logging.info("Start")

# Output in file:
# [2026-03-20 19:30:12] 25 root - INFO - Start

# ------------------------------------------------------------

# 🔹 Log Levels:

# INFO → general info  
# WARNING → something unusual  
# ERROR → error occurred  
# CRITICAL → serious error  

# ------------------------------------------------------------

# 🔹 Final Flow:

# Program → logging config → logging call → message saved in file

# ------------------------------------------------------------

# 🔹 One-Line Summary:

# Logger helps track program execution and errors in a structured file for debugging and production use.