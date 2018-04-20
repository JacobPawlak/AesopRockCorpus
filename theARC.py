#Jacob Pawlak
#February 25th, 2018
#Go Blue Team!


################################ IMPORTS ################################



#get the nltk library
import nltk
#Use OS and glob library to move through the computer's filesystem
import os
import glob
#To convert the ARC dictionary into a JSON object
import json



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

#dictionary of hapax legomenon, sorted by song/album
hapax_legomena = {}

#longest word(s) because Why not, i'm sure it will be interesting.
longest_word = {}



################################ HELPER-FUNCTIONS ################################



#Helper function to insert the albums and songs entry into the ARC
def arc_helper_albums():

	ARC['albums_with_songs'] = albums

	return


#Helper function to insert the list_of_words into the ARC
def arc_helper_list_of_words():

	ARC['list_of_words'] = list_of_words

	return


#Helper function to insert the nltk_list_of_words into the ARC
def arc_helper_nltk_list_of_words():

	ARC['nltk_list_of_words'] = nltk_list_of_words

	return


#Helper function to insert the nltk_list_of_words into the ARC
def arc_helper_hapax_legomena():

        ARC['hapax_legomena'] = hapax_legomena

        return


#Helper function to insert the longest_word dict into the ARC
def arc_helper_longest_word():

        ARC['longest_word'] = longest_word

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

				#break the songs down to tokenized words and add them to the list of words
				open_file = open(file, 'r')
				for line in open_file:
					if line != "\n":
						print("LINE")
						print(line[:-1])
						tokens = nltk.word_tokenize(line)
						tokenss = []
						print("TOKENS")
						print(tokens)
						print("TAGGED TOKENS")
						print(nltk.pos_tag(tokens))
						#starting to clean the unwanted symbols and stuff out
						bad_tokens = ['(', ')', '[', ']', '{', '}', '`', '\"']
						for token in tokens:
							#look at the first character
							first_char = token[:1]
							#while it is bad, delete it and look at the new first character
							while first_char in bad_tokens:
								token = token[1:]
								first_char = token[:1]
							tokenss.append(token)
						#cleaning the empty strings out now with list comprehension
						tokensss = [t for t in tokenss if t]
						tokenssss = [t for t in tokensss if t != "\'\'"]
						print("CLEANED TOKENSSS")
						print(tokensss)
						print("TAGGED TOKENSSS")
						print(nltk.pos_tag(tokensss))
						print("TOKENSSSS")
						print(tokenssss)

				open_file.close()

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


#Function to look through the nltk_list_of_words and pick out the single occurrence words
def find_hapax_legomena():

	print()

	return


#Combs through the nltk_list_of_words and picks out the longest word(s)
def find_longest_word():

	print()

	return


#You know what it is. Fill. The. ARC.
def fill_the_arc():

	arc_helper_albums()
	arc_helper_list_of_words()
	arc_helper_nltk_list_of_words()
	arc_helper_hapax_legomena()
	arc_helper_longest_word()

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
