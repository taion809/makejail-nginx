About
=====
Configuration and patch file for makejail and nginx on debian squeeze.

Instructions
========
If you only want the config you can pull or copy it from here.

If you download it, the easiest place to put it is in the makejail directory

	sudo mv nginx.py /etc/makejail/nginx.py
	
	cd /etc/makejail
	
	sudo makejail nginx.py

After that you will need to edit your nginx script inside of /etc/init.d/
I have provided a patchfile for convenience (this is for the nginx 1.2.5 release on squeeze provided by nginx.org)

More?
=====
My blog which details using makejail and nginx can be found here: http://www.redstalker.com