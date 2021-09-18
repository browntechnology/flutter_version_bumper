# This file holds the functions to commit the changes after updating the version
import os

def gitCommitAndTag(versionOrVersionString, isBeta):
    os.system("git add *")
    ver_str = ""
    if type(versionOrVersionString) is str:
        ver_str = versionOrVersionString
    else:
        ver_str = versionOrVersionString.versionString()
    os.system("git commit -m \"Prepare for version " + ver_str + "\"")
    if isBeta:
        os.system("git tag beta-" + ver_str)
    else:
        os.system("git tag v" + ver_str)
    