## Calculating user statistics
Write a mapper and reducer that returns - for each user - the number of comments, the average number of upvotes per comment, and the average length of each comment.

## Questions
Q1: Who is most prolific, that is, who has the most comments.  Make sure it is a real user, not '[deleted]' or a bot like 'AutoModerator'.  
A: 'Late_Night_Grumbler' with 8175 comments is most prolific subreddit.

Q2: Who is the best liked, the highest average upvotes?  
A: 'yelloueze' is the best liked subreddit, with 5508.0 upvotes.

Q3: Who has the most verbose, the longest average comment length?  
A: 'Ayylamokaiii' has the most verbose comment with average comment length of 2782.

## Files
`mapper.py`: mapper of this problem  
`reducer.py`: reducer of this problem  
`part-00000`: output of the MapReduce program
