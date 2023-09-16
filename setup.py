import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Text-Summarizer-Project'
AUTHOR_USER_NAME = 'senthil100695'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'senthil100695@gmail.com'

setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= 'A small Python pacakage for nlp app',
    long_description= long_description,
    long_description_content_type="text/markdown",
    url = f'https://github.com/senthil100695/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        "Bug Tracker" : f"https://github.com/senthil100695/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {'':'src'},
    packages = setuptools.find_packages(
        where='src'
    ),
    )