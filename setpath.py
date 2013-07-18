import os
import os.path
def which(filename):
    paths = os.environ.get("PATH").split(os.pathsep)
    cmds = []
    for path in paths:
        cmd = os.path.join(path, filename)
        if os.path.isfile(cmd):
            cmds.append(cmd)
    return cmds

npm = which('npm')[0]
bower = which('bower')[0]
print os.environ["PATH"]
pathlist = [npm, bower]
os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)

print os.environ["PATH"]
