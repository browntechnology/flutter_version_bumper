# flutterver: Flutter Versioning
This is a command line tool to manage Flutter projects versioning.

# Installation
Copy `flutterver` executable (from `dist` folder) to your Flutter project location.

# Usage
Syntax: `flutterver COMMAND [options]`

Commands:

    bump                  Bump the version of the project automatically
    
    set VERSION_STRING    Set the version of the project to the VERSION_STRING (A.B.C+X)
    
Options:

    --hotfix      Will only bump the hotfix in the version
    
    --commit      Will commit the changes after bumping the version and will add a git tag
    
    --stable      Set this version as a stable version (git tag will start with v)
    
    --beta        (Default) Set this version as beta version (git tag will start with beta-)
    

# Examples

## Bump the version automatically
Bumping the version `A.B.C` starting from `C`, Maximum value for `C` and `B` is 9. `A` doesn't have a maximum value.

Command: ```$ ./flutterver bump```

Result Examples:

  `Old Version` ➞    `New Version`
  
  `1.0.0`       ➞   `1.0.1`
  
  `1.0.2+1`     ➞   `1.0.3`
  
  `1.0.9`       ➞   `1.1.0`
  
  `1.9.6`       ➞   `1.9.7`
  
  `1.9.9`       ➞   `2.0.0`
  
  `9.9.9`       ➞   `10.0.0`
  
## Bump or add version hotfix
Bumping the `X` value in version `A.B.C+X` or add `+1` in version `A.B.C`. `X` value has no maximum.

Command: ```$ ./flutterver bump --hotfix```

Result Examples:

  `Old Version` ➞    `New Version`
  
  `1.0.0`       ➞   `1.0.1+1`
  
  `1.0.2+1`     ➞   `1.0.2+2`
  
  `1.0.9`       ➞   `1.0.9+1`
  
  `1.0.9+9`     ➞   `1.0.9+10`
  
  
## Set the version manually
Set the version to version `A.B.C+X` or `A.B.C`.

`NOTICE: Only A.B.C or A.B.C+X versioning is acceptable`

Command: ```$ ./flutterver set 2.0.4+2```

Result Examples:

  `Old Version` ➞    `New Version`
  
  `1.0.0`       ➞   `2.0.4+2`
  
  `1.0.2+1`     ➞   `2.0.4+2`
  
  `3.1.9`       ➞   `2.0.4+2`
  

## Commiting and adding a tag automatically
Adding the `--commit` option will commit all the changes after bumping the version under message `Prepare for version {NEW_VERSION}`, and will create a tag `v{NEW_VERIONS}` if `--stable` option is set, or tag `beta-{NEW_VERSION}` by default or if `--beta` option was set.

<br/>
<br/>

Made with ❤️ By [Brown Technology](https://www.brown-technology.com)
