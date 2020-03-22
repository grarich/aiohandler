import setuptools  

with open("README.md", "r", encoding="utf-8") as fh:  
    long_description = fh.read()  

setuptools.setup(  
    name="aiohandler",  
    version="0.1.0",  
    author="grarich",  
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