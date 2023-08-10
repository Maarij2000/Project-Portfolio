import random

import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import pyttsx3
import csv
import pandas as pd
import numpy as np
import pandas as pd
import timeit
import wikipedia

# #b.	Would you like to place a new order? (Yes or No)
# i.	If yes: Ask questions that Afraaz Ali provided
# 1.	1. POL (Port of Loading)
# 2.	2. POD (Port of Deloading)
# 3.	3. Commodity (Type of Goods)
# 4.	4. Terms (Incoterm)
# 5.	5. Net Weight (Weight of Goods)
# 6.	6. T Gwt (Total weight of Goods in vessels)
# 7.	7. Package (Number of goods)
# 8.	8. Volume (Dimensions)
# 9.	9. Pick-up Address
# Attributes referring to the information collected about the shipping


listener = sr.Recognizer()
microphone = sr.Microphone()
player = pyttsx3.init()
pol = pod = commodity = terms = ""
pick_up_address = ""
net_weight = total_weight = package =  volume = 0
main_menu_counter = 0
#
# def IBM_Speech(file_name):
#     authenticator = IAMAuthenticator("KfzwRzlAhU_fg8o1QRCrpOe0xFVNMIuOgUj1ls-Uox-N")
#     stt = SpeechToTextV1(authenticator = authenticator)
#
#     stt.set_service_url("https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/669d6070-bac9-41c6-81de-787b06d21ce6")
#
#     with open(file_name, "rb") as f:
#         res = stt.recognize(audio = f, content_type="audio/wav", model = "en-US_NarrowbandModel").get_result()
#
#     print(res)
#     text = res["results"][0]["alternatives"][0]["transcript"]
#     print(type(text))

def listen():

    with sr.Microphone() as input_device:
        print("I am ready, listen")
        listener.adjust_for_ambient_noise(input_device)
        listener.dynamic_energy_threshold = 3000
        voice_content = listener.listen(input_device, timeout = 7.0)

    with open("Talk.wav", "wb") as f:
        f.write(voice_content.get_wav_data())

    authenticator = IAMAuthenticator("KfzwRzlAhU_fg8o1QRCrpOe0xFVNMIuOgUj1ls-Uox-N")
    stt = SpeechToTextV1(authenticator=authenticator)

    stt.set_service_url(
        "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/669d6070-bac9-41c6-81de-787b06d21ce6")

    with open("Talk.wav", "rb") as f:
        res = stt.recognize(audio=f, content_type="audio/wav", model="en-US_NarrowbandModel", end_of_phrase_silence_time = 0.6, smart_formatting= True, inactivity_timeout=-1, split_transcript_at_phrase_end = True, timestamps=True).get_result()

    print(res)
    text = res["results"][0]["alternatives"][0]["transcript"]

    return text



def order_id():
    random_number = ""
    for i in range(0, 5):
        random_number = random_number + str(random.randint(0, 9))
    return random_number

