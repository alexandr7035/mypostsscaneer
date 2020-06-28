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

        data = self.get_group_posts("1")
        
    
    def get_group_posts(self, group_link):
        
        posts = []

        data = self.api.wall.get(access_token=vk_app_service_key, 
                                v=settings.vk_api_version,
                                domain="cotocat",
                                count=1)

        print("TOTAL POSTS: " + str(len(data['items'])), "\n"*3)

        posts.extend(data['items'])

        print(posts)

        return data
