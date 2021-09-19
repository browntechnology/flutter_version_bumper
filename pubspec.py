# This file holds the functions to update and bump the version in pubspec.yml file

from version import Version

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import yaml
import collections

def _readPubspec():
    # Reading the pubspec.yml file
    pubspec_r_stream = open("pubspec.yml", "r")
    pubspec = yaml.load(pubspec_r_stream, Loader=Loader)
    pubspec_r_stream.close()

    return pubspec

#Using a custom Dumper class to prevent changing the global state
class CustomDumper(yaml.Dumper):
    #Super neat hack to preserve the mapping key order. See https://stackoverflow.com/a/52621703/1497385
    def represent_dict_preserve_order(self, data):
        return self.represent_dict(data.items())    

CustomDumper.add_representer(dict, CustomDumper.represent_dict_preserve_order)

def _writePubspec(pubspec_dict):
     # Writing the changes to pubspec.yml file
    pubspec_w_stream = open("pubspec.yml", "w")
    pubspec_w_stream.write(yaml.dump(pubspec_dict, Dumper=CustomDumper))
    pubspec_w_stream.close()

# Set the version of pubspec.yml file
def setPubspecVersion(new_version_str):
    pubspec = _readPubspec()
    pubspec["version"] = new_version_str
    _writePubspec(pubspec)

# Bump pubspec.yml version
def bumpPubspecVersion(isHotfix):
    pubspec = _readPubspec()

    v = Version(pubspec["version"])
    v.bump(isHotfix)
    
    pubspec["version"] = v.versionString()
    _writePubspec(pubspec)
    return v.versionString()
   
