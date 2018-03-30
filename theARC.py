#Jacob Pawlak
#February 25th, 2018
#Go Blue Team!


################################ IMPORTS ################################



import nltk
import os, glob



################################ GLOBAL VARIABLES ################################



#list of song titles
song_titles = []

#list of album titles
album_titles = []

#dictionary of albums and their songs
albums = {}

#whole dictionary that will get turned into a json file
ARC = {}

#dictionary of words (not the NLTK Token list) this list does not include the part of speech or anything like that, just the word count
list_of_words = {}

#dictionary of tenkenized words (includes POS, count, and other data?)
nltk_list_of_words = {}



################################ HELPER-FUNCTIONS ################################



#Helper function to insert the albums and songs entry into the ARC
def arc_helper_albums():

	ARC['albums_with_songs'] = albums

	return

#Helper function to open the song file and scan inside of it
def cf_helper_open(song_file):

	print()

	return



################################ SUB-FUNCTIONS ################################



#Function that searches the project directory for the albums and songs that I have scraped from the ol' internet
def clean_files():

	#change the current directory to 'Albums'
	os.chdir("Albums")

	#grab a list of all the subdirectories (of Albums)
	subds = os.listdir()

	#for each of the aesop rock albums (subdirectory in subdirectories)
	for subd in subds:

		#change the current directory to the album subdirectory
		os.chdir(subd)
		#print("\t" + subd)

		#if the album title is not in the list of album titles...
		if subd not in album_titles:
			#add it
			album_titles.append(subd)

		#make a temp list to be used in the albums dict
		songs = []

		#for each song (file will look like Blah.song)
		for file in glob.glob("*.song"):
			#print(file)

			#add the song to the list of songs for this album
			songs.append(file[:-5])

			#if the song is not yet in the list of songs...
			if file[:-5] not in song_titles:
				#add it
				song_titles.append(file[:-5])

		#add this album's songs to the albums dict
		albums[subd] = songs
		#print(albums)

		#go up a directory for the loop
		os.chdir("..")

	return

#Function to fill the list_of_words dictionary (this till not split by part of speech, just the tokens
def fill_list_of_words():

	print()

	return


#Function to fill the nltk_list_of_words dictionary, this will tokenize and pic part of speech for each word
def fill_nltk_list_of_words():

	print()

	return


#You know what it is. Fill. The. ARC.
def fill_the_arc():

	arc_helper_albums()

	return



################################ MAIN-FUNCTION ################################



def main():

	#scan in and clean the files
	clean_files()
	print()
	#print(song_titles)
	print()
	#print(len(song_titles))
	print()
	#print(album_titles)
	print()
	#print(len(album_titles))
	print()

	#fill the ARC, starting with albums
	fill_the_arc()
	print()
	print("The ARC: \n")
	print(ARC)

main()
