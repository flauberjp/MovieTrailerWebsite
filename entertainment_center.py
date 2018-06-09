import fresh_tomatoes
import media

john_wick = media.Movie("John Wick",
                        181,
                        "An ex-hitman comes out of retirement to track down the gangsters that took everything from him. With New York City as his bullet-riddled playground, JOHN WICK (Keanu Reeves) is a fresh and stylized take on the 'assassin genre'.",
                        "https://vignette.wikia.nocookie.net/john-wick8561/images/2/29/John_Wick_Poster_003.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
#print(john_wick.storyline)
avatar = media.Movie("Avatar",
                     221,
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     "https://www.topteny.com/wp-content/uploads/2015/02/poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
the_300_spartans = media.Movie(
    "300",
    150,
    "300 spartans to defend their home land against the conqueror Xerxes and his horde of millions soldiers",
    "https://www.movieposter.com/posters/archive/main/46/MPW-23465",
    "https://www.youtube.com/watch?v=UrIbxk7idYA")
#the_300_spartans.show_trailer()

gattaca = media.Movie(
    "Gattaca",
    148,
    "Is a humam being determined by the DNA?",
    "https://images-na.ssl-images-amazon.com/images/I/51QM82SNT3L.jpg",
    "https://www.youtube.com/watch?v=hWjlUj7Czlk")

matrix = media.Movie(
    "Matrix",
    150,
    "Machines dominated the humans, transformed them in batteries, is that true? Why we allowed it?",
    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")


the_godfather = media.Movie(
    "The Godfather",
    94,
    "See how italian mafia works",
    "http://img.goldposter.com/2015/04/The-Godfather_poster_goldposter_com_2.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

braveheart = media.Movie(
    "BRAVEHEART",
    174,
    "When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt against King Edward I of England.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSnnenelmzF4MKdtHBnaQYbDstLRExO1brKmrTBe_Ve40Vwq_lO",
    "https://www.youtube.com/watch?v=qDGjf3OZhKc")    

rocky = media.Movie(
    "Rocky",
    139,
    "A small time boxer gets a once-in-a-lifetime chance to fight the heavyweight champ in a bout in which he strives to go the distance for his self-respect.",
    "https://images-na.ssl-images-amazon.com/images/I/61NNabHp%2BsL._SY879_.jpg",
    "https://www.youtube.com/watch?v=3VUblDwa648")    



the_last_of_mohicans = media.Movie(
    "THE LAST OF THE MOHICANS",
    112,
    "The last members of a dying Native American tribe, the Mohicans -- Uncas, his father Chingachgook, and his adopted half-white brother Hawkeye -- live in peace alongside British colonists. But when the daughters of a British colonel are kidnapped by a traitorous scout, Hawkeye and Uncas must rescue them in the crossfire of a gruesome military conflict of which they wanted no part: the French and Indian War.",
    "http://www.mubis.es/media/users/8232/58254/el-ultimo-mohicano-para-cuando-original.jpg",
    "https://www.youtube.com/watch?v=IAqLKlxY3Eo")    

the_lord_of_the_rings = media.Movie(
    "The Lord of the Rings",
    175,
    "In a small village in the Shire a young Hobbit named Frodo (Elijah Wood) has been entrusted with an ancient Ring. Now he must embark on an epic quest to the Cracks of Doom in order to destroy it.",
    "https://wtfbabe.files.wordpress.com/2012/09/the-lord-of-the-rings-fellowship-of-the-rings.jpg",
    "https://www.youtube.com/watch?v=dn7UHJLcPp4")    

movies =[john_wick, avatar, the_300_spartans, gattaca, matrix, the_godfather, braveheart, rocky, the_last_of_mohicans, the_lord_of_the_rings]

def main():
    """Funcao principal da aplicacao. """
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
    



