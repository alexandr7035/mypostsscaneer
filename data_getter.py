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

        
        
    
    def get_group_posts(self, group_link):
        
        print("GROUP LINK:", group_link)
        
        group_name = group_link.split("/")[-1]

        
        posts = []


        data = self.api.wall.get(access_token=vk_app_service_key, 
                                v=settings.vk_api_version,
                                domain=group_name,
                                count=0)

        
        print("TOTAL POSTS: " + str(len(data['items'])), "\n"*3)
        
        posts.extend(data['items'])

        print(posts)

        for post in posts:
            post_link = "vk.com/"

            post_link += group_name + "?w=wall" + str(post["from_id"]) + "_" + str(post["id"])
            print(post_link)


        return posts
        
