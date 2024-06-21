INTRODUCTION

 -Varibles are a temporary store for a piece of information

HOW DO THEY WORK ?

 -There are two actions we can perform with variables

	-Setting (storing) the value of the variable
	 directly or indirectly (result of a process)

	-Reading (getting) the value from the variable
	 by placing the varible name preceded by a "$"
	 
 -Before Bash interprets (runs) each line of a script it
  checks for variables and replaces them for it's value.

COMMAND LINE ARGUMENTS && SCRIPT VARIABLES

	-Commands use argumnets to modify it's behaviour

	-Scripts use varibles to accept arguments and
	 modify their behaviour

SPECIAL VARIABLES (Automatically set by the system)

	-$0 The name of the Bash script
	-$1..$9 The first nine arguments to the Bash script
	-$# How many arguments are passed to the Bash script
	-$@ All the arguments passed to the Bash script
	-$? The exit status of the most recently run process
	-$$ The process ID of the current script
	-$USER The username of the user running the script
	-$HOSTNAME the hostname of the machine running the script
	-$SECONDS The number of seconds since the script was started
	-$RANDOM Returns a different random number each time
	-$LINENO Returns the current line number in the Bash script

SETTING VARIABLES

	-variable=value (no space before or after the = sign)
	-Bash is case sensitive

QUOTES
	-Single quotes will treat every caracter literally
	-Doble quotes will allow you to do substitution that is the
	 use of variables in the setting of a value

COMMAND SUBSTITUTION

	-Command substitution allows us to store the output of a 
	 command or a program in a variable
	-To do so you need to place it inside of brackets()
	 peceded by a $

EXPORTING VARIABLES

	-Scripts run inside their own process so the scope of
	 a variable is that particular process
	-If inside that script runs another script and we want
	 the variable to be abailable for it we need to export
	 the variable

SUMMARY

	$1,$2..etc.
	Command line arguments to the script

	variable=value
	Sets the value for a varible (NO space befor or after the = )

	quotes " '
	Double accept variable subtitution, single will not

	variable=$(command)
	Saves the output of a command or program as a variable value

	export var1
	Makes var1 available to child processes

IMPORTANT CONCEPTS

	-Formatting
	 The presensce or absece of spaces or any caracter is important

	-Manageability
	 If any particular value is going to be used several times in a
	 script then store it in a variable makes it easier to manag makes it easier to manage
