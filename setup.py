from setuptools import setup,find_packages

setup(
    name='pixiv-save',
    version='1.0.4',
    description='save pixiv user illusts',
    author='HIbian',
    author_email='hibianchen@gmail.com',
    install_requires=['PixivPy==3.6.2','argparse'],
    packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts': [
            'pixivsave = pixivsave.main:main'
        ]
    },
    scripts=['pixivsave.py']
)
# python setup.py bdist_wheel  
# python setup.py sdist    
# twine upload dist/pixiv_save-{version}*