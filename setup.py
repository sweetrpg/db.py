from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-db",
    install_requires=[
        "dnspython~=2.0",
        "marshmallow~=3.0",
        "mongoengine~=0.27",
        "PyMongo[srv]~=3.0",
        "sweetrpg-model-core",
        "sweetrpg-common",
    ],
    extras_require={},
)
