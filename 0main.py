from urllib.request import Request, urlopen

main = "https://forum.mobilism.org/viewtopic.php?f=2&t=2020443"
second = "https://forum.mobilism.org/viewtopic.php?f=2&t=2020443&start=15"
start = "&start="
n = 15; #0, 15, 30, 45 etc
m = 4455;

urls = list();
for n in range(15, m+1, 15):
    url = main + start + str(n)
    urls.append(url)


progress = 0;


for url in urls:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    if "Winning numbers:" in str(webpage):
        f = open("validURLS.txt", "a");
        f.write(url);
        f.write("\n");
        f.close();
        print("valid", url);

    print(progress);
    progress += 1;
