select description from crime_scene_reports
where year=2021 and month = 7 and day = 28 and street = "Humphrey Street";

-- checking the interview stranscripts

select name, transcript from interviews
where day = "28" and month = "7" and year = "2021";

-- checking to see how many people by the name Eugene in the peoples table
select name from people where name = 'Eugene';
-- there is only one eugene in people list

-- let's find out who are the 3 witnesses from the list of names of people who game interviews on july 28, 2021. According to crime report
-- each of them mentioned bakery in their report

select name,transcript from interviews
where year=2021 and month=7 and day=28 and transcript like '%bakery%'
order by name;

-- according to eugene the thief was withdrawing money from the ATM on Leggett Street. Let's check the detials from that atm records
select account_number, amount from atm_transactions
where year = 2021 and month =7 and day=28 and atm_location='Leggett Street' and transaction_type='withdraw';

-- let's find the account names of those transactions from the bank based on their transaction detials
select name, atm_transactions.amount, atm_transactions.account_number from people
join bank_accounts on people.id = bank_accounts.person_id
join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where atm_transactions.year=2021
and atm_transactions.month=7
and atm_transactions.day=28
and atm_transactions.atm_location='Leggett Street'
and atm_transactions.transaction_type = 'withdraw';

-- according to raymonds lead lets find out the infomation about the airport in Fiftyville
select abbreviation, full_name, city
from airports
where city = 'Fiftyville';

-- Now let's find out what the flights scheduled on 29 from Fiftyville and order them by time
select flights.id, full_name, city, flights.hour, flights.minute
from airports
join flights
on airports.id = flights.destination_airport_id
where flights.origin_airport_id = (
    select id
    from airports
    where city = 'Fiftyville'
)
and flights.year = 2021
and flights.month = 7
and flights.day = 29
order by flights.hour, flights.minute;
-- the first flight scheduled to be 8.20 to LaGuardia Airport in New York City (flight id is 36) this might be the place where theif went

-- Now can check the passengers list to find out who are the people onboard that flight ordering them by their passport numbers
select passengers.flight_id, name, passengers.passport_number, passengers.seat
from people
join passengers
on people.passport_number = passengers.passport_number
join flights
on passengers.flight_id = flights.id
where flights.year = 2021
and flights.month = 7
and flights.day = 29
and flights.hour = 8
and flights.minute = 20
order by passengers.passport_number;
-- now let's check the phone call records to find the person who bought the tickets

-- first, need to check the possible names of the callers, and put the names in the suspect list. ordering them according to the durations of the calls
select name, phone_calls.duration
from people
join phone_calls
on people.phone_number = phone_calls.caller
where phone_calls.year = 2021
and phone_calls.month = 7
and phone_calls.day = 28
and phone_calls.duration <= 60
order by phone_calls.duration;

-- next let's check the possible names of the call-receiver. then order them by the durations of the calls
select name, phone_calls.duration
from people
join phone_calls
on people.phone_number = phone_calls.receiver
where phone_calls.year = 2021
and phone_calls.month = 7
and phone_calls.day = 28
and phone_calls.duration <= 60
order by phone_calls.duration;

-- according to Ruth the thief drove away in a car from the bakery, within 10minutes from the theft. So let's check the licencse plates of cars within that time frame with
-- the respective owners of the vehicles

select name, bakery_security_logs.hour, bakery_security_logs.minute
from people
join bakery_security_logs
on people.license_plate = bakery_security_logs.license_plate
where bakery_security_logs.year = 2021
and bakery_security_logs.month = 7
and bakery_security_logs.day = 28
and bakery_security_logs.activity = 'exit'
and bakery_security_logs.minute >= 15
and bakery_security_logs.minute <= 25
order by bakery_security_logs.minute;