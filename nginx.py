chroot="/var/chroot/nginx"
testCommandsInsideJail=["/usr/sbin/nginx"]
processNames=["nginx"]

testCommandsOutsideJail=["wget -r --spider http://localhost/"]

preserve=["/usr/share/nginx/html",
          "/var/log/nginx",
          "/dev/log"]

users=["nginx"]
groups=["nginx"]

userFiles=["/etc/passwd",
           "/etc/shadow"]

groupFiles=["/etc/group",
            "/etc/gshadow"]

forceCopy=["/etc/hosts",
           "/etc/mime.types"]

