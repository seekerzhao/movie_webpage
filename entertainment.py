import media
import fresh_tomatoes

funnyVedio = media.Movie("funnyVedio", "a funny vedio",
			"http://img01.taopic.com/141002/240423-14100210124112.jpg",
			"https://www.youtube.com/watch?v=Xs0AupRWyC0")

MaGirl_1 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img5.imgtn.bdimg.com/it/u=900789529,877641406&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")

MaGirl_2 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img5.imgtn.bdimg.com/it/u=900789529,877641406&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
MaGirl_3 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img5.imgtn.bdimg.com/it/u=900789529,877641406&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
MaGirl_4 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img5.imgtn.bdimg.com/it/u=900789529,877641406&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")					
MaGirl_5 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img5.imgtn.bdimg.com/it/u=900789529,877641406&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
# print(funnyVedio.discription)
# print (MaGirl.discription)

# funnyVedio.openPoster()
# media.testFunction('I love you')

movies = [funnyVedio, MaGirl_1, MaGirl_2, MaGirl_3, MaGirl_4, MaGirl_5]
fresh_tomatoes.open_movies_page(movies)