import setuptools
setuptools.setup(name='Reptyl Shell',
    version='0.0.0.3',
    author='0ut0flin3',
    description='Reptyl is a cross-platform command line shell that supports execution of commands in natural language ',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        
                ],
    install_requires=['openai==0.26.1'],
    python_requires='>=3'
        )
