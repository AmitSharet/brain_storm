from setuptools import setup, find_packages


setup(
    name = 'brain_storm',
    version = '0.1.0',
    author = 'Amit Sharet',
    description = 'Advanced System Design University Project',
    packages = find_packages(),
    install_requires = ['click', 'flask', 'Pillow'],
    tests_require = ['pytest', 'pytest-cov'],
)