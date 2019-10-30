from typing import Optional

from setuptools import setup, find_packages


package_name = 'cognitive_complexity'


def get_version() -> Optional[str]:
    with open('cognitive_complexity/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")
    return None


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='Library to calculate Python functions cognitive complexity via code',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    keywords='flake8',
    version=get_version(),
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools'],
    url='https://github.com/Melevir/cognitive_complexity',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
