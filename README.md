# SimpleKeyGen95
Very simple KeyGen for Windows 95

there's not much to say really it's just a really shitty python code that generates Windows 95 keys :3

### Structure

## XXX
A three-digit number between 001 and 366, representing the day of the year.

## YY
A two-digit number between 95 and 99, indicating the last two digits of the key’s year. Technically, it could extend up to 03, but to avoid generating invalid years between 04-92, this range is limited to 95-99.

## OEM and 00
These segments remain unchanged for every key, solely indicating that the key is an OEM (Original Equipment Manufacturer) key.

## SSSSS
A five-digit number whose digits must sum to a value divisible by 7.

## ZZZZZ
A randomly generated five-digit number for additional uniqueness. 
