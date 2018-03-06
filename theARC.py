#Jacob Pawlak
#February 25th, 2018
#Go Blue Team!

import os, glob

#list of song titles
song_titles = []
#list of album titles
album_titles = []
#whole dictionary that will get turned into a json file
ARC = {}

def clean_files():

	#change the current directory to 'Albums'
	os.chdir("Albums")
	#grab a list of all the subdirectories (of Albums)
	subds = os.listdir()

	#for each of the aesop rock albums (subdirectory in subdirectories)
	for subd in subds:
		#change the current directory to the album subdirectory
		os.chdir(subd)
		print("\t" + subd)
		#if the album title is not in the list of album titles, add it
		if subd not in album_titles:
			album_titles.append(subd)
		#for each song (file will look like Blah.song)
		for file in glob.glob("*.song"):
			print(file)
			#if the song is not yet in the list of songs, add it
			if file[:-5] not in song_titles:
				song_titles.append(file[:-5])
		#go up a directory for the loop
		os.chdir("..")

	return

def cf_helper_open(song_file):


	return

def main():

	#scan in and clean the files
	clean_files()
	print()
	print(song_titles)
	print()
	print(len(song_titles))
	print()
	print(album_titles)
	print()
	print(len(album_titles))
	print()

main()
