import time

# Define the list of processes and their initial states
waitingProcesses = ['P1', 'P2', 'P3']
runningProcesses = []

# Function to change the state of a process
def get_running_state():
    result = ''
    # adds the first process from the waiting list to the running list
    runningProcesses.append(waitingProcesses[0])
    
    # removes the first process in the waiting list
    waitingProcesses.pop(0)
    
    # loops thru all the running process
    for process in runningProcesses:
        result = f"Running => {process}"
   
    print(result)

def get_waiting_state():
    print('Waiting =>')
    print(*waitingProcesses, sep = ", ")
   
    
def halt():
    print (f"{runningProcesses[0]} is paused" )
    # runs running function 
    get_running_state()
    
    # adds the first process from the waiting list to the running list
    waitingProcesses.append(runningProcesses[0])
    
    # removes the first process in the waiting list
    runningProcesses.pop(0)

def terminate():
    print(f"{runningProcesses[0]} ")
    
    # removes the first process in the waiting list
    runningProcesses.pop(0)

# First process is running (P1)
get_running_state()
# Get remaining waiting process (P2, P3)
get_waiting_state()
# Pause the current process running (P1) then make the next process run (P2)
halt()
# Get remaining waiting processes (P3, P1)
get_waiting_state()
# Terminate the current process running (P2)
terminate()
# Run another Process (next process is P3)
get_running_state()
# Get remaining waiting Process (P1)
get_waiting_state()
# Pause the current process running (P3) then make the next process run (P1)
halt()
# Get remaining waiting process (P3)
get_waiting_state()
# Terminate the current process running (P1)
terminate()
# Run the next waiting Process (P3)
get_running_state()
# Terminate the current process running (P3)
terminate()