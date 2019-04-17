# googler.py: takes command line 
# arguments and opens a google search
import webbrowser
import sys
search_terms = '+'.join(sys.argv[1:])

url = r'https://google.com/search?q=' + search_terms

print(url)
webbrowser.open(url)