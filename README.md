# 361-microservice
Given company name, returns salary information for internship from levels.fyi, using text file communication

## Communication Contract:
### Requesting information:
My microservice will work by reading a text file containing a company name. The microservice is currently implemented to accept any capitalization for companies that are listed in the companies.json. For example, "zillow" will be converted to "Zillow" and work correctly, "Jane street" will be converted to "Jane-Street" and work correctly. Companies that are not currently in the JSON will still work if the capitalization/dashes are correct. For example, "Disney" is not in the json, but will still work correctly, however "disney" will not. "Chick Fil A" is not in the JSON yet and will only work if given as "Chick-Fil-A." I will be working on improving the error handling so the microservice will automatically convert the companies correctly, but for now you will need to stick to the companies in the JSON, or provide correct capitlization and dashes based on how it is displayed on levels.fyi.

### Receiving information:
The text file will be updated to show salary information from levels.fyi. For example, "Zillow" will return "$55.29 per hour, $9,584 per month". If you provide a company name that does not exist on levels.fyi, or is structured incorrectly and not in the JSON as mentioned above, the microservice will return "Could not find (company)'s salary"


![image](https://user-images.githubusercontent.com/91440965/199101513-4f81ffe2-cbb2-4f59-acb7-4e5af1a4e310.png)
