from urllib.request import Request, urlopen

f = open("imageUrls.txt", "r");
lines = f.readlines();

ff = open("onlyImageLinks.txt", "a");
for line in lines:
    a = line.index('"');
    s = line[a+1:];
    b = s.index('"');
    s = s[:b];
    #now s contains the link to the image

    ff.write(s);
    ff.write("\n");

    #progress indicator
    print(s);
    
ff.close();
