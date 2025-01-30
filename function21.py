# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def rate(moviee):
    for x,y in moviee.items():
        if x=="imdb" and y>5.5:
            return True
    return False
for i in range(len(movies)):
    rating=rate(movies[i])
    if(rating==True):
        print(f"{i+1}){rating}")


def rate(moviee):
    for x,y in moviee.items():
        if x=="imdb" and y>5.5:
            return True
    return False
for i in range(len(movies)):
    rating=rate(movies[i])
    if(rating==True):
        print(movies[i]["name"])

print("\n")
def rate(moviee,categories):
    for x in moviee:
        if moviee[x]==categories:
            return True
    return False
for i in range(len(movies)):
    rating=rate(movies[i],"Romance")
    if(rating==True):
        print(movies[i]["name"])



def rate(moviee):
    count=float(0)
    count1=int(0)
    for i in range(len(moviee)):
        count+=moviee[i]["imdb"]
        count1+=1
            
    return count/count1
rating=rate(movies)
print(rating)

def rate(moviee,categories):
    count=float(0)
    count1=int(0)
    for i in range(len(moviee)):
        if moviee[i]["category"]==categories:
            count+=moviee[i]["imdb"]
            count1+=1
            
    return count/count1
rating=rate(movies,"Romance")
print(rating)
    