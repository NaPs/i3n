from setuptools import setup, find_packages
import os

version = '0.1~dev'
ldesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='i3n',
      version=version,
      description='Set of tools for i3 wm',
      long_description=ldesc,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent'],
      keywords='i3 notes workspace',
      author='Antoine Millet',
      author_email='antoine@inaps.org',
      url='https://idevelop.org/p/i3n/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=['i3n', 'i3n-bar'],
      include_package_data=True,
      zip_safe=True,
      install_requires=['i3-py'])
