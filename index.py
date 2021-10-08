from flask import Flask
from instagramy import InstagramUser

app = Flask(__name__)

@app.route('/')
def main():
    return 'Api is working'


@app.route('/<string:username>')
def instagram(username):

    try:
        bio = InstagramUser(username).biography
        profile_pic =  InstagramUser(username).profile_picture_url
        followers =  InstagramUser(username).no_of_mutual_follower
        following =  InstagramUser(username).number_of_followings
        fullname =  InstagramUser(username).fullname
        is_private =  InstagramUser(username).is_private
        is_verified = InstagramUser(username).is_verified
        number_of_posts = InstagramUser(username).number_of_posts

        data = {
            "full name":fullname,
            "bio" : bio,
            "profile picture":profile_pic,
            "followers":followers,
            "following":following,
            "posts":number_of_posts,
            "is verified":is_verified,
            "is private":is_private     
        }
        return data

    except:
        return "error"



if __name__ == '__main__':
  app.run()
