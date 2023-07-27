# UbisoftAccountGenerator
Python script that automatically generates Ubisoft / Uplay accounts without having to go to the website.

I've created a script that allows you to automatically generate Ubisoft / Uplay accounts without having to go through the hassle of going to the website.

Please note, if you are in a different country, you may need to use a different legaloptinskey and modify it as such in the script. To access a different legaloptinskey:

Send a GET request to https://public-ubiservices.ubi.com/v3/policies/{CountryCode}?languageCode=en&contentFormat=HTML where {CountryCode} is the abbreviation for your country. For example, USA would be https://public-ubiservices.ubi.com/v3/policies/US?languageCode=en&contentFormat=HTML, or Canada would https://public-ubiservices.ubi.com/v3/policies/CA?languageCode=en&contentFormat=HTML, and so on.

For this request to be successful you will need a singular header: "ubi-appid": "f35adcb5-1911-440c-b1c9-48fdc1701c68"
