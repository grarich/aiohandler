import setuptools  

with open("README.md", "r") as fh:  
    long_description = fh.read()  

setuptools.setup(  
    name="aiohandler",  
    version="0.0.2",  
    author="distudy",  
    author_email="grarich123+github@gmail.com",  
    description="httpheader for logging on async",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/grarich123/aiohandler",  
    packages=setuptools.find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3.8",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],  
)  