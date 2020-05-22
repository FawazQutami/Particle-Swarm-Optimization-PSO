"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Setup Functions - install required libraries
-- File Name    :   setup.py
-- *********************************************
"""

# load Packages
import subprocess
import sys

from eHandler import PrintException as EH

marks = '==' * 30 + '\n'


def install_required_Packages():
    """
    Install the required PACKAGES
    :return: Nothing
    """

    try:
        # List all the required packages
        required_packages = [
            'matplotlib',
            'numpy',
        ]

        # Check and retrieve the installed packages info
        installed = subprocess.check_output(
            [
                sys.executable
                ,'-m'
                ,'pip'
                ,'freeze'
            ]
        )
        # Split and strip the returned info to get the
        # installed packages names list
        installed_packages = [r.decode().split('==')[0]
                              for r in installed.split()]
        # Loop over the required packages
        for package in required_packages:
            # If the package is not in the installed packages
            if package not in installed_packages:
                # print informative message
                print(marks)
                print("Installing {}! Please wait ...")
                print(marks)
                # Send a check call and install the package
                subprocess.check_call(
                    [
                        sys.executable
                        ,"-m"
                        ,"pip"
                        ,"install"
                        ,package
                    ]
                )
    except:
        EH()