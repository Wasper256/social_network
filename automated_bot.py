import requests
import os
import random
import json


BASE_URL = users = os.environ.get("BASE_URL", "http://127.0.0.1:8000/api/v1")


def read_rules():
    try:
        users = int(os.environ.get("NUMBER_OF_USERS"))
        posts = int(os.environ.get("MAX_POSTS_PER_USER"))
        likes = int(os.environ.get("MAX_LIKES_PER_USER"))
        return users, posts, likes
    except KeyError:
        print("Error! Check the rules and try again!")


def register_new_user():
    url = BASE_URL + '/registration/'
    payload = {
        "username": "user" + str(random.randint(1, 1000000000)),
        "email": "user" + str(random.randint(1, 1000000000)) + "@email.com",
        "password1": "qwerty123qwerty123",
        "password2": "qwerty123qwerty123",
        "first_name": "first_name" + str(random.randint(1, 1000000000)),
        "last_name": "last_name" + str(random.randint(1, 1000000000)),
        "date_of_birth": "2019-06-25",

    }
    response = requests.request("POST", url, data=json.dumps(payload),
                                headers={"Content-Type": "application/json"})
    print("New user created")
    return response.json()["token"]


def create_posts(token):
    url = BASE_URL + '/posts/'
    payload = {
        "title": ''.join(random.choice(token) for _ in range(50)),
        "content": ''.join(random.choice(token) for _ in range(200)),
    }
    requests.request("POST", url, data=json.dumps(payload),
                     headers={"Content-Type": "application/json",
                              "Authorization": "Bearer " + token})
    print("Post created")


def get_posts_list(token):
    url = BASE_URL + '/posts/'
    response = requests.request("GET", url,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer " + token})
    posts_list = []
    for i in response.json():
        posts_list.append(i.get("id"))
    print("Post list of len {} is extracted".format(len(posts_list)))
    return posts_list


def create_likes(token, posts_list):
    url = BASE_URL + '/like_post/' + str(random.choice(posts_list)) + "/"
    payload = {
        "like": True
    }
    requests.request("POST", url, data=json.dumps(payload),
                     headers={"Content-Type": "application/json",
                              "Authorization": "Bearer " + token})
    print("Post liked")


def main():
    number_of_users, max_posts_per_user, max_likes_per_user = read_rules()
    for i in range(number_of_users):
        token = register_new_user()
        for j in range(random.randrange(0, max_posts_per_user)):
            create_posts(token)
        posts_list = get_posts_list(token)
        for k in range(random.randrange(0, max_likes_per_user)):
            create_likes(token, posts_list)
    print("Job is finished!")



if __name__ == '__main__':
    main()