from setuptools import setup

setup(
    name='keras-centernet',
    version='0.0.0',
    description='Keras implementation for CenterNet',
    url='https://github.com/seqsense/keras-centernet',
    author='SEQSENSE',
    packages=['keras_centernet'],
    install_requires=[
        'Keras>=2.2.4',
        'opencv-python>=3.4.3.18',
        'tqdm>=4.26.0',
        #'youtube-dl>=2019.4.30',
        'pytest>=4.4.1',
        'Pillow>=6.0.0',
        'matplotlib>=3.0.3',
        'Cython>=0.29.7',
        'pycocotools>=2.0.0',
    ],
    zip_safe=True,
    license='Other/Proprietary License',
)
