import time

# List of processes
processes = ["P0", "P1", "P2"]

# Function to simulate a process running
def run_process(process_name):
    print(f"{process_name} running")
    time.sleep(1)  # Simulate some work being done
    print(f"{process_name} waiting")

# Function to simulate a process termination

def halt_process(process_name):
    print(f"{process_name} paused")
    
def terminate_process(process_name):
    print(f"{process_name} done")

# Simulate the scheduling and execution of processes
while processes:
    current_process = processes.pop(0)
    run_process(current_process)
    halt_process(current_process)
    terminate_process(current_process)
    
    


print("All processes are done!")

