__author__ = 'jc321013'
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from Currency import current_time_date  # imports function from Currency file to get the date
from Currency import current_trip_location
from Currency import get_all_details
from Currency import convert
from Currency import get_details


class ExchangeCalculator(App):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)

    def build(self):
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')  # allows access to the layout of the app
        Window.size = (350, 700)
        ExchangeCalculator.load_details(self)
        self.root.ids.trip_location.text = current_trip_location()  # id of the app, know which part of the layout to apply the function to
        self.root.ids.real_time.text = current_time_date()
        self.root.ids.update_currency = get_all_details()
        return self.root

    def load_details(self):
        spinner_details_file = open("config.txt", 'r', encoding='utf-8')  # opens and reads the config file to access the list of countries
        spinner_details_data = spinner_details_file.readlines()  # reads the lines of the file
        spinner_details_file.close()
        countries = []
        for spinner_details_line in spinner_details_data:
            spinner_details_strings = spinner_details_line.strip().split(",")  # splits the data needs only what is necessary
            countries.append(spinner_details_strings[0])
        self.root.ids.spinner_details.values = countries[1:]  # has access from line 1 onwards
        self.root.ids.home_country.text = countries[0]

    def get_conversion(self, home):
        self.trip = []
        config_file = open('config.txt', 'r')
        lines = config_file.readlines()
        config_file.close()
        self.country_code = []
        for line in lines[1:]:
            section = line.split(',')
            self.country_code.append(section[0])
            self.trip_details.add(section [0], section[1], section[2])





        # self.root.id.input_details.text = convert
        # self.root.id.input_details.text = get_details
        # get_conversion_file = open("currency_details.txt", 'r', encoding='utf-8')
        # get_conversion_data = get_conversion_file.readlines()[1:]
        # get_conversion_file.close()
        # countries = []
        # for get_conversion_line in get_conversion_data:
        #     get_conversion_strings = get_conversion_line.strip().split(",")
        #     countries.append(get_conversion_strings[0])
        # for line in get_conversion_data:
        #     country_string = get_details('currency_code + currency_symbol')
        #     line = line.strip().split(",")
        #     if country_string == line[4]:
        #         return 'AUD + $'
        #     self.root.ids.trip_details.text = get_details





        # self.root.ids.trip_details.values = countries[1:]
        # self.root.ids.input_details.text = countries[0]
        #
        # location_trip_file = open("config.txt", 'r', encoding='utf-8')
        # location_trip_data = location_trip_file.readlines()[1:]
        # location_trip_file.close()
        # countries = []
        # for location_trip_line in location_trip_data:
        #     location_trip_strings = location_trip_line.strip().split(",")
        #     countries.append(location_trip_strings[0])
        # for config_row in location_trip_data:
        #     real_time_string = time.strftime("%Y/%m/%d")
        #     config_row = config_row.strip().split(",")
        #     if real_time_string >= config_row[1] and real_time_string and real_time_string <= config_row[2]:
        #         return "Current Trip Location:" + config_row[0]
        # value = int(self.root.id.input_details.text)
        # result = value
        # self.root.ids.input_details.text = str(result)
        # print(value)
        # details = []
        # for details in get_details():
        #     details.append(get_details)
        # return details



        # get details for country codes
        # convert- conversion
#
#     dict = {'Country_name': 'Australia', 'currency_code': 'AUD', 'currency_symbol': '$'}
# self.home_country =


          #

        #
        #
        # try:
        #     value = float(self.root.ids.input_miles.text)
        #     return value
        # except ValueError:
        #     return 0


ExchangeCalculator().run()
