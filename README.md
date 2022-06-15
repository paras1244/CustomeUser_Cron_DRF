
1. First of all create your own environment 
<<<<<command >>>>
python3 -m venv venv
source venv/bin/activate 


2. Install the all dependencies using requirements.txt
<<<<<command >>>>
pip3 install -r requirements.txt 


3. Run your project using Local server 8000
<<<<<command >>>>
python3 manage.py runserver 


4. Import the postman collection that i have atteched into our project folder 
<<<<<POSTMAN collection folder name  >>>>
Test the APIs.postman_collection.json


NOTE: In postman collection I have added the perfect names of APIs so you can identify using those titles in the postman collection

5. Register the user using register API
(http://127.0.0.1:8000/register) ----> POST request
 
6. Login by using the registered user (After that you get the access token, so you need to add the access token in every API before call or request.)
(for add tocken in every request in POSTMAN you need to click Authorization > bearer token > add token)
(http://127.0.0.1:8000/login) ----> POST request


7. Add the hotel using add hotel API && Check the other APIs like edit hotel, remove hotel and delete hotel.
(http://127.0.0.1:8000/hotel) ----> Add the hotel ( POST request )
(http://127.0.0.1:8000/hotel/1/) ----> edit the hotel ( PUT request )
(http://127.0.0.1:8000/hotel/1/) ----> delete the hotel ( DELETE request )

8. Get the Hotel list using 
(http://127.0.0.1:8000/hotel) ----> Get all hotel list (GET request)

9. Click on the voting the hotel api  
    (http://127.0.0.1:8000/vote/1/)  add id of your hotel that you want to vote -------> (POST request )

10. for check the History of the hotel winer 
(http://127.0.0.1:8000/Daily_Winners_history) ----> ( Get request )


NOTE: I have added the 24 hours(means every night 12:00 am) renewal of votes for every user.
and also renewal of history of winner. 

Every User get 1.75 votes for use every day.
when user give vote to some hotel first time it will cut the 1 vote
second time 0.50(1/5) and third time 0.25(1/4)

User can add vot 3 time per day.
