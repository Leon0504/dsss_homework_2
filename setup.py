from setuptools import setup, find_packages

setup(
    name='math_quiz',  # The name of package
    version='0.1',  # The initial version of package
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Creates a CLI command `math_quiz` to run `math_quiz` function
        ],
    },
    license='MIT',  # My using license
    description='A simple math quiz game that tests arithmetic skills.',
    long_description=open('README.md').read(),  # Reads the content of README.md for the long description
    long_description_content_type='text/markdown',
    url='<https://github.com/Leon0504/dsss_homework_2>',
    author='Dingjia Lin',
    author_email='lindingjia8@gmail.com',  # My name and email-address
)
