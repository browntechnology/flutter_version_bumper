import pubspec as p
import git
import sys

help_str = """
Welcome to flutter_bump_version Tool.
By Brown Technology.

Syntax: flutter_bump_version COMMAND [options]
Commands:
\t    bump\t\t\tBump the version of the project automatically
\t    set VERSION_STRING\t\tSet the version of the project to the VERSION_STRING (A.B.C+X)
Options:
\t    --hotfix\t\t\tWill only bump the hotfix in the version
\t    --commit\t\t\tWill commit the changes after bumping the version and will add a git tag
\t    --stable\t\t\tSet this version as a stable version (git tag will start with v)
\t    --beta\t\t\t(Default) Set this version as beta version (git tag will start with beta-)
"""

def main():
    if len(sys.argv) < 2:
        print(help_str)
        return
    
    newVersion = ""
    if sys.argv[1] == "bump":
        newVersion = p.bumpPubspecVersion("--hotfix" in sys.argv)
    elif sys.argv[1] == "set":
        if len(sys.argv) < 3:
            print(help_str)
            return
        p.setPubspecVersion(sys.argv[2])
        newVersion = sys.argv[2]
    else:
        print(help_str)
        return
    
    if "--commit" in  sys.argv:
        git.gitCommitAndTag(newVersion, "--stable" not in sys.argv)

if __name__ == "__main__":
    main()

