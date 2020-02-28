# SuzyBot

A Discord bot that I made so that that my friend doesn't keep putting bot commands for groovy in #general

___

## Getting environment variables to the container while maintaining data integrity

***Friday, February 28, 2020***

So here is the situation, over that past week I have slowly been adding 
a fewfeatures that one would find in a real application. as of the moment 
those features have been 
- 1: A mongodb database 
- 2: Containerization with docker 

originally whenever I would want to rebuild my container, 
I would run ***`bins/rebuildDb.bash`***, it woudl
- stop the server 
- rebuild it
- restart it and

Now what I wanted to do was find a system so that I was not creating a
container from my local system but instead from my git repository

The only issue is that my application pulls environment variables 
from a `.env` file that is not present in the repository(for 
security reasons)

#### The Current Issue
Finding a secure way I can pass the environment variables to my program
while not comprising all of my tokens and connection strings

___