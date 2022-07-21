import webbrowser

# webbrowser.open('https://www.python.org/', new=1)

# help(webbrowser)
chrome = webbrowser.get(using='chrome')
chrome.open_new('https://www.python.org/')