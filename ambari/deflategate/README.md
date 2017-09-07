## Deflategate conversation over time
Way back in 2015, the New England Patriots allegedly deflated footballs used in the AFC championship game. Multiple suspensions, a federal judge got involved, dogs and cats living together.

Write a mapper and reducer that counts the number of mentions of "Deflategate" or "Tom Brady" for each day of May 2015 in the NFL subreddit (nfl in the dataset). Also, make sure to count both capitalized and non-capitalized versions.

## Question
Q: Which two days were people talking about Deflategate the most? Just enter the dates (we know is May 2015)  
A: From the plot below, we know May 7th with 2049 mentions had the highest mentions. May 12th had the second highest with 2036 mentions.

![Number of mentions of 'Deflategate' or 'Tom Brady' for each day in May 2015](https://user-images.githubusercontent.com/30658373/30156426-39bbf082-93f2-11e7-9ca7-5bc8fa7b5dfe.jpg)

From the plot, we can notice the number of mentions started to increase around May 6th. This is when the NFL's investigative report was released. Talk died down pretty quickly until May 11th, when the NFL announced they were suspending Tom Brady.

## Files
`mapper.py`: mapper of this problem  
`reducer.py`: reducer of this problem  
`part-00000`: output of the MapReduce program
