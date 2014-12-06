from os.path import join
from setuptools import setup, find_packages


package_name = 'mpl_style_gallery'
info = {}
execfile(join(package_name, '__init__.py'), info)

main_entry_point = '{}.app:main'.format(package_name)


setup(
    name=package_name,
    version=info['__version__'],
    author='Tony S. Yu',
    author_email='tsyu80@gmail.com',
    maintainer='Tony S. Yu',
    maintainer_email='tsyu80@gmail.com',
    description='Gallery for Matplotlib stylesheets',
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'start-mpl-style-gallery = {}'.format(main_entry_point),
        ]
    },
    license='BSD',
    packages=find_packages(),
)
