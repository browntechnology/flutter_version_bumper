# This file holds the Version class

class Version:
    def __init__(self, versionText):
        ver_dot_splited = versionText.split(".")
        major = int(ver_dot_splited[0])
        minor = int(ver_dot_splited[1])
        buildno_and_hotfix = ver_dot_splited[2].split("+")
        build_no = int(buildno_and_hotfix[0])
        hotfix = 0
        if len(buildno_and_hotfix) > 1:
            hotfix = int(buildno_and_hotfix[1])

        self.major = major
        self.minor = minor
        self.build_no = build_no
        self.hotfix = hotfix
    
    # Return the version as string
    def versionString(self):
        hotfix_str = ""
        if self.hotfix != 0:
            hotfix_str = "+" + str(self.hotfix)
        
        ver_str = str(self.major) + "." + str(self.minor) + "." + str(self.build_no) + hotfix_str
        return ver_str

    def bump(self, isHotfix):
        # if isHotfix bump the hotfix only
        if isHotfix:
            self.hotfix = self.hotfix + 1
        else:
            self.hotfix = 0
            # bump the build_no first
            if self.build_no == 9:
                self.build_no = 0
                # Then if the build_no is 9 bump the minor
                if self.minor == 9:
                    # If minor is 9 bump the major
                    self.minor = 0
                    self.major = self.major + 1
                else:
                    self.minor = self.minor + 1
            else:
                self.build_no = self.build_no + 1