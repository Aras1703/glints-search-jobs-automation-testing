from glints.glints import Glints
from getpass4 import getpass
import time


try:
    with Glints() as auto:
        auto.glints_test()
        auto.dropdown_languages('English')
        auto.to_login_page()
        time.sleep(7)
        auto.credential(input("\nEmail or Phone number: "), getpass("\nPassword: "))
        auto.to_jobs_page()
        auto.to_explore_page()
        auto.search_jobs(input('\nWhat kind of job are you looking for ? '))
        auto.job_filtration()
        time.sleep(7)
        auto.report_summary()
        
except Exception as e:
    if "in PATH" in str(e):
        print(
            'If you trying to run the bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows : \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n'
        )
    else:
        raise
