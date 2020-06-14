from setuptools import find_packages, setup

readme = []
with open('README.rst', 'r') as fh:
    readme = fh.readlines()

tests_require = [
    'django-webtest==1.9.7',
    'factory-boy==2.12.0',
    'mock==4.0.2',
    'pytest-cov==2.8.1',
    'pytest-django==3.9.0',
    'pytest==5.4.2',
    'requests-mock==1.8.0',
    'requests-toolbelt==0.9.1',
]

setup(
    name='localshop',
    version='2.0.0-alpha.1',
    author='Michael van Tellingen',
    author_email='michaelvantellingen@gmail.com',
    url='http://github.com/mvantellingen/localshop',
    description='A private pypi server including auto-mirroring of pypi.',
    long_description='\n'.join(readme),
    zip_safe=False,
    install_requires=[
        'celery==4.3.0',
        'django-braces==1.13.0',
        'django-celery-beat==1.6.0',
        'django-celery-results==1.1.2',
        'django-environ==0.4.5',
        'django-model-utils==3.1.2',
        'django-widget-tweaks==1.4.5',
        'Django==1.11.29',
        'docutils==0.14',
        'netaddr==0.7.19',
        'psycopg2==2.8.5',
        'redis==3.5.3',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    license='BSD',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'localshop = localshop.runner:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
