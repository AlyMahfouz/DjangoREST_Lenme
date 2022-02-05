from setuptools import setup

setup(
    name='Django',
    version='0.1',
    license='GPL3',
    author='Aly Mahfouz',
    author_email='alykdev@gmail.com',
    description='Using REST API',
    install_requires=[
 
        #libs Tool
        
        'django',
        'djangorestframework',
        'django-filter',
        'markdown'
    ]
)