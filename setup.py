
import setuptools


setuptools.setup(setup_requires=['pbr'],
                 pbr=True,
                 test_suite="pylint_flectra.test",
                 package_data={'': ['*.yaml']})
