		THE FOLLOWING ARE THE FUNCTION OF THE VARIOUS SCRIPTS
0. 0-iam_betty	    	      	- A script that switches the current user to the user betty.

1. 1-who_am_i			- A script that prints the effective username of the current user.

2. 2-groups			- A script that prints all the groups the current user is part of.

3. 3-new_owner			- A script that changes the owner of the file hello to the user betty.

4. 4-empty			- A script that creates an empty file called hello.

5. 5-execute			- A script that adds execute permission to the owner of the file hello.

6. 6-multiple_permissions	- A script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
   				  The file hello will be in the working directory

7. 7-everybody			- A a script that adds execution permission to the owner, the group owner and the other users, to the file hello
   				      The file hello will be in the working directory
    	       	       	      	      You are not allowed to use commas for this script

8. 8-James_Bond			- A script that sets the permission to the file hello as follows:
   				Owner: no permission at all
				Group: no permission at all
				Other users: all the permissions

9. 9-John_Doe			- A script that sets the mode of the file hello to this:
   				  -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
				  The file hello will be in the working directory
				  You are not allowed to use commas for this script

10. 10-mirror_permissions	- A script that sets the mode of the file hello the same as olleh’s mode.

11. 11-directories_permissions	- A a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

12. 12-directory_permissions	- A script that creates a directory called my_dir with permissions 751 in the working directory.

13. 13-change_group		- A script that changes the group owner to school for the file hello.

14. 100-change_owner_and_group	- A script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

15. 101-symbolic_link_permissions - A script that changes the owner and the group owner of _hello to vincent and staff respectively.
    				  The file _hello is in the working directory
    	 	      	  	  The file _hello is a symbolic link

16. 102-if_only			  - A script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

17. 103-Star_Wars		  - A script that will play the StarWars IV episode in the terminal.