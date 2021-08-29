import urllib.request

opener = urllib.request.URLopener()
opener.addheader('Mozilla/5.0', 'Mark')
filename, headers = opener.retrieve("https://images.mobilism.org/?di=69SSS1AO", "abc.png");
