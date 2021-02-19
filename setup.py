from distutils.core import setup

setup(
    name='moodle-kit',
    packages=['moodle_kit'],
    version='0.1.1', 
    license='GNU',
    description='A simple Python package with some functionalities to interact with moodle-based LMS.',
    author='Ahmad Febrianto',
    author_email='achmadfebryanto@gmail.com',
    url='https://github.com/ahmadfebrianto/moodle-kit',
    download_url='https://github.com/ahmadfebrianto/moodle-kit/archive/v0.1.1.tar.gz',
    keywords=['moodle'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
