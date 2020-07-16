from distutils.core import setup

setup(
    name='SecondaryStructurePredictor',
    version='0.1dev',
    packages=['secondaryStructurePredictor',],


    #package_data={'secondaryStructurePredictor': ['../bin/*']},
    package_data={'secondaryStructurePredictor': ['trained_model/struc_classifier_SD2_0.7907']},
    author='Vincenzo Laveglia',
    author_email='vinclaveglia@gmail.com',
    description='Protein Secondary Structure Predictor',

    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    #long_description=open('README.txt').read(),
    )
