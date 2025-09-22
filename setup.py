import os
import sys
from setuptools import setup, find_namespace_packages
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
      version='1.0.18',
      description=('A docassemble extension.'),
      long_description='# docassemble.mlhframework\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n* 9/22/25   1.0.18 minor language edits; email-forms-to-self and error screen improvements\r\n* 8/14/25   1.0.17 minor language edits and add "patience, assembling" screen\r\n* 8/11/25   1.0.16 add "github_user" entry to avoid spammy log messages\r\n* 7/21/25   1.0.15 Edit terms and conditions to reflect PPO deletion after 60 days\r\n* 5/29/25   1.0.14 About page updates; minor terms of use update\r\n* 4/17/25   1.0.13 simplify feedback form output\r\n* 4/10/25   1.0.12 tweak feedback form and add email collection\r\n* 4/3/25    1.0.11 add court logic for 2nd Ottawa circuit location; update "Can I e-file?" info\r\n* 3/11/25   1.0.10 update cover sheets\r\n* 2/25/25   1.0.9 update address defaults; add function to remove unneeded punctuation\r\n* 1/27/25   1.0.8 fix sign in/sign up text issue\r\n* 1/8/25    1.0.7 add name field to tester feedback form\r\n* 12/13/24  1.0.6 update court addresses\r\n* 11/21/24  1.0.5 update privacy policy\r\n* 10/28/24  1.0.4 add sign-in button to "home" page; simplify tester feedback form\r\n* 10/7/24   1.0.3 add placeholder survey embed code\r\n* 10/1/24   1.0.2 download screen and coversheet updates to add new user surveys\r\n* 9/17/24   1.0.0 tweak download screen; advance to version 1 since this is now live\r\n* 9/9/24    0.4.37 add download screen to framework; update error page\r\n* 9/6/24    0.4.36 remova comma ref from validation messages; update feedback form\r\n* 8/22/24   0.4.35 coversheet 2.0 method\r\n* 8/19/24   0.4.34 update snapshot method\r\n* 8/16/24   0.4.33 set progress bar method: stepped\r\n* 8/13/24   0.4.32 display logo on administrative pages\r\n* 8/1/24    0.4.31 Override default validation messages\r\n* 7/23/24   0.4.30 Tweak review accordion code; remove default for MLH_esign; update courts source; help text edit\r\n* 7/11/24   0.4.29 Add review screen accordion code\r\n* 7/3/24    0.4.28 Add "down for maintenance" template to framework\r\n* 6/24/24   0.4.27 Remove old saving and navigation intro screens\r\n* 6/20/24   0.4.26 Update Terms of Use and Privacy Policy\r\n* 6/13/24   0.4.25 Intro/outro changes; add help info on OP lawyer\r\n* 6/3/24    0.4.24 Fix button refs on share screen; remove share in-progress option\r\n* 5/31/24   0.4.23 Remove share json file option from sharing page\r\n* 5/30/24   0.4.22 Update phone collection screens; add terms and conditions screen\r\n* 5/29/24   0.4.21 increase Sign Up button size; retitle "My Forms" page\r\n* 5/28/24   0.4.20 changes to intro and outro questions; add help_user_ask_role_template; change name to MLH-Forms; added progress settings to outro questions; changed review link language\r\n* 4/26/24   0.4.19 Tweaks to cover sheet\r\n* 4/26/24   0.4.18 sign in sign up color update\r\n* 4/22/24   0.4.17 Fix Sign up Sign in styling (2nd attempt)\r\n* 4/9/24    0.4.16 Tweaks to cover sheet\r\n* 4/8/24    0.4.15 Minor wording changes; added tag for GA4 data.\r\n* 4/2/24    0.4.14 Court loader additions; portfolio-wide cover sheet; "Back" and "Next" language. bharrison\r\n* 4/1/24    0.4.13 Update Sign Up Sign In styling\r\n* 3/12/24   0.4.12 Nav panel updates; turn progress bar on by default\r\n* 1/18/24   0.4.11 Help text readability improvements.\r\n* 1/16/24   0.4.10 change collapsible templates from blue to green; correct alt_text typo\r\n* 1/9/24    0.4.9 style/design improvements; skip outro "saving answers" if logged in; fix headers; change exit button to link.\r\n* 1/2/24    0.4.8 change "register" to "sign up" in another spot.\r\n* 1/2/24    0.4.7 Remove unused exit link, redudant logo alt text;Change language from register to sign up.\r\n* 12/11/23  0.4.6 Remove reference to "phone number" from Share page\r\n* 12/11/23  0.4.5 Updated About page; Updated Share page; Fixed missing Continue button bug\r\n* 12/8/23   0.4.4 added: dark mode defaults added, collapsible template explainer; changed: instructions for saving, feedback form for prod server\r\n* 12/5/23   0.4.3 language edits to PII screen; address field and phone improvements; adds common questions; more minor changes\r\n* 11/28/23  0.4.2 minor language edits; separated code blocks (EKM merged).\r\n* 11/8/23   Changes to signature page and minor wording changes. EKM\r\n* 10/25/23  Add index page -EmilyKM\r\n* 10/25/23  CSS improvements and tweaks after using it work a few weeks\r\n* 10/24/23  Enhancements to custom feedback form. bharrison\r\n* 10/12/23  Sync css based on MLH\'s Guide to Legal Help. Bryce Willey\r\n* 10/9/23   Include favicon code to set image for tabs in browsers. Bryce Willey (EKMiller merged).\r\n* 10/6/23   Fixed error in court loader. Bryce Willey \r\n* 10/2/23   Create custom tester feedback form. bharrison\r\n* 8/21/23   Incorporate standard intro/outro screens, global variables. Brett Harrison\r\n* Dec 2022 - July 2023   NEW. Emily K. Miller, ekressmiller@lsscm.org. Built on SuffolkLITLab\'s al_courts programming to allow interviews to populate dropdown menus with counties and then court names usings source spreadsheet. Fixed issue with labels for PO Boxes.\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Emily K. Miller',
      author_email='ekressmiller@lsscm.org',
      license='',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.ALToolbox>=0.12.0', 'docassemble.AssemblyLine @ git+https://github.com/SuffolkLITLab/docassemble-AssemblyLine.git@main', 'docassemble.GithubFeedbackForm>=0.5.6'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/mlhframework/', package='docassemble.mlhframework'),
     )
