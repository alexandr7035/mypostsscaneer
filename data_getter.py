import vk
import settings

try:
    from keys import vk_app_service_key
except Exception as e:
    print("Can't load key, exit.")
    print("\"" + str(e) + "\"")
    exit(1)


class PostsScanner():
    def __init__(self):

        # VK
        session = vk.Session()
        self.api = vk.API(session, v=settings.vk_api_version)

        
        
    
    def get_group_posts(self, group_link, user_id):
        
        print("GROUP LINK:", group_link)
        print("USER ID: ", user_id)
        
        group_name = group_link.split("/")[-1]

        
        all_posts = []
        user_posts = []

        data = self.api.wall.get(access_token=vk_app_service_key, 
                                v=settings.vk_api_version,
                                domain=group_name,
                                count=0)

        
        print("TOTAL POSTS: " + str(len(data['items'])))
        
        all_posts.extend(data['items'])

        #print(posts)

        for post in all_posts:
            try:
                if post["signer_id"] == user_id:
                    post_link = "vk.com/" + group_name + "?w=wall" + str(post["from_id"]) + "_" + str(post["id"])
                    user_posts.append(post_link)
            except KeyError:
                pass
        
        print("TOTAL USER POSTS: ", len(user_posts), "\n")
        print(user_posts)

        return user_posts
        
