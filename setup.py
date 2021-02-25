from setuptools import setup
from os import path


base_dir = path.abspath(path.dirname(__file__))
with open(path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='moodle-kit',
    packages=['moodle_kit'],
    version='0.1.7', 
    license='GNU General Public License v3.0',
    description='A simple Python package with some functionalities to interact with moodle-based LMS.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Ahmad Febrianto',
    author_email='achmadfebryanto@gmail.com',
    url='https://github.com/ahmadfebrianto/moodle-kit',
    download_url='https://github.com/ahmadfebrianto/moodle-kit/archive/v0.1.7.tar.gz',
    keywords=['moodle'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
)
