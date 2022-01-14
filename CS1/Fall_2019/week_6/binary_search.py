## Binary search class example
## By THC.

# Find an item with value key in the_list[p ... r].
# Return the index of the item, or None if no such item
# is in the_list[p ... r].
def binary_search(the_list, key, p = 0, r = None):
    if r == None:   # use default value of last index in the_list?
        r = len(the_list) - 1

    if p > r:
        return None     # sublist is empty, so not found
    else:
        midpoint = (p + r) // 2
        if the_list[midpoint] == key:
            return midpoint     # found it!
        elif key < the_list[midpoint]:
            # If key is in the_list, it must be in the first half
            # of the sublist.
            return binary_search(the_list, key, p, midpoint - 1)
        else:
            # If key is in the_list, it must be in the second half
            # of the sublist.
            return binary_search(the_list, key, midpoint + 1, r)

countries = ["Afghanistan", "Akrotiri", "Albania", "Algeria",
             "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica",
             "Antigua and Barbuda", "Argentina", "Armenia", "Aruba",
             "Ashmore and Cartier Islands", "Australia", "Austria",
             "Azerbaijan", "Bahamas, The", "Bahrain", "Bangladesh",
             "Barbados", "Bassas da India", "Belarus", "Belgium", "Belize",
             "Benin", "Bermuda", "Bhutan", "Bolivia",
             "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil",
             "British Indian Ocean Territory", "British Virgin Islands",
             "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi",
             "Cambodia", "Cameroon", "Canada", "Cape Verde",
             "Cayman Islands", "Central African Republic", "Chad", "Chile",
             "China", "Christmas Island", "Clipperton Island", "Cocos",
             "Colombia", "Comoros", "Congo, Democratic Republic of the",
             "Congo, Republic of the", "Cook Islands", "Coral Sea Islands",
             "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
             "Czech Republic", "Denmark", "Dhekelia", "Djibouti", "Dominica",
             "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
             "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia",
             "Europa Island", "Falkland Islands", "Faroe Islands", "Fiji",
             "Finland", "France", "French Guiana", "French Polynesia",
             "French Southern and Antarctic Lands", "Gabon", "Gambia, The",
             "Gaza Strip", "Georgia", "Germany", "Ghana", "Gibraltar",
             "Glorioso Islands", "Greece", "Greenland", "Grenada",
             "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea",
             "Guinea-Bissau", "Guyana", "Haiti",
             "Heard Island and McDonald Islands", "Holy See", "Honduras",
             "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran",
             "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica",
             "Jan Mayen", "Japan", "Jersey", "Jordan", "Juan de Nova Island",
             "Kazakhstan", "Kenya", "Kiribati", "Korea, North",
             "Korea, South", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
             "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
             "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar",
             "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
             "Marshall Islands", "Martinique", "Mauritania", "Mauritius",
             "Mayotte", "Mexico", "Micronesia, Federated States of",
             "Moldova", "Monaco", "Mongolia", "Montserrat", "Morocco",
             "Mozambique", "Namibia", "Nauru", "Navassa Island", "Nepal",
             "Netherlands", "Netherlands Antilles", "New Caledonia",
             "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue",
             "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman",
             "Pakistan", "Palau", "Panama", "Papua New Guinea",
             "Paracel Islands", "Paraguay", "Peru", "Philippines",
             "Pitcairn Islands", "Poland", "Portugal", "Puerto Rico",
             "Qatar", "Reunion", "Romania", "Russia", "Rwanda",
             "Saint Helena", "Saint Kitts and Nevis", "Saint Lucia",
             "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines",
             "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
             "Senegal", "Serbia and Montenegro", "Seychelles",
             "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
             "Solomon Islands", "Somalia", "South Africa",
             "South Georgia and the South Sandwich Islands", "Spain",
             "Spratly Islands", "Sri Lanka", "Sudan", "Suriname", "Svalbard",
             "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan",
             "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo",
             "Tokelau", "Tonga", "Trinidad and Tobago", "Tromelin Island",
             "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands",
             "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
             "United Kingdom", "United States", "Uruguay", "Uzbekistan",
             "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands",
             "Wake Island", "Wallis and Futuna", "West Bank",
             "Western Sahara", "Yemen", "Zambia", "Zimbabwe"]

while True:
    target = input("Enter the name of a country (RETURN to end): ")
    if len(target) == 0:
        break
    index = binary_search(countries, target)
    if index == None:
        print(target + " is not in the list of countries")
    else:
        print(target + " appears at index " + str(index))