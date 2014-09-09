from setuptools import setup, find_packages

version = '0.3.0'

setup(name="helga-prod-fixer",
      version=version,
      description=('IRC bot using twisted'),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='helga fix prod',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/helga',
      license='MIT',
      packages=find_packages(),
      py_modules=['helga_prod_fixer'],
      entry_points = dict(
          helga_plugins=[
              'fixprod = helga_prod_fixer:fix',
          ],
      ),
)
