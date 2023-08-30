import json
import sys


def getTweets():
    f = open('Tweets.json')
    data = json.load(f)
    f.close()
    return data["tweets"]


def getMostLikedOfUser(user_tweets):
    mostLiked = {
        "username": "",
        "content": "",
        "likes": 0
    }

    for tweet in user_tweets["tweets"]:
        if tweet["likes"] >= mostLiked["likes"]:
            mostLiked["username"] = user_tweets["username"]
            mostLiked["content"] = user_tweets["content"]
            mostLiked["likes"] = user_tweets["likes"]

    return mostLiked


def mostLikableTweet():
    tweets = getTweets()

    mostLiked = {
        "username": "",
        "content": "",
        "likes": 0
    }

    for tweets_per_user in tweets:
        most_liked_for_user = getMostLikedOfUser(tweets_per_user)

        if most_liked_for_user["likes"] >= mostLiked["likes"]:
            mostLiked = most_liked_for_user

    print(f'"username": {mostLiked["username"]}')
    print(f'"content": {mostLiked["content"]}')
    print(f'"likes": {mostLiked["likes"]}')


def get_sum_of_likes_per_user(user_tweets):
    likes_sum = 0
    for tweet in user_tweets["tweets"]:
        likes_sum += tweet["likes"]

    return likes_sum


def mostLikesPerUser():
    tweets = getTweets()

    mostLikedUser = {
        "username": "",
        "totalLikes": 0
    }

    for tweets_per_user in tweets:
        if get_sum_of_likes_per_user(tweets_per_user) >= mostLikedUser["totalLikes"]:
            mostLikedUser["username"] = tweets_per_user["username"]
            mostLikedUser["totalLikes"] = tweets_per_user["totalLikes"]

    print(f'"username": {mostLikedUser["username"]}')
    print(f'"mostLikedUser": {mostLikedUser["totalLikes"]}')


if __name__ == "__main__":
    if sys.argv[1] == "a":
        mostLikableTweet()
    elif sys.argv[1] == "b":
        mostLikesPerUser()
