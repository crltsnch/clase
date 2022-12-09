from setuptools import setup

setup(
    name="paquete",
    version="1.0",
    description="Paquete de prueba",
    author='Jorge',
    package="paquete",
    packages=['paquete':'paquete.hola', 'paquete.adios'],
    script=['']
)