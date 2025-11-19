# Item Based Collaborative Filtering - Top 5 recommendations for Nike products

Using the items dataset (nike_data_2022_09.csv) and the users dataset (people.csv), I updated the code provided in the lab assignment in order to give top 5 recommended items for a certain user.

Code modifications:
* generated new User-Item matrix for first 10 users and 15 items from dataset with rating from 1 to 5 (0 means that the item was not reviewed)
* generated Item-Item Similarity Matrix using cosine similarity
* used the recommend_items function in order to determine top 5 recommended products for the user 5 and this is the result:

Recommendations for user Gigi Bohling (User number 5):
- Item index 5 | id=I06 | name='NFL Miami Dolphins (Mike Gesicki)' | predicted_score=5.882
- Item index 13 | id=I14 | name='Nike Therma Lockup (NFL Kansas City Chiefs)' | predicted_score=4.708
- Item index 1 | id=I02 | name='Club América' | predicted_score=4.609
- Item index 4 | id=I05 | name='Paris Saint-Germain Repel Academy AWF' | predicted_score=4.412
- Item index 9 | id=I10 | name='Nike Therma Crucial Catch (NFL Miami Dolphins)' | predicted_score=4.401

The user interacted with the following items:
Original ratings of selected user:
Item index -> rating
  2: 5
  7: 3
  14: 5