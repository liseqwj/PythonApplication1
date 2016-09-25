rain = input("Is it raining today? y/n: ")
if rain == "y":
    umbrella = input("Do you have an umbrella? y/n: ")
    if umbrella == "y":
        pass 
    else:
        print("Wait a while")
        sleep(5)
        moreRain = True
        while moreRain:
            askForRain = input("Is it still raining? y/n: ")
            if askForRain == "y":
                print("wait a little longer")
                sleep(2)
            else:
                moreRain = False
print()
print("Hooray! you can go outside safely")