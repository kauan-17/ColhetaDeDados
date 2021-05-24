
import tweepy
import csv
import time
import json

consumer_key ="TEFoK4WWww6mCSsPodONNCOIF"
consumer_secret ="BDw6vAOjXoa2JxroVPxqf2NzZ6bo71hqRs3KBfTRHPWy6GUo4I"
access_token ="1160650651619213317-BlSZ0kzTik0qmWyLGcOEdq66JjjLUY"
access_token_secret ="zKdclgqI1VYXTAoA54naMZIhXku2Fz2U3GXAwMyAAzid9"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

arq = csv.writer(open("base_teste.csv", "w", encoding='utf-8'))
arq2 = open("base_teste_json.json", "w", encoding='utf-8')
row = []

statuses = tweepy.Cursor(api.search, q="#flamengo", since='2019-10-19', until='2019-10-21', lang='pt').items()

while True:
    try:
        for status in statuses:
            print (status._json)
            # Salvando o JSON
            arq2.write(json.dumps(status._json))
            arq2.write("\n")
    except tweepy.TweepError:

        print("wait 15 minutes...")
        time.sleep(60 * 15)
        continue
    except StopIteration:
        print("Acabou!!")
        break
    except Exception as e:
        print(e)


