"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics
-- File Name    :   eHandler.py
-- *********************************************
"""

# load Packages
import linecache
import sys

marks = '==' * 30 + '\n'


def PrintException():
    """ Exception Handling
    :return: string message about exception type and location
    """

    # Get the exception objects from the system
    excType, excObj, tbl = sys.exc_info()
    # Construct the table object frame
    tbl_Frame = tbl.tb_frame
    # Get the line number from the table
    line_no = tbl.tb_lineno
    # get the file name from the table
    file_name = tbl_Frame.f_code.co_filename
    # from linecash package check the file
    linecache.checkcache(file_name)
    # Get the line details from the file
    line = linecache.getline(file_name, line_no, tbl_Frame.f_globals)

    # Construct the error message and location
    msg = f'*** Error Message ***:\n' \
        f'\tf"File Name:({file_name}' \
        f'\n\tLINE #: {line_no}' \
        f'\n\tWhere: {line.strip()}' \
        f'\n\tError: {excObj}'
    # Print the exception error message
    print(marks + msg + '\n' + marks)