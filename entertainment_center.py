# import fresh_tomatoes and media classes
import fresh_tomatoes
import media

# Initializing objects with arguments
friday = media.Movie("Friday", "A family  wake up one Friday morning and get ready for an average Friday of work and school until it changes.",
                    "http://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
                    "https://www.youtube.com/watch?v=dxduMVVnrvU")

a_few_good_men = media.Movie("A Few Good Men", "Court martial of two marines charged with a murder of a fellow marine",
                        "http://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                        "https://www.youtube.com/watch?v=ePo91pMcu94")

the_shawshank_redemption = media.Movie("The Shawshank Redemption", "A man convicted of his wife murder, successfully escape the Shawshank prison",
                    "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                    "https://www.youtube.com/watch?v=6hB3S9bIaco")

inception = media.Movie("Inception", "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                    "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                    "https://www.youtube.com/watch?v=66TuSJo4dZM")

office_space = media.Movie("Office Space", "Three company workers who hate their jobs and decide to rebel against their greedy boss.",
                    "http://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                    "www.youtube.com/watch?v=_IwzZYRejZQ")

goodfellas = media.Movie("GoodFellas", "Henry Hill and his friends work their way up through the mob hierarchy.",
                    "http://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

# Putting all objects in an array
movies = [friday, a_few_good_men, the_shawshank_redemption, inception, office_space, goodfellas]

#print (media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
                                
