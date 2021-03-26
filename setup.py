from setuptools import setup

setup(
    name="helloworld",
    version="0.0.1",
    description="description of say hello.",
    py_modules=["say_hello"],
    package_dir={"": "src"},
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    },
    url="https://github.com/ankit-gyanchand/ta_mle_module_packaging",
    author="ankit_300",
    author_email="ankit.gyanchand@tigeranalytics.com",
)
