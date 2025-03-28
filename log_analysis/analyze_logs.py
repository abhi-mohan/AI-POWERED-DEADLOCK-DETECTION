import os
import re
import pandas as pd
import psutil
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

LOG_DIR = "logs"
OUTPUT_REPORT = "log_report.txt"

ERROR_PATTERNS = {
  "deadlock": r"deadlock detected",
  "memory leak": r"out of memory|memory exceeded",
  "cpu overload": r"cpu usage high|cpu exceeded",
  "file error": r"file not found|permission denied",
}

def analyze_logs():
  report = []
  
  if not os.path.exists(LOG_DIR):
      os.makedirs(LOG_DIR)

  log_files = [f for f in os.listdir(LOG_DIR) if f.endswith(".log") or f.endswith(".txt")]
  
  if not log_files:
      print(Fore.RED + "❌ No log files found in the 'logs/' directory!")
      return
  
  print(Fore.YELLOW + f"🔍 Scanning {len(log_files)} log files...")

  for log_file in log_files:
      with open(os.path.join(LOG_DIR, log_file), "r") as f:
          lines = f.readlines()

      for line in lines:
          for issue, pattern in ERROR_PATTERNS.items():
              if re.search(pattern, line, re.IGNORECASE):
                  log_entry = f"[{issue.upper()}] in {log_file}: {line.strip()}"
                  report.append(log_entry)
                  print(Fore.RED + "⚠ " + log_entry)

  if report:
      with open(OUTPUT_REPORT, "w") as f:
          f.write("\n".join(report))
      print(Fore.GREEN + f"✅ Analysis complete! Report saved as '{OUTPUT_REPORT}'")
  else:
      print(Fore.GREEN + "✅ No critical issues found in logs.")

if __name__ == "__main__":
  analyze_logs()
