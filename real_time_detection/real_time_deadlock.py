import psutil
import time

def detect_deadlock():
    print("🔍 Monitoring system processes for potential deadlocks...")

    while True:
        processes = [p.info for p in psutil.process_iter(['pid', 'name', 'status'])]

        # Simulate deadlock detection logic (Example: If too many processes are 'stuck')
        stuck_processes = [p for p in processes if p['status'] == 'stopped']

        if len(stuck_processes) > 3:
            print("⚠️ Deadlock Detected! Resolving...")
            # Resolve by terminating a low-priority process (Example: Terminate the first stuck process)
            psutil.Process(stuck_processes[0]['pid']).terminate()
            print(f"✅ Process {stuck_processes[0]['name']} (PID: {stuck_processes[0]['pid']}) terminated to resolve deadlock.")

        else:
            print("✔ No Deadlock Detected.")

        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    detect_deadlock()
