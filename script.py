files = [
    {
        "name":"Linpeas",
        "location":"https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh",
        "saveTo":"../Linux/Enumeration"
    },
    {
        "name":"LinEnum",
        "location":"https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh",
        "saveTo":"../Linux/Enumeration"
    },
]

gits = [
    {
        "name":"python-pty-shells",
        "repo":"https://github.com/infodox/python-pty-shells.git",
        "saveTo":"../Shells"
    }
]

for file in files:
    try:
        output = subprocess.call(["wget", "--no-if-modified-since","-nc", "-P",file["saveTo"], file["location"]], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(e)

for git in gits:
    
    if os.path.isdir(git["saveTo"]+"/"+git["name"]):
        subprocess.call(["git", "-C", git["saveTo"]+"/"+git["name"], "pull"])
    else:
        if not os.path.isdir(git["saveTo"]):
            os.makedirs(git["saveTo"])
        subprocess.call(["git", "-C", git["saveTo"], "clone", git["repo"]])
