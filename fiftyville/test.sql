-- First we search about the description of the crime
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street ='Humphrey Street';
-- took place at 10:15am interviews with 3 witnesses all mentioned the bakery
--know the witnesses transcription from bakery reports
SELECT name,transcript FROM interviews
WHERE year=2021 AND day=28 AND month=7 ;
-- at he withdrawn money from the atm the go to Emma's bakery .. by Eugene
--then went to his car and left the parking lot by Ruth
-- when he was leaving he talken in the mobile for less than a min to take plane next day
-- see what he do at the bakery
SELECT license_plate FROM bakery_security_logs WHERE day=28 AND month=7 AND hour=10 AND year=2021 AND minute=23;
--plate no. is 322W7JE OR ONTHK55
--the phone calls less than minute
SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration<60 ;
--search for the name have the plate and phone number
SELECT name FROM people WHERE  id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts WHERE bank_accounts.account_number=atm_transactions.account_number AND year=2021 AND day=28 AND month=7 ) AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day=28 AND month=7 AND hour=10 AND year=2021 AND minute=23) AND phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration<60);
--get the person id that withdrawn money that time from atm
SELECT person_id FROM atm_transactions JOIN bank_accounts WHERE bank_accounts.account_number=atm_transactions.account_number AND year=2021 AND day=28 AND month=7 AND transaction_type='withdraw' AND atm_location='Humphrey Lane';
-- now we know the thief which is DIANA wi phone number = (770) 555-1861
--and passport_number is 3592750733 license_plate is 322W7JE
-- now we wanna know where she is going
SELECT full_name FROM flights JOIN airports WHERE destination_airport_id=airports.id AND flights.id IN (SELECT flight_id FROM passengers WHERE passport_number=3592750733 AND day=29 AND month=7 AND year=2021);
--know who helped here
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration<60 AND caller='(770) 555-1861');
