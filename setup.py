from setuptools import setup


setup(
    name='blog-api',
    version='0.1.0',
    author='asterix',
    install_requires=[
        'fastapi',
        'uvicorn',
        'SQLAlchemy',
        'alembic',
        'asyncpg',
        'pydantic',
        'pydantic-settings'
    ]
)
