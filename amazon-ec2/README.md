# Deploying a Hadoop cluster on Amazon EC2
In this lesson, a small Hadoop cluster with 1 NameNode and 3 DataNodes was deployed on Amazon EC2. The clustes was used to analyze a dataset of posts from [superuser.com](http://superuser.com/), a StackExchange community.

## Dataset
The dataset is an XML file which can ne downloaded [here](https://s3.amazonaws.com/content.udacity-data.com/courses/ud1000/data/Posts.xml). Python library [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) was used to parse the content of dataset.   

A glimpse of the tags and the attributes in the XML file:

```python
[('Body',
  "text here"),
 ('ViewCount', '1191'),
 ('Title',
  'Why does the Macbook Pro Unibody crash on hibernate under Windows?'),
 ('LastActivityDate', '2009-07-15T21:15:21.323'),
 ('AnswerCount', '3'),
 ('CommentCount', '2'),
 ('AcceptedAnswerId', '3841'),
 ('Score', '4'),
 ('PostTypeId', '1'),
 ('OwnerUserId', '26'),
 ('Tags', '<mac><crash><boot-camp>'),
 ('CreationDate', '2009-07-15T07:17:13.970'),
 ('FavoriteCount', '1'),
 ('Id', '37')]
```

## Problem Set

1. [View counts and post scores](./view-counts)
2. [Average number of answers](./avg-answer)
3. [Average post lifetime](./avg-post-life)
