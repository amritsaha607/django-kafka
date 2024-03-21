from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-kafka',
    version='0.0.9',
    description='An utility library for django & kafka integration',
    package_dir={
        '': 'app',
    },
    packages=find_packages(where='app'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amritsaha607/django-kafka.git',
    author='amritsaha607',
    author_email='amritsaha607@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
