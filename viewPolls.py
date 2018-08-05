import time
import subprocess
from polls import clearPollsInFile
process_downloader2 = subprocess.Popen("ls -R", shell=True, stdout=subprocess.PIPE)
out2 = process_downloader2.stdout.readlines()
print(out2)
time.sleep(3600)


'''
clearPollsInFile()

F = open('idpolls.txt','r')
print("Polls.txt")
file = F.read()
F.close()
print(file)
print("\n\n\n")
time.sleep(3600)
'''