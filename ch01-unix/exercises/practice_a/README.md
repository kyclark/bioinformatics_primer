# Unix Exercises

For this exercise, you will create a "files" directory. In there, create a file called "answers.txt" and cut/paste in the commands that you create along with the output. When you are finished, do the following:

    $ git add files
    $ git commit -m 'all done' files
    $ git push

* Make a directory (in this directory) called "files" and download the following files in there:
	* Download the following using their existing filenames (i.e., you will have "usdeclar.txt", etc.):
		* https://www.constitution.org/usdeclar.txt
		* https://www.usconstitution.net/const.txt
	* Download https://www.gutenberg.org/files/25344/25344-0.txt as "scarlet.txt" (in one line, i.e., do not download and then rename -- how can you specify the download filename?)
* Show a long listing of the files
* Show a command to count the number of lines in each file and a total count of all lines
* Show a command that will find the files in this directory which are larger than 50k
* Show a command that will tell you what kind of file that Unix considers "const.txt"
* Show a single command that will print the MD5 sum of all the text files (without mentioning each file individually)
* Show the output of a command that will tell you how much disk space in kilobytes (K) is being used
* Show a command to count how many lines of text contain the word "judge" (irrespective of case) in all the files
* Show a command that will display only the names of the files that contain the word "human" 
* Show a single command that will count the number of times the word "scarlet" appears in "scarlet.txt" (case-insensitive); that is, not the number of lines that contain "scarlet" but each occurrence of the word
* Show a single command that will take the first 15 lines from each file and append them into a new file called "foo"
* Show a command that shows how many lines are in "foo"
* You might have expected that the total number of lines in the previous question would be 45 (15 * 3), but it should not be. Why is it more or less?
* Remove the file called "foo"
* Do "history > cmds"
* "git add -A files" and then commit and push. Ensure you can see your new files on Github.

