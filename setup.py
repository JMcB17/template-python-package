import setuptools
import template_package


with open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='template-package',
    version=template_package.__version__,
    author='JMcB',
    author_email='joel.mcbride1@live.com',
    license='GPLv3',
    description='Template package!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JMcB17/template-python-package',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'template-package=template_package:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
    ],
    python_requires='>=3',
    install_requires=[

    ]
)
