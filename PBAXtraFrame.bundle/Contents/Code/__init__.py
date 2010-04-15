# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *
import Cookie

####################################################################################################

VIDEO_PREFIX = "/video/pbaxtraframe"
PLUGIN_NAME = L('PBAXtraFrame')
PLUGIN_REVISION = 0.1
PLUGIN_UPDATES_ENABLED = True
DEBUG_XML_RESPONSE = False
REFRESH_RATE = 5
CACHE_INTERVAL = 1800
WEBROOT = "http://xtraframe.pba.com"

NAME = L('Title')

# XPath Locations
# categories:	//ul[@class='nav-left'][1]//a/@href
# title: 		//div[@id='video-list']//span[@class='video-thumb-title']
# video_id: 	//div[@id='video-list']//span[@class='video-thumb-title']/a/@href
# img:			//div[@id='video-list']//img
# date: 		//div[@id='video-list']//span[@class='video-thumb-date']
# description:	//div[@id='video-list']//div
# url: 			http://xtraframe.pba.com/Default.aspx<video_id>

# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART           = 'art-default.jpg'
ICON          = 'icon-default.jpg'

####################################################################################################

def Start():

    ## make this plugin show up in the 'Video' section
    ## in Plex. The L() function pulls the string out of the strings
    ## file in the Contents/Strings/ folder in the bundle
    ## see also:
    ##  http://dev.plexapp.com/docs/mod_Plugin.html
    ##  http://dev.plexapp.com/docs/Bundle.html#the-strings-directory
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, L('VideoTitle'), ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    ## set some defaults so that you don't have to
    ## pass these parameters to these object types
    ## every single time
    ## see also:
    ##  http://dev.plexapp.com/docs/Objects.html
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)

# see:
#  http://dev.plexapp.com/docs/Functions.html#CreatePrefs
#  http://dev.plexapp.com/docs/mod_Prefs.html#Prefs.Add
def CreatePrefs():
    Prefs.Add(id='username', type='text', default='', label='Username')
    Prefs.Add(id='password', type='text', default='', label='Password', option='hidden')

# see:
#  http://dev.plexapp.com/docs/Functions.html#ValidatePrefs
def ValidatePrefs():
    loginCheck = SignIn()

    if(loginCheck == True):
        return MessageContainer(
            "Success",
            "Username and Password Accepted!"
        )
    else:
        return MessageContainer(
            "Error",
            "Invalid Username and Password"
        )

#### the rest of these are user created functions and
#### are not reserved by the plugin framework.
#### see: http://dev.plexapp.com/docs/Functions.html for
#### a list of reserved functions above

#
# Example main menu referenced in the Start() method
# for the 'Video' prefix handler
#

def MainMenu():
    # Container acting sort of like a folder on
    # a file system containing other things like
    # "sub-folders", videos, music, etc
    # see:
    #  http://dev.plexapp.com/docs/Objects.html#MediaContainer
    dir = MediaContainer(viewGroup="InfoList")
    dir.Append(Function(DirectoryItem(NewVideos,"New Videos",summary="LIVE Streaming Qualifying and Match Play for Every Tournament",thumb=R(ICON),art=R(ART))))
    dir.Append(Function(DirectoryItem(Telecasts,"Telecasts",summary="PBA Tour is the major professional tour for ten-pin bowling, operated by the Professional Bowlers Association",thumb=R('icon-tour.png'),art=R(ART))))
    dir.Append(Function(DirectoryItem(Interviews,"Interviews",summary="Behind the Scenes Features on the Lumber Liquidators PBA Tour",thumb=R(ICON),art=R(ART))))
    dir.Append(Function(DirectoryItem(Productions,"Xtra Frame Productions",summary="Exclusive Productions provided only from Xtra Frame",thumb=R(ICON),art=R(ART))))
    dir.Append(Function(DirectoryItem(Archives,"Archived Tournament Action",summary="Product Spotlights from PBA Product Registered Companies",thumb=R(ICON),art=R(ART))))
    dir.Append(Function(DirectoryItem(Tips,"Tips and Equipment",summary="Bowling tips and guides to help you bowl better and improve your game and win",thumb=R(ICON),art=R(ART))))
    
    dir.Append(PrefsItem(title="Preferences...",summary="Setup Xtra Frame Username and Password",thumb=R('icon-prefs.png')))
	
    return dir

