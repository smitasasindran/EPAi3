### Assignment 9: Named Tuples

Submitted by:   
Smita Sasindran (smitasasindran@gmail.com)


### Question 1:
Use the Faker (Links to an external site.)library to get 10000 random profiles. 
Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, 
and average age (add proper doc-strings). - 250 (including 5 test cases)


Function definition:
Pass the number of fake profiles to be generated, and if debug statements should be printed     
```def profiles_summary_named_tuples(n=10000, debug=True):```




### Question 2: 
Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)   

Function definition:
Pass the number of fake profiles to be generated, and if debug statements should be printed     
```def profiles_summary_dict(n=10000, debug=True):```


### Question 3:
Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies 
(name, symbol, open, high, close). Assign a random weight to all the companies. 
Calculate and show what value the stock market started at, what was the highest value during the day, 
and where did it end. Make sure your open, high, close are not totally random. 
You can only use namedtuple. - 500  (including 10 test cases)

```def stock_market(n):```


### Helper Functions: 


1. timed decorator   
Decorate the functions with ```@timed(iterations)```

2. Function to create fake profiles  
Function to create 'n' fake profiles. If make_tuple is passed as true, it returns 'n' profiles 
that are named tuples, else it returns a profile in a dictionary format.  
```def get_profiles(n, make_tuple=False):```

3. Function to get the profile summary for profiles with named tuples  
This function calculates the mean age, oldest age, mean location, most common blood type when the profiles are in named tuple format.      
```def get_summary_named_tuples(n, profiles):```

4. Function to get the profile summary for profiles with dicts  
This function calculates the mean age, oldest age, mean location, most common blood type when the profiles are in dictionary format.      
```def get_summary_named_dict(n, profiles):```

5. Common calculation function 
A common calculation function that can be used once the counts are already available.   
```def calculate(n, age, lat, lng, blood_type_counts):```

