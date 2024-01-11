passworDict = {
    'facebook':'Username: Sigma69 Password: Cornoncob420',
    'twitter':"Username: @Sigma69_1337 Password: Lol",
    "lacob d'souza" : "Username: ilostmybookbloxchannel Password: LolIactuallylostmyaccountlikeimagine",
    "lola" : "Username: @xCoin_ Password: TGJSAPO12412515"
}
passwordrec = input('Enter the social media site or app you want login for Eg. youtube, facebook, twitter\n')
passw = passwordrec.lower()
if passw in list(passworDict.keys()):
  print("Here is your username and password:")
  print(passworDict[passw])
elif passw == 'youtube':
   yid = input('Please enter your YouTube username:')
   if yid.lower() == "jacob d'souza":
    print(passworDict["jacob d'souza"])
   if yid.lower() == "lola":
    print(passworDict["lola"])
else:
    print("Invalid entry. Please enter a valid social media site or app name.")