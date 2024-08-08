from setuptools import setup, find_packages

setup(
    name="slurm_utils",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "click",  # for CLI interface
    ],
    entry_points={
        "console_scripts": [
            "slurm_utils=slurm_utils.cli:main",
        ],
    },
    author="Giannis Daras",
    author_email="giannisdaras@utexas.edu",
    description="A utility library for SLURM job management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/giannisdaras/slurm_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)