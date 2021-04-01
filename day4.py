import os
import requests


def IsItDown():
    print(
        "Wecome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separted by comma)"
    )
    URLs = input()
    URL = URLs.lower().split(',')
    for n in URL:
        if ".com" not in n:
            print(f"{n} is not a valid URL")
        else:
            try:
                url = n.strip().replace("http://", "")
                URL_code = requests.get(f"http://{url}")
                if URL_code.status_code == 200:
                    print(f"http://{url} is up")
            except:
                print(f"http://{url} is down!")
    restart()
    return


def restart():
    print("Do you want to start over? y/n")
    answer = input().lower()
    if answer == "y":
        os.system('clear')
        IsItDown()
    elif answer == "n":
        print("k. bye!")
        return
    else:
        print("That's not a valid answer.")
        restart()


IsItDown()
