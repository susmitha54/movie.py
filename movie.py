############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like


movies=[]
common_movies=[]
same_movies=[]
for i in range(5):
    movie = input ("What movies you like:")
    movies.append(movie)
for movie in movies:        
    if(movie not in common_movies):
        common_movies.append(movie)
    else:    
        if(movie not in same_movies):
           same_movies.append(movie)  
print("movies:",movies)       
print("You both like:",same_movies)
