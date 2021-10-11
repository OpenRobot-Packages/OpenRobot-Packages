from setuptools import setup

readme = ''
with open('README.md') as f:
    readme = f.read()
    
packages = [
    'openrobot'
]

setup(
    name='OpenRobot-Packages',
    author='OpenRobot',
    url='https://github.com/OpenRobot/Packages',
    version='0.0.0',
    packages=packages,
    license='MIT',
    description='The base package that will be installed on any OpenRobot package.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    classifiers=[]
)
