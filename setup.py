import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='python_ib',  
     version='0.1',
     #scripts=['dokr'] ,
     author="Luis Miguel Sáez",
     author_email="luismiguelsaez83@gmail.com",
     description="Interactive Brokers flex query download",
     url="https://github.com/luismiguelsaez/python-library-interactive-brokers/script",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )