from price_prediction import predict_price
import pandas as pd
userInput = ''
while(userInput != 'q'):
    print("Write q to quit, or pass m2 of flat you want to predict price")
    userInput = input()
    if(userInput == 'q'):
        exit()
    m2 = pd.to_numeric(userInput)
    print("Pass number of rooms")
    userInput = input()
    rooms = pd.to_numeric(userInput)
    
    print('Predicted price:' + str(predict_price('../Scrapper/flatcrawling/flatcrawling/spiders/offers.json', rooms, m2)))
    