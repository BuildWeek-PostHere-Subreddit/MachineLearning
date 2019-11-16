import pandas as pd
import praw
​
redd = praw.Reddit(client_id='632ZdOOH5hzFAA', client_secret='jwVjywvA6SeVMI_C5n6hVDr5iMI', username='matthewlsessions', password='', user_agent='testagent')
​
df = pd.read_csv('subreddit_namesn.csv')
​
def df_range(mindf,maxdf, df):
    req_list = df.values[mindf:maxdf].tolist()
    return(req_list)
​
names = df_range(0, 4990, df)
​
df = pd.DataFrame([], columns=['name', 'title', 'url', 'banner_url', 'subscribers', 'active_accounts', 'score', 'text'])
​
​
counter = 0
for i in names:
    name = i[0]
    sub = redd.subreddit(name)
    title = sub.title
    url = sub.url
    banner_url = sub.banner_img
    subscribers = sub.subscribers
    active_accounts = sub.accounts_active
    score = 0
    data = sub.hot(limit=1000)
    text = ''
    for words in data:
        text = text + words.title
        score = score + words.score
    dfa = pd.DataFrame([[name, title, url, banner_url, subscribers, active_accounts, score, text]], columns=['name', 'title', 'url', 'banner_url', 'subscribers', 'active_accounts', 'score', 'text'])
    df = df.append(dfa)
    if counter % 20 == 0:
        print(f'Call {counter} of 4990')
    counter = counter + 1
    df.to_csv('all_data.csv')
