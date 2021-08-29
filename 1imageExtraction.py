from urllib.request import Request, urlopen

f = open("validURLS.txt", "r");
content = f.read();
urls = content.split("\n");

for url in urls:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    print(url);
    if "Winning numbers" in str(webpage):
        index = str(webpage).index("Winning numbers");
        url = str(webpage)[index:index+120];
        #print(url); break;
        ff = open("imageUrls.txt", "a");
        ff.write(url);
        ff.write("\n");
        ff.close();
    else:
        print("no image found");

