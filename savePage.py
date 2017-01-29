import os, optparse
import csv, time
from simulateKeydown import *

def parse_args():
    usage = '''usage: %prog [options] arg1 args
                python savePage.py -i website.csv
                or
                python savePage.py -w http://www.python.org
            '''
    parser = optparse.OptionParser(usage)
    parser.add_option("-i", "--in", dest="inputFile", help="the input csv file")
    parser.add_option("-u", "--url", dest="website", help="the website to be saved")

    #curPath = os.path.split(os.path.abspath(__file__))[0]
    #parser.add_option("-d", "--dest", dest="destPath", default=curPath, help="the path to be saved")

    (option, args) = parser.parse_args()

    if option.inputFile and option.website:
        parser.error("more than one website args")

    if option.inputFile is None and option.website is None:
        parser.error("no website args")

    return option, args

def readCSV(filename):
    urls = []
    with open(filename, "rb") as file:
        reader = csv.reader(file)
        for row in reader:
            urls.append(row[0])
    return urls

def openBrowser(urls):
    from selenium import webdriver
    driver = webdriver.Chrome("chromedriver.exe")

    for url in urls:
        driver.get(url)
        time.sleep(0.5)
        savePage(url)
        time.sleep(0.5)
    driver.close()

def savePage(url):

    # simulate ctrl+s
    SendInput(Keyboard(VK_CONTROL), Keyboard(KEY_S))
    time.sleep(0.2)
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP),
              Keyboard(KEY_S, KEYEVENTF_KEYUP))
    time.sleep(0.2)

    os.system("setTextAndClick.exe " + url[7:] + ".html")
    time.sleep(0.5)


if __name__ == '__main__':
    option, args = parse_args()
    if option.inputFile:
        urls = readCSV(option.inputFile)
    elif option.website:
        urls = []
        urls.append(option.website)
    openBrowser(urls)