## Subreddit Love Index
Write a mapper and reducer that counts the words "love" and "hate" in comments and calculate what I'm calling the "love index" for each subreddit. The love index is the difference in love and hate counts, divided by the sum:

![](./love_index.PNG)

This is a sort of normalized measure of love. It ranges from 1 (all the love) to -1 (too much hate), taking into account the total number of love and hate comments. This makes it so big subreddits with a bunch of comments are on the same scale as small subreddits.

## Questions
Q1: Which subreddit has the highest love index?  
A: Random_Acts_Of_Amazon with 0.6775 love index.

Q2: Which subreddit has the lowest love index?  
A: ukpolitics with -0.3603 love index.

## Files
`mapper.py`: mapper of this problem  
`reducer.py`: reducer of this problem  
`part-00000`: output of the MapReduce program
