import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.mlhframework',
      version='0.4.21',
      description=('A docassemble extension.'),
      long_description='# docassemble.mlhframework\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n* 5/28/24   0.4.20 changes to intro and outro questions; add help_user_ask_role_template; change name to MLH-Forms; added progress settings to outro questions; changed review link language\r\n* 4/26/24   0.4.19 Tweaks to cover sheet\r\n* 4/26/24   0.4.18 sign in sign up color update\r\n* 4/22/24   0.4.17 Fix Sign up Sign in styling (2nd attempt)\r\n* 4/9/24    0.4.16 Tweaks to cover sheet\r\n* 4/8/24    0.4.15 Minor wording changes; added tag for GA4 data.\r\n* 4/2/24    0.4.14 Court loader additions; portfolio-wide cover sheet; "Back" and "Next" language. bharrison\r\n* 4/1/24    0.4.13 Update Sign Up Sign In styling\r\n* 3/12/24   0.4.12 Nav panel updates; turn progress bar on by default\r\n* 1/18/24   0.4.11 Help text readability improvements.\r\n* 1/16/24   0.4.10 change collapsible templates from blue to green; correct alt_text typo\r\n* 1/9/24    0.4.9 style/design improvements; skip outro "saving answers" if logged in; fix headers; change exit button to link.\r\n* 1/2/24    0.4.8 change "register" to "sign up" in another spot.\r\n* 1/2/24    0.4.7 Remove unused exit link, redudant logo alt text;Change language from register to sign up.\r\n* 12/11/23  0.4.6 Remove reference to "phone number" from Share page\r\n* 12/11/23  0.4.5 Updated About page; Updated Share page; Fixed missing Continue button bug\r\n* 12/8/23   0.4.4 added: dark mode defaults added, collapsible template explainer; changed: instructions for saving, feedback form for prod server\r\n* 12/5/23   0.4.3 language edits to PII screen; address field and phone improvements; adds common questions; more minor changes\r\n* 11/28/23  0.4.2 minor language edits; separated code blocks (EKM merged).\r\n* 11/8/23   Changes to signature page and minor wording changes. EKM\r\n* 10/25/23  Add index page -EmilyKM\r\n* 10/25/23  CSS improvements and tweaks after using it work a few weeks\r\n* 10/24/23  Enhancements to custom feedback form. bharrison\r\n* 10/12/23  Sync css based on MLH\'s Guide to Legal Help. Bryce Willey\r\n* 10/9/23   Include favicon code to set image for tabs in browsers. Bryce Willey (EKMiller merged).\r\n* 10/6/23   Fixed error in court loader. Bryce Willey \r\n* 10/2/23   Create custom tester feedback form. bharrison\r\n* 8/21/23   Incorporate standard intro/outro screens, global variables. Brett Harrison\r\n* Dec 2022 - July 2023   NEW. Emily K. Miller, ekressmiller@lsscm.org. Built on SuffolkLITLab\'s al_courts programming to allow interviews to populate dropdown menus with counties and then court names usings source spreadsheet. Fixed issue with labels for PO Boxes.\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Emily K. Miller',
      author_email='ekressmiller@lsscm.org',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALToolbox>=0.10.1', 'docassemble.AssemblyLine>=2.28.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/mlhframework/', package='docassemble.mlhframework'),
     )

