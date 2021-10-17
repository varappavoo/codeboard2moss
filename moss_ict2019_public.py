#!/usr/bin/python3
####################################################################################################
###
### ORIGINAL SOURCE: https://github.com/soachishti/moss.py
### MODIFIED TO PREPROCESS FILE SUBMITTED BY STUDENTS FROM CODEBOARD.IO AND GOOGLECLASSROOM
###
####################################################################################################
import mosspy
from submissions_dir_files import *
from shutil import copyfile

organize_file=0
def get_proper_file_structure(path_and_filename):
	# CODEBOARD/project_162752_submissions_graph/xxxxxx1811939/480085/Root/src/Graph.java
	# GCLASSROOM/xxxxx1815917/BSTNode.java
	new_directory="MOSS/submissions/"
	path_and_filename_split = path_and_filename.split("/")
	if path_and_filename_split[0]=="CODEBOARD":
		username=path_and_filename_split[2]
		submissionid=path_and_filename_split[3]
		filename=path_and_filename_split[6]
	else:
		username=path_and_filename_split[1]
		submissionid="GCLASSROOM"
		filename=path_and_filename_split[2]
	new_filename=new_directory + username+"_"+submissionid+"_"+filename
	print(new_filename)
	return new_filename

def organize_file_for_submissions():
	for file in hashing_submissions_list:
		copyfile(file,get_proper_file_structure(file))
	for file in bst_submissions_list:
		copyfile(file,get_proper_file_structure(file))
	for file in graph_submissions_list:
		copyfile(file,get_proper_file_structure(file))
	for file in classroom_submissions_list:
		copyfile(file,get_proper_file_structure(file))

if(organize_file):
	organize_file_for_submissions()

userid = 123123123

m = mosspy.Moss(userid, "java")

m.addBaseFile("MOSS/base_files/base_graph_Test_Graph.java")
m.addBaseFile("MOSS/base_files/base_hashing_DistinctWords.java")
m.addBaseFile("MOSS/base_files/base_bst_BST.java")
m.addBaseFile("MOSS/base_files/base_bst_Test_BST.java")
m.addBaseFile("MOSS/base_files/base_hashing_SpellChecker.java")
m.addBaseFile("MOSS/base_files/base_hashing_Main.java")
m.addBaseFile("MOSS/base_files/base_graph_Graph.java")
m.addBaseFile("MOSS/base_files/base_bst_Main.java")
m.addBaseFile("MOSS/base_files/base_graph_Main.java")

# Submission Files
m.addFilesByWildcard("MOSS/submissions/*.java")

url = m.send() # Submission Report URL

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "MOSS/reports/report.html")

# Download whole report locally including code diff links
mosspy.download_report(url, "MOSS/reports/report/", connections=128)


