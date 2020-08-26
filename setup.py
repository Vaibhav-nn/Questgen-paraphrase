from distutils.core import setup

setup(name='Questgen',
      version='1.0.0',
      description='Question generator from any text',
      author='Questgen contributors',
      author_email='vaibhavtiwarifu@gmail.com',
      license='gnu',
      packages=['Questgen'],
      url="https://github.com/ramsrigouthamg/Questgen.ai",

      package_data={'Questgen': ['questgen.py', 'mcq.py', 'train.py']}
      )
