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
#{
#	"word": count, "word": count, etc
#}

#dictionary of tenkenized words (includes POS, count, and other data?)
nltk_list_of_words = {}
#{
#	"word/pos": {"word": WORD, "pos": POS, "count": count }
#}

#dictionary of hapax legomenon, sorted by song/album
hapax_legomena = {}
#{
#	"word": "song", "word": "song", etc
#}

#longest word(s) because Why not, i'm sure it will be interesting.
global longest_word
#{
#	"word": count, "word": count, etc
#}



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

        ARC['longest_word'] = find_longest_word()

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
						#print("LINE")
						#print(line[:-1])
						tokens = nltk.word_tokenize(line)
						tokenss = []
						#print("TOKENS")
						#print(tokens)
						#print("TAGGED TOKENS")
						#print(nltk.pos_tag(tokens))
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
						#getting rid of the other non-empty empty string string
						tokenssss = [t for t in tokensss if t != "\'\'"]
						#all of the following are just for debug
						#print("CLEANED TOKENSSS")
						#print(tokensss)
						#print("TAGGED TOKENSSS")
						#print(nltk.pos_tag(tokensss))
						#print("TOKENSSSS")
						#print(tokenssss)
						#print(nltk.pos_tag(tokenssss))

						cleaned_tokens = tokenssss
						fill_list_of_words(cleaned_tokens)

						cleaned_tokens_pos = nltk.pos_tag(cleaned_tokens)
						fill_nltk_list_of_words(cleaned_tokens_pos)

						#IMPORTANT: tokenssss is the cleaned list, sorry that you had to read all of the tokenssss variations,
						#	but you know how Python is with those immutable lists


				open_file.close()

		#add this album's songs to the albums dict
		albums[subd] = songs
		#print(albums)

		#go up a directory for the loop
		os.chdir("..")

	os.chdir("..")

	return


#Function to fill the list_of_words dictionary (this till not split by part of speech, just the tokens
def fill_list_of_words(tokens):

	for token in tokens:
		if token.lower() not in list_of_words.keys():
			list_of_words[token.lower()] = 1
		else:
			list_of_words[token.lower()] += 1

	return


#Function to fill the nltk_list_of_words dictionary, this will tokenize and pic part of speech for each word
def fill_nltk_list_of_words(tokens):

	for token in tokens:
		temp_dict = { token[0]: token[1]}
		temp_key = str(token[0]) + "/" + str(token[1])
		if temp_key not in nltk_list_of_words.keys():
			nltk_list_of_words[temp_key] = {"word": token[0], "pos": token[1], "count": 1 }
		else:
			nltk_list_of_words[temp_key]["count"] += 1

	return


#Function to look through the nltk_list_of_words and pick out the single occurrence words
def find_hapax_legomena():

	for word in nltk_list_of_words.keys():
		if nltk_list_of_words[word]["count"] == 1:
			hapax_legomena[word] = 1

	return


#Combs through the nltk_list_of_words and picks out the longest word(s)
def find_longest_word():

	longest_word = {"a": 1}

	for word in list_of_words.keys():
		if len(word) > len(list(longest_word.keys())[0]):
			longest_word = { word: list_of_words[word] }
		elif len(word) == len(list(longest_word.keys())[0]):
			longest_word[word] = list_of_words[word]

	return longest_word


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
	find_hapax_legomena()
	#longest_word = find_longest_word()
	#fill the ARC, starting with albums
	fill_the_arc()
	#print out the ARC in dictionary form
	print("The ARC: \n")
	print(ARC)
	print("#Words total")
	print(len(nltk_list_of_words))
	print("#Hapax")
	print(len(hapax_legomena))
	print("Longest word")
	print(list(ARC["longest_word"].keys())[0])

	json_file = open("the_ARC.json", 'w')
	json_file.write(str(ARC))
	json_file.close()

	#transform the dictionary into the JSON object the_ARC.json

main()
