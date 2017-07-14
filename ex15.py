from sys import argv    #argv prompts you to input something along with the python execution line. sys is a package
#and argv is a feature in that package

script, filename = argv #assigns the input to a variable (in this case the file name)

txt = open(filename) #open the file and assign the content to a variable named txt

print "Here's your file %r:" %filename #print "here is your file" along with the file name
print txt.read() #print the content of txt

print "Type the filename again"  #prompt user to input the filename again upon prompting
file_again = raw_input("> ") #allow user to enter the file name

txt_again = open(file_again) #assign the file content to txt_again

print txt_again.read()  #print the content of txt_again
