from content_selection import ret_html
import json
x,y=ret_html('/var/www/html/posts/your_posts_1.json')
print(json.dumps([{'url': url, 'timestamp': timestamp} for url, timestamp in zip(x, y)]))
#print(x)
#print(y)
