import vk

import data_getter


scanner = data_getter.PostsScanner()

data = scanner.get_group_posts("lftable")

print(data)