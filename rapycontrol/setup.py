import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rapycontrol",
    version="0.1.0",
    author="Muwon Lee",
    author_email="lmwmason@naver.com",
    description="A Python library for controlling stepper motors and other devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmwmason/rapycontrol/tree/main/rapycontrol",
    install_requires=[
        "RPi.GPIO==0.7.1",
        "pyserial==3.5",
    ],
    package_data={'': ['LICENSE.txt', 'requirements.txt']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

