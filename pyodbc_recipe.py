from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class PyodbcRecipe(CompiledComponentsPythonRecipe):
    version = '4.0.30'
    url = 'https://github.com/mkleehammer/pyodbc/archive/{version}.tar.gz'
    site_packages_name = 'pyodbc'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True
    install_in_targetpython = False

recipe = PyodbcRecipe()
