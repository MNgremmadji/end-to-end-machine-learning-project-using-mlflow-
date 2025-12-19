import setuptools 

with open('README.md', 'r', encoding= 'utf-8') as f: 
    long_description = f.read() 

__version__ = "0.0.0" 

repo_name = "end-to-end-machine-learning-project-using-mlflow-" 
author_user_name = "MNgremmadji"
src_repo = "mlproject" 
author_email = 'oxmbaimou.gmail.com' 

"""setuptools.setup(
     name=src_repo , 
    version= __version__ , 
    author= author_user_name, 
   description= " a python package for ml app", 
    long_description= long_description, 
    long_description_content = 'text/markdown' ,  
    url = f"https://github.com/{author_user_name}/{repo_name}",
    projects_urls = {
    "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    package_dir={"":"src"} ,
)
"""

setuptools.setup(
    name=src_repo , 
    version= __version__ , 
    author= author_user_name, 
    description= " a python package for ml app", 
    long_description= long_description, 
    long_description_content = 'text/markdown' , 
    url = f"https://github.com/{author_user_name}/{repo_name}" , 
    projects_urls = {
    "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    package_dir={"":"src"} , 
    packages= setuptools.find_packages(where = "src")
)