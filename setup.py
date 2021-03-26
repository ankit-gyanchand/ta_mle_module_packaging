from setuptools import setup

setup(
    name='helloworld',
    version='0.0.1',
    description='description of say hello.',
    py_modules=['say_hello'],
    package_dir={'': 'src'},
    classifiers=[
        'programming language :: Python :: 3',
        'programming language :: Python :: 3.6',
        'programming language :: Python :: 3.7',
        'License :: MIT License :: simple and permissive',
        'Operating System :: OS independent',
    ],
    install_requires=[
        
    ],
    extras_require={
        'dev': [
            'pytest>=3.7',
        ]
    },
    url='www.google.com',
    author='Ankit',
    author_email='moralankit@gmail.com',
    
)

