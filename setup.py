import setuptools

setuptools.setup(
     name='python_ib',  
     version='0.1',
     author="Luis Miguel Sáez",
     author_email="luismiguelsaez83@gmail.com",
     description="Interactive Brokers flex query download",
     url="https://github.com/luismiguelsaez/python-library-interactive-brokers/script",
     packages=setuptools.find_packages(),
     install_reqs = parse_requirements('requirements.txt', session='hack'),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )