WHAT IS A SCRIPT ?
	
	-Is a plain text file containing a series of
	 intructuions.

HOW DO SCRIPTS WORK ?

	-Scripts work like any program, by executing
	 every instruction one after the other.

HOW TO RUN OR EXECUTE A SCRIPT IN LINUX ?

	-Scripts are run or executed by typing
	 ./name of the script and pressing enter.

WHY THE ./ BEFORE THE NAME OF THE SCRIPT ?

	-In linux commands are located in special
	 directories that are listed in the $PATH 
	 variable.

	-When we type a word and press enter $BASH
	 assumes it is a command and starts looking
	 for in the directories listed in the $PATH
	 variable and when it founds a first match
	 tries to run it.

	-We type the ./ caracters to tell $BASH that
	 the command is in the working directory
	 and not to look for it in the ones listed in
	 $PATH.

The Shebang (#!)
	
	-This #!/bin/bash must be the first line in a 
	 script it contains the Shebang followed by 
	 the $PATH to the interpreter(program) that will 
	 interpret(run)the rest of the lines in the text 
	 file.

Formating (IMPORTANT)

	-The Shebang must be in the very first line
	 (line 2 won't do even if the first line is blank).
	 There must be no spaces between the # and ! and
	 the $PATH to the interpreter(program).
