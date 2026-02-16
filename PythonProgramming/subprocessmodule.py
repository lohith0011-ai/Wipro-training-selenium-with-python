









import subprocess

# subprocess.run() - run command and wait
# subprocess.popen() - run process asynchronously
# subprocess.PIPE - capture the output
# subprocess.CompleteProcess - result
# subprocess.TimeoutExpired - Time out expection
# subproces.CalledProcessError - command failure

result = subprocess.run("dir", shell=True, capture_output=True, text=True)
print(result)

result = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)
print(result)

result = subprocess.run("python-version", shell=True, capture_output=True, text=True)
print(result)
#print(result.stderr)