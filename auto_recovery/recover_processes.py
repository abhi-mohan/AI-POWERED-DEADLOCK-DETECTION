import psutil
import os
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

LOG_FILE = "recovery_log.txt"
CPU_THRESHOLD = 95  # CPU usage percentage considered as unresponsive
MEMORY_THRESHOLD = 500  # MB of memory usage to check for stuck processes
TIME_THRESHOLD = 300  # Process run time in seconds to be considered for checking

def log_message(message):
  """Logs a message to console and file."""
  print(message)
  with open(LOG_FILE, "a") as log:
      log.write(message + "\n")

def detect_and_recover_processes():
  """Detects stalled processes and attempts to restart or terminate them."""
  log_message(Fore.YELLOW + "🔍 Scanning processes for deadlocks...")

  for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info', 'create_time']):
      try:
          cpu_usage = proc.info['cpu_percent']
          memory_usage = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
          runtime = time.time() - proc.info['create_time']

          if cpu_usage > CPU_THRESHOLD and memory_usage > MEMORY_THRESHOLD and runtime > TIME_THRESHOLD:
              log_message(Fore.RED + f"⚠ Potential deadlock detected in process: {proc.info['name']} (PID: {proc.info['pid']})")
              
              # Try to restart the process
              try:
                  proc.terminate()  # Attempt to terminate
                  proc.wait(timeout=5)  # Wait for process to terminate
                  new_proc = psutil.Popen(proc.cmdline())  # Restart
                  log_message(Fore.GREEN + f"✅ Successfully restarted {proc.info['name']} (New PID: {new_proc.pid})")
              except Exception as e:
                  log_message(Fore.RED + f"❌ Failed to restart {proc.info['name']}. Terminating instead.")
                  proc.kill()  # Force terminate if restart fails
          
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
          continue

  log_message(Fore.GREEN + "✅ Auto recovery process completed.")

if __name__ == "__main__":
  detect_and_recover_processes()