def write_to_csv(data):
    data = [data]
    with open('Order_Details.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def write_to_status_csv(data):
    data = [data]
    with open('Order_Status.csv', 'a', encoding= 'UTF8', newline = '') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def talk(text):
    voice = player.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    player.setProperty('voice', voice[1].id)
    player.setProperty("rate", 150)
    player.say(text)
    player.runAndWait()


def confirmation(input):
    talk(f"Is {input} the correct thing that you said?")


def order_response(attributes):
    talk("You said " + attributes + ". Is this correct? (Please say Yes or No)")
    response = listen()
    if "yes" in response:
        return attributes
    counter = 0
    while ("no" in response and counter < 2):
        counter = counter + 1
        talk("May you please repeat it?")
        user_input = listen()
        talk("You said " + user_input + ". Is this correct? (Yes or No)")
        reply = listen()
        if "yes" in reply:
            return user_input

    talk("You have reached maximum number of tries, please call again later. Have a great day!")
    return 0


def option_1():
    talk("Our services include the following:")
    talk("Sea Freight")
    talk("Air Freight")
    talk("Warehousing & Distribution")
    talk("Custom Clearance")
    talk("To no more about these services please visit our website at fahimexpress.ae:")


# If the user chooses option 2 and ask about the things needed to place a new order
def option_2():
    # Thinking of removing talk because the options already specify if the user wants to place a new order
    counter = 0
    # talk("Would you like to place a new order? ( Please say Yes or No)")
    # reply = listen()
    # if "yes" in reply:
    print("Understood. Please specify the port of loading")
    talk("Understood. Please specify the port of loading")
    pol = listen()
    pol = order_response(pol)

    if pol != 0:
        talk("Understood")
        print("Please specify the port of deloading")
        talk("Please specify the Port of Deloading")
        pod = listen()
        pod = order_response(pod)

        if pod != 0:
            talk("Understood")
            print("Please specify the type of goods")
            talk("Please specify the type of goods")
            commodity = listen()
            commodity = order_response(commodity)

            if commodity != 0:
                talk("Understood")
                print("Please specify the net weight of the goods")
                talk("Please specify the net weight of the goods")
                net_weight = listen()
                net_weight = order_response(net_weight)

                if net_weight != 0:
                    talk("Understood")
                    print("Please specify the total weight of goods in the vessel")
                    talk("Please specify the total weight of goods in the vessel")
                    total_weight = listen()
                    total_weight = order_response(total_weight)

                    if total_weight != 0:
                        talk("Understood")
                        print("Please specify the number of packages")
                        talk("Please specify the number of packages")
                        package = listen()
                        package = order_response(package)

                        if package != 0:
                            talk("Understood")
                            print("Please specify the Volume")
                            talk("Please specify the Volume")
                            volume = listen()
                            volume = order_response(volume)

                            if volume != 0:
                                talk("Understood")
                                print("Please specify the pick up address")
                                talk("Please specify the pick up address")
                                pick_up_address = listen()
                                pick_up_address = order_response(pick_up_address)
                                order_number = order_id()
                                write_to_csv([order_number, pol, pod, commodity, net_weight, total_weight, package, volume, pick_up_address])
                                write_to_status_csv([order_number, "Under Review"])
                                talk("Your Order ID is " + order_number + " please keep it with you for future references")
                                talk("Thank you for using Fahim Ali express, our representative will contact you in the next 24 to 48 hours with the pricing details.")
                                talk("Have a great day!")

def option_3():
    counter_option  = 0
    flag = 0
    while counter_option < 3 and flag != 1:
        talk("Please tell us your 5 digit order id")
        order_number = listen()
        df = pd.read_csv("Order_Status.csv")
        # response = input("Enter your 4 digit ID")

        # print(type(order_number))
        # print(df["Order_ID"][0])
        for ind, row in df.iterrows():
            if int(order_number) == row["Order_ID"]:
                talk("Your status of Order ID" + order_number + " is... " + row["Status"])
                flag = 1

        if counter_option == 2:
            talk("Sorry,we were not able to find your order id. Please call again later")
            break

        if flag != 1 and counter_option < 3:
            talk("Sorry, we were not able to find your Order id. Please try again")
            counter_option = counter_option + 1


# Welcome message
def main_menu():
    global main_menu_counter
    talk("Welcome to Fahim Express! Please select from one of the options")
    talk("If you'd like to know about our services, please say 1")
    talk("If you'd like to place a new order, please say 2")
    talk("If you'd like to follow up on your order,  please say 3")
    response = listen()
    if "one" in str(response):
        option_1()
    elif 2 == int(response):
        option_2()
    elif 3 == int(response):
        option_3()
    else:
        while main_menu_counter < 2:
            if main_menu_counter == 2:
                talk("You have reached the maximum number of tries. Please call again later. Have a great day!")
            main_menu_counter = main_menu_counter + 1
            talk("Invalid option chosen. Please listen to the main menu again and choose an option")
            main_menu()


    #
# response = input("Please type your response")
main_menu()












