import pubspec as p

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
    p.bumpPubspecVersion(False)

if __name__ == "__main__":
    main()

