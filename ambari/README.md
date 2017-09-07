# Deploy a Hadoop cluster with Ambari
In this lesson, a large Hadoop cluster with 1 Standby NameNode, 1 Active NameNode and 4 DataNodes was set up on Amazon EC2 by using Apache Ambari. This cluster was used to analyze a dataset of Reddit comments from May 2015.

## Dataset
The data is a ~4.5 GB CSV file with columns separated with tabs. The file can be downloaded [here](https://s3.amazonaws.com/content.udacity-data.com/courses/ud1000/data/comments.tar.gz). The columns are: subreddit, author, body, created_utc, ups, downs, gilded, archived. For each comment,

* **subreddit**: The subreddit the comment was posted in  
* **author**: Username of the comment author  
* **body**: Comment text  
* **create_utc**: UTC timestamp of when the comment was posted  
* **ups**: Comment upvotes  
* **downs**: Comment downvotes  
* **gilded**: 1 if the user was given Reddit gold for the comment, 0 otherwise  
* **archived**: 1 if the comment was archived, 0 otherwise  

## Problem Set
1. [Love and Hate](./love-hate)  
2. [User statistics](./user-stats)
3. [Deflategate](./deflategate)
