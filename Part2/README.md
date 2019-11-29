# Part II

This part is based on the simple tool developed in part 1. 

This part is to use Travis CI to clone this GitHub repository and test the code every time a change is committed. 

All functions are same as the functions in part 1. But since the code need to be run automatically, some parameters like instance name, project name, and so on, are embedded in the code. 

The setup script to deploy on Travis CI is the .travis.yml file under root. And the script that will be executed on Travis CI is the run.sh under this folder. 
