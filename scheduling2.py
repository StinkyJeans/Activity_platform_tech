import threading
import time

# Function to simulate process execution
def run_process(process_name):
    for i in range(4):
        print(f"{process_name} -> running state")
        time.sleep(1)
        
        if process_name == "P0" and i == 2:
            print("P0 -> interrupted")
            time.sleep(1)
            print("P0 -> waiting state")
        elif process_name == "P2" and i == 1:
            print("P2 -> interrupted")
            time.sleep(1)
            print("P2 -> waiting state")
        elif process_name == "P1" and i == 3:
            print("P1 -> Done")
            return
        elif process_name == "P0" and i == 3:
            print("P0 -> Done")
            return
        elif process_name == "P2" and i == 3:
            print("P2 -> Done")
            return
        else:
            print(f"{process_name} -> waiting state")

# Create thread objects for each process
p0_thread = threading.Thread(target=run_process, args=("P0",))
p1_thread = threading.Thread(target=run_process, args=("P1",))
p2_thread = threading.Thread(target=run_process, args=("P2",))

# Start the threads
p0_thread.start()
p1_thread.start()
p2_thread.start()

# Wait for all threads to finish
p0_thread.join()
p1_thread.join()
p2_thread.join()

print("All processes are done.")