def NewVideos(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("New")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir
	
def Interviews(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("Interviews")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir
	
def Telecasts(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("Telecasts")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir
	
def Productions(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("Productions")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir
	
def Archives(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("Archives")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir

def Tips(sender):
    dir = MediaContainer(viewGroup="InfoList")
    list = GetVideoList("Tips")
    for i in range(len(list)):
	    PMS.Log(list[i])
	    dir.Append(WebVideoItem(list[i][0], title=list[i][1], subtitle=list[i][2], summary=list[i][3], thumb=list[i][4]))
    if len(dir) == 0: return MessageContainer("No items available", "There are no items available.")
    return dir

def GetVideoList(cat):
    loginCheck = SignIn()
    if (loginCheck != True):
	    PMS.Log("Unable to Retrieve Video Item")
	    return MessageContainer("No items available", "There are no items available.")

    list = []
       
    req = XML.ElementFromURL(WEBROOT, True)
	
    categories = req.xpath("//ul[@class='nav-left'][1]//a/@href")
    category = "/" + categories[0]

    # Seriously, no Case type statement in Python? There has to be a much better way to do this entire codeblock 
    if (cat == "New"): category = "" 
    if (cat == "Telecasts"): category = "/" + categories[0]
    if (cat == "Interviews"): category = "/" + categories[1]
    if (cat == "Productions"): category = "/" + categories[2]
    if (cat == "Archives"): category = "/" + categories[3]
    if (cat == "Tips"): category = "/" + categories[4]
	
    req = XML.ElementFromURL(WEBROOT + category, True)
    titles = req.xpath("//div[@id='video-list']//span[@class='video-thumb-title']//*")
    videos = req.xpath("//div[@id='video-list']//span[@class='video-thumb-title']/a/@href")
    thumbs = req.xpath("//div[@id='video-list']//img/@src")
    summaries = req.xpath("//div[@id='video-list']//div")
    dates = req.xpath("//div[@id='video-list']//span[@class='video-thumb-date']")

    for i in range(len(titles)):
        video=[WEBROOT + "/" + videos[i], titles[i].text.strip(), dates[i].text.strip(), summaries[i].text.strip(), thumbs[i]]
        list.append(video)

    return list

def CheckLogin():
    try:
        cookies = Cookie.SimpleCookie(HTTP.GetCookiesForURL(WEBROOT))
        if cookies["XtraFrameUser"].value != '':
            return True
    except (Cookie.CookieError, KeyError):
        return False

def SignIn():
    if CheckLogin():
        PMS.Log("Login - Already logged in")
        return True

    username = Prefs.Get('username')
    password = Prefs.Get('password')
    if not (username and password):
        PMS.Log('username or password is empty')
        return False

    req = XML.ElementFromURL(WEBROOT, True)

    eventvalidation = None
    viewstate = None

    eventvalidation = req.xpath('//input[@type="hidden"][@name="__EVENTVALIDATION"]/@value')
    viewstate = req.xpath('//input[@type="hidden"][@name="__VIEWSTATE"]/@value')
    
    PMS.Log('signing in...')

    params = {
        '__EVENTVALIDATION': eventvalidation[0],
        '__VIEWSTATE': viewstate[0],
        'LoginWebUserControl:userName': username,
        'LoginWebUserControl:password': password,
        'LoginWebUserControl:LoginButton': 'LOGIN'
		}

    resp = HTTP.Request(WEBROOT + "/Default.aspx", values=params, cacheTime=CACHE_INTERVAL)

    if CheckLogin():
        PMS.Log("Login - Success")
        return True
    else:
        PMS.Log("Login - Failed -Response '%s'" % (resp))
        return False