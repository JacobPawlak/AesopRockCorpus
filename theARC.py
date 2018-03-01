#Jacob Pawlak
#February 25th, 2018
#Go Blue Team!

import os, glob


song_titles = []
album_titles = []
albums = {}


def clean_files():
	os.chdir("Albums")
	subds = os.listdir()

	for subd in subds:
		os.chdir(subd)
		print("\t" + subd)
		album_titles.append(subd)
		for file in glob.glob("*.song"):
			print(file)
			song_titles.append(file[:-5])
		os.chdir("..")


def main():

	clean_files()
	print(song_titles)
	print(album_titles)

main()
