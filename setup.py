#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="ansible-runner-kafka",
    version="0.1",
    author="Elmar Athmer",
    url="https://github.com/zauberpony/ansible-runner-kafka",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'confluent-kafka',
    ],
    entry_points={'ansible_runner.plugins': 'kafka = ansible_runner_kafka'},
    zip_safe=False,
)
