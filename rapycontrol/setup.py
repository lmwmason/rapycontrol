import setuptools

with open("README.md", "r", encoding="utf-8") as fh :
    long_description = fh.read()

setuptools.setup(
    name="rapycontrol",
    version="0.1.0",
    author="Muwon Lee",
    author_email="lmwmason@naver.com",
    description="A Python library for controlling stepper motors and other devices.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lmwmason/rapycontrol/tree/main/lib",
    