from distutils.core import setup

setup(  name='apiblender',
        version='0.1',
        description='API Blender allows you to easily interact with many APIs',
        author='Georges Gouriten',
        author_email='georges.gouriten@gmail.com',
        url='http://github.com/netiru/apiblender',
        packages=['apiblender'],
        package_data={'apiblender': [   'config/*.example', 
                                        'config/*/*.example',
                                        'config/*/*/*.example']},
        requires = ['oauth2'],
        license = "GNU/GPL v3 License",
        keywords="api"    )
