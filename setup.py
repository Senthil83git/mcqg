from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Senthil Kumar',
    author_email='sendhil83@gmail.com',
    install_requires=["openai","langchain","langchain_community","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)