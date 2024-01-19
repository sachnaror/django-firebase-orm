import firebase_orm
from setuptools import find_packages, setup

setup(
    name="django-firebase-orm",
    version=firebase_orm.__version__,
    description="NoSQL object model database for django ORM integration",
    author="Tralah M Brian",
    author_email="schnaror@gmail.com",
    url="https://github.com/sachnaror/django-firebase-orm",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "firebase-admin==2.13.0",
        "grpcio>=1.9.1",
        "django",
    ],
    test_suite="tests",
    license="MIT",
)
