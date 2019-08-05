import subprocess

class ControllerExec:

    def __init__(self):
        return

    def check_git_version(self):
        """
        git version check
        :return:
        """
        cmd = 'pwd'
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

print('Xpresso AI-Abzooba')
print('***************************************')
from subprocess import check_output



#print(check_output("ls -l", shell=True).decode())
#print(check_output("echo $PYTHONPATH", shell=True).decode())
print('Docker Installation Check')
print('***************************************')
pwd='admin1'
cmd='xprctl login -u admin1'
print(check_output("".format(cmd, pwd), shell=True).decode())
