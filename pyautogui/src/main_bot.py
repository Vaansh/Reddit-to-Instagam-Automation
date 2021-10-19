from PIL import Image
import instagram_script
import credentials
import save_resize_image
import time

username = credentials.IGusername
password = credentials.IGpassword
instagram_script.logintoig(username, password)

filePath = ""  # Example: /Users/name/Desktop/folder/pictures/'

hashtags = ""
subreddit = credentials.reddit.subreddit("")  # Subreddit name
post = 7200  # Frequency of post; in seconds
urlPosted = []  # Avoid redundant posts

# num of rounds can be decided here
currenpost = 1
numposts = 100

while currenpost <= numposts:  # num of rounds can be decided here
    for submission in subreddit.hot(limit=25):
        url = submission.url
        fileName = str(submission)
        fullPath = filePath + fileName + ".png"
        title = '"' + str(submission.title) + '"'
        credit = "(Via: u/" + str(submission.author) + " on Reddit)"
        caption = title + "\n" + "\n" + credit + "\n" + "\n" + "\n" + hashtags

        if (url.endswith("jpg") or url.endswith("png")) and (not url in urlPosted):  # Post bounds can be set here
            try:
                urlPosted.append(url)
                save_resize_image.saveImage(url, filePath, fileName, currenpost)
                save_resize_image.correctShape(fullPath, fileName, filePath, currenpost)
                finalImgPath = fileName + str(currenpost) + "final.jpg"

                fullFinalImgPath = filePath + finalImgPath
                instagram_script.uploadtoig(
                    fullPath=fullFinalImgPath, caption=caption, post=post
                )  # make sure caption has no emojis

                subreddit = credentials.reddit.subreddit("")  # Subreddit name; refresh reddit
                currenpost = currenpost + 1
            except:
                print("cant be posted, next...")
                continue
        else:
            continue
