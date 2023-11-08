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
      version='0.4.0',
      description=('A docassemble extension.'),
      long_description="# docassemble.mlhframework\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n* 10/12/23   Sync css based on MLH's Guide to Legal Help. Bryce Willey\r\n* 10/9/23    Include favicon code to set image for tabs in browsers. Bryce Willey (EKMiller merged).\r\n* 10/6/23    Fixed error in court loader. Bryce Willey \r\n* 10/2/23    Create custom tester feedback form. bharrison\r\n* 8/21/23    Incorporate standard intro/outro screens, global variables. Brett Harrison\r\n* Dec 2022 - July 2023   NEW. Emily K. Miller, ekressmiller@lsscm.org. Built on SuffolkLITLab's al_courts programming to allow interviews to populate dropdown menus with counties and then court names usings source spreadsheet. Fixed issue with labels for PO Boxes.\r\n\r\n",
      long_description_content_type='text/markdown',
      author='Emily K. Miller',
      author_email='ekressmiller@lsscm.org',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.AssemblyLine>=2.26.0', 'googledrivedownloader>=0.4'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/mlhframework/', package='docassemble.mlhframework'),
     )

