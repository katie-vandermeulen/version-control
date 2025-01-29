import time
print(time.time())

f = open('/workspace/version-control/projectName/output/version.md','w')
f.write(str(time.time()) + '\n')
f.close()