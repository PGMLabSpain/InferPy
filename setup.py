from setuptools import setup

exec(open('inferpy/version.py').read())

setup(
    name='inferpy',
    version=__version__,
    description='Deep probabilistic modelling made easy',
    author='Andrés R. Masegosa, Rafael Cabañas',
    author_email="andresma@ual.es, rcabanas@ual.es",
    packages=['inferpy', 'inferpy.inferences',
              'inferpy.models', 'inferpy.util'],
    install_requires=['numpy>=1.7'],
    extras_require={
        'tensorflow': ['tensorflow>=1.2.0rc0'],
        'tensorflow with gpu': ['tensorflow-gpu>=1.2.0rc0'],
        'visualization': ['matplotlib>=1.3',
                          'pillow>=3.4.2',
                          'seaborn>=0.3.1']},
   # tests_require=['pytest', 'pytest-pep8'],
    url='http://inferpy.readthedocs.io',
    keywords='machine learning statistics probabilistic programming tensorflow edward',
    license='Apache License 2.0',
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
<<<<<<< HEAD
=======
                 'Programming Language :: Python :: 2.7',
>>>>>>> 7336269c3037a882c57af3063e887eec2e47741a
                 'Programming Language :: Python :: 3.4'],
)
