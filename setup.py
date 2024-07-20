import setuptools

with open ("README.md", "r") as file:
    long_description = file.read()
    
__version__ = "1.0.0"

REPO_NAME = "END-TO-END_NLP"
AUTHOR_USER_NAME = 'akanksha-th'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'ak.t.kree@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A local package for text summarization",
    long_description = long_description,
    url='https://github.com/akanksha-th/' + REPO_NAME,
    project_urls={
        "Bug Tracker": f'https://github.com/akanksha-th/{REPO_NAME}/issues',
    },
    package_dir= {'': 'src'},
    packages=setuptools.find_packages(where='src')
)

