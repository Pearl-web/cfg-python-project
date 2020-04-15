import requests
import csv

collected_data = []
#created list for exporting data later on to csv

while True:

    def covid_database_search():

        # I want it to show only today's data so have to use yesterdays date as API is "Live By Country And Status After Date"
        # for today's data I need to use after yesterdays date in the url

        from datetime import date, timedelta
        today = date.today()
        yesterday = today - timedelta(days = 1)

        #asking for user input

        user_input = input('What country would you like to find out about?')


        url = 'https://api.covid19api.com/live/country/{}/status/confirmed/date/{}T13:13:30Z'.format(user_input, yesterday)

        response_api = requests.get(url)


        covid_data = response_api.json()
        collected_data.append(covid_data)
        return covid_data

    #print(covid_data)- this shows inital data in one long line for a given country, below splits this up so only
    #relevant data is shown to the user

    def run():

        for item in covid_database_search():
            if item['Country'] == 'China' or item['Country'] == 'United States of America' or item['Country'] == 'Canada':
                #these three countries do not have a data set without a province, so we have to show all of the data
                print('Province: ' + item['Province'])
                print('Country: ' + item['Country'])
                print('Total Confirmed Cases: ' + str(item['Confirmed']))
                print('Deaths:' + str(item['Deaths']))
                print('Recovered:' + str(item['Recovered']))
                print('Current Active Cases:' + str(item['Active']))
                print('Date:' + str(item['Date']))
                print("")
            else:
                #this shows only the data for the main country and not provinces of the country
                if item['Province'] == "":
                    print('Country: ' + item['Country'])
                    print('Total Confirmed Cases: ' + str(item['Confirmed']))
                    print('Deaths:' + str(item['Deaths']))
                    print('Recovered:' + str(item['Recovered']))
                    print('Current Active Cases:' + str(item['Active']))
                    print('Date:' + str(item['Date']))
                    print("")


    run()

  #asking the user if they would like to see more data

    exit_programme = input('Would you like information about another country?')
    if exit_programme == 'no':
        print('Ok - before you go...')
        break

# question before they leave the programme about exporting data

user_input_2 = input('Would you like to export all of the data into a csv format so you can compare country data?')
if user_input_2 == 'yes':

    with open('covid_results.txt','w') as covid_file:
        writer = csv.writer(covid_file)
        writer.writerows(collected_data)

        print('It has been exported. Bye!')
else:
    print('0k - Bye Bye :)')






















