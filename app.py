import vk

import data_getter

user_id = 188855048
group_link = 'lftable'

scanner = data_getter.PostsScanner()

data = scanner.get_group_posts(group_link, user_id)

