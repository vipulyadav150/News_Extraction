import requests


def extract_location(main_url):
    manual_city = input("Enter city name: ")
    manual_city = manual_city.lower()
    main_url = main_url + '/' + manual_city
    # print(main_url)

    return main_url,manual_city




