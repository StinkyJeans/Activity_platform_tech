import time

# List of processes
processes = ["P0", "P1", "P2"]


def run_process(process_name):
    print(f"{process_name} running")
    time.sleep(1)  
    print(f"{process_name} waiting")

def terminate_process(process_name):
    print(f"{process_name} done!")

while processes:
    current_process = processes.pop(0)

    run_process(current_process)

    if current_process == "P0":
        terminate_process(current_process)
    if current_process == "P1":
        terminate_process(current_process)
    if current_process == "P2":
        terminate_process(current_process)

print("All processes are done!")
