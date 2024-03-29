__author__ = 'Reyaz Ahmad'

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
        #returned_output = subprocess.check_output(cmd)


        p = subprocess.Popen(["xprctl login -u admin1"], stdout=subprocess.PIPE, shell=True)

        print(p.communicate())


        #print('Output:', returned_output)

    def login(self):
        """
                login without user
                :return:
        """
        cmd = "xprctl login"
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

    def login_with_user_name(self):
        """
        login with user
        :return:
        """
        cmd = "xprctl login -u user1"
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

    def logout(self):
        """
        logout
        :return:
        """
        # cmd= "xprctl logout"
        # returned_output=subprocess.check_output(cmd)
        cat = subprocess.Popen(['pwd'],
                        stdout=subprocess.PIPE,
                        )
        print('Output:', cat)


    def get_data(self):
        """

        :return:
        """
        # p = subprocess.Popen(["xprctl login"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        p = subprocess.Popen(["xprctl login -u admin1"], stdout=subprocess.PIPE, shell=True)
        p.communicate("")



controller_exec=ControllerExec()
# controller_exec.check_git_version()
controller_exec.get_data()

