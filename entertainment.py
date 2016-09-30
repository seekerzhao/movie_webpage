import media
import fresh_tomatoes

funnyVedio = media.Movie("funnyVedio", "a funny vedio",
			"http://img01.taopic.com/141002/240423-14100210124112.jpg",
			"https://www.youtube.com/watch?v=Xs0AupRWyC0")

MaGirl_1 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://img1.imgtn.bdimg.com/it/u=4002825267,2389293098&fm=11&gp=0.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")

MaGirl_2 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://wh.yesky.com/uploadImages/upload/20160924/sbe5cpfwludjpg.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
MaGirl_3 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://upload.jxntv.cn/2016/0812/1470965214544.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
MaGirl_4 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://www.1fanyi.com/data/attachment/forum/201608/17/230211ko7gpttpe6eqgces.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")					
MaGirl_5 = media.Movie("MaLong", "Ma long's beautiful girlfriend",
					"http://picture.youth.cn/xwjx/201608/W020160812353741177087.jpg",
					"https://www.youtube.com/watch?v=Xs0AupRWyC0")
# print(funnyVedio.discription)
# print (MaGirl.discription)

# funnyVedio.openPoster()
# media.testFunction('I love you')
print(media.Movie.VALID_STRINGS)

movies = [funnyVedio, MaGirl_1, MaGirl_2, MaGirl_3, MaGirl_4, MaGirl_5]
fresh_tomatoes.open_movies_page(movies)
