import re
import urllib
import urllib2


def main(args):
    response = urllib2.urlopen('http://www.pinkbike.com/photo/podlist')
    html = response.read()
    #shorthtml = re.findall(r'<ul class="uPhotoSmall">\s+?<div class="inElm" id="elm\d+">\s+?<li class="inElm" id="elm\d+.??style="width: 230px;">\s+?<a href="http://\w{3}\.pinkbike.com/photo/\d+/', html)
    shorthtml = re.findall(r'<a href="http\w?://www.pinkbike.com/photo/\d+', html)[0]
    #print shorthtml
    photoLink = shorthtml[9:]
    #print photoLink
    #photoLink = re.findall(r'http\w?://\w{3}.pinkbike.org/\w+?/\w+?\.jpg', shorthtml)[0]
    #print photoLink
    #photoLink = photoLink[0]
    photoPage = urllib2.urlopen(photoLink + "/?s6")
    photohtml = photoPage.read()
    photohtml = re.findall(r'//ep\d.pinkbike.org/\w+/\w+.jpg', photohtml)[0]
    #print photohtml
    photohtml = photohtml[:20] + "6" + photohtml[21:33] + "5" + photohtml[34:]
    #print photohtml
    photohtml = 'https:' + photohtml
    #photohtml = photohtml[9:]
    urllib.urlretrieve(photohtml, "/media/sf_VM/Code/Other/Python/Desktop_Changer/POD.jpg")
    return 0

if __name__ == '__main__':
    pass
    import sys
    sys.exit(main(sys.argv))
