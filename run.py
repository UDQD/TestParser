import requests as rq

albumid = 1
photoid = 1

data_posts = rq.get('https://jsonplaceholder.typicode.com/posts').json()
data_users = rq.get('https://jsonplaceholder.typicode.com/users').json()
data_photos = rq.get(f'https://jsonplaceholder.typicode.com/photos?albumId={albumid}').json()

total_info = {}

for user in data_users:
    total_info[user['id']] = {'name': user['name']}
    posts_list = []
    posts_titles = []
    for post in data_posts:
        if post['userId'] == user['id']:
            posts_list.append(str(post['id']))
            posts_titles.append(post['title'])
    total_info[user['id']]['posts'] = posts_list
    for i in range(len(posts_list)):
        total_info[user['id']][i] = [posts_list[i], posts_titles[i]]

for num in range(1, len(total_info) + 1):
    file_name = "user_" + str(num) + ".txt"
    file = open(file_name, "w")
    file.write(f"{num}: {total_info[num]['name']}\n")
    file.write(f"""{", ".join(total_info[num]['posts'])}\n""")
    for i in range(len(total_info[num]['posts'])):
        file.write(f"{total_info[num][i][0]}: {total_info[num][i][1]}\n")
    file.close()

url = ''
for e in data_photos:
    if e['id'] == photoid:
        url = e['url']
        break

p = rq.get(url)
out = open("img.jpg", "wb")
out.write(p.content)
out.close()
