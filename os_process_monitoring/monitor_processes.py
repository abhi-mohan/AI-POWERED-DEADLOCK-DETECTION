
import psutil
import time

def monitor_processes():
  print(f"{'PID':<10}{'Process Name':<25}{'CPU %':<10}{'Memory %':<10}{'Execution Time':<15}")
  print("=" * 70)
  
  process_start_time = {}

  try:
      while True:
          for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'create_time']):
              pid = proc.info['pid']
              name = proc.info['name']
              cpu = proc.info['cpu_percent']
              memory = proc.info['memory_percent']
              
              if pid not in process_start_time:
                  process_start_time[pid] = proc.info['create_time']

              start_time = process_start_time[pid]
              elapsed_time = time.time() - start_time

              print(f"{pid:<10}{name:<25}{cpu:<10}{memory:<10}{elapsed_time:.2f} sec")

          print("\nRefreshing in 5 seconds...\n")
          time.sleep(5)
  
  except KeyboardInterrupt:
      print("\n🔴 Process monitoring stopped.")

if __name__ == "__main__":
  monitor_processes()
