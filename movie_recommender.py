import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,euclidean_distances


class MovieRecommender():
    def __init__(self,file_name="movie_dataset.csv",test_file="test.csv"):
        # get data from the given file and construct new feature for this data
        self.moviesdata = self.construct_data(file_name)
        self.test = self.construct_data(test_file)
        self.add_new_feature()


    def construct_data(self,file_name):
        # Read CSV File
        moviesdata = pd.read_csv(file_name)
        #Select Features
        features = ['keywords','cast', 'genres','director','title','vote_average']
        for feature in features:
            moviesdata[feature] = moviesdata[feature].fillna('')
        return moviesdata


    #concatanate features into a single string
    def concatanate_features(self,row):
        return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']+" "+row['title']+" "+str(row['vote_average'])


    #add new feature to all movies. New feature will be concatanete of the all available features
    def add_new_feature(self):
        self.moviesdata["combined_features"] = self.moviesdata.apply(self.concatanate_features, axis=1)
        self.test["combined_features"] = self.test.apply(self.concatanate_features, axis=1)


    def get_title(self,index):
        return self.moviesdata[self.moviesdata.index == index]["title"].values[0]

    def get_index(self,title):
        if len(self.test[self.test.title == title]) <1:
            return -1
        return self.test[self.test.title == title]["index"].values[0]

    ## Create count matrix from this new combined column
    def get_distance(self):
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(self.moviesdata["combined_features"])
        return cosine_similarity(count_matrix)

    def get_euclidean_distance(self):
        ##Create count matrix from this new combined column
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(self.moviesdata["combined_features"])
        # Compute the euclidean distance based on the count_matrix
        return euclidean_distances(count_matrix)


    def getKNN_euclidean(self,movie,K,movie_name):
        self.moviesdata = self.moviesdata.append(self.test[self.test.title == movie_name],ignore_index=True)
        self.distance = self.get_euclidean_distance()
        similar_movies_index = list(enumerate(self.distance[len(self.moviesdata)-1]))
        # sort row in descending order
        similar_movies_index = sorted(similar_movies_index, key=lambda x: x[1])
        # return similar movies
        return [self.get_title(similar_movies_index[i][0]) for i in range(1, K+1)]


    def getKNN_cosine(self,movie,K,movie_name):
        self.moviesdata = self.moviesdata.append(self.test[self.test.title == movie_name],ignore_index=True)
        print(self.moviesdata)
        self.distance = self.get_distance()
        print(self.distance)
        similar_movies_index = list(enumerate(self.distance[len(self.moviesdata)-1]))
        # sort row in descending order
        similar_movies_index = sorted(similar_movies_index, key=lambda x: x[1],reverse=True)
        # return similar movies
        return [self.get_title(similar_movies_index[i][0]) for i in range(1, K+1)]


    def movieRecommender(self,movie):
        # Get index of this movie from its title
        movie_index = self.get_index(movie)
        if movie_index == -1:
            return ["Movie could not found."]
        return self.getKNN_euclidean(movie_index,50,movie)
        #get row of given movie from cosine sim matrix

"""
a=MovieRecommender()
b=a.movieRecommender("Superman")
for i in range(len(b)):
    print(b[i])
"""