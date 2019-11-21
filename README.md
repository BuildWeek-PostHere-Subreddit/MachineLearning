## Post-Here Subreddit Recommender

### Overview:
The scope of this application is to take a potential reddit post from a user and provide a list of subreddits that are relevant to said post. This application will use Machine Learning and Natural Language Processing (NLP) techniques to provide the best possible results to our users.

### Project Architecture:
Our team of full-stack web developers created an application on React that interfaces with our Data Science API. The Data Science API accepts text from the React app and then sends the text to our model. The model first vectorizes the text input using a TFIDF Vectorizer that we fit to our Subreddit data. The model then computes the cosine similarity between our vectorized text input and our vectorized training data. Finally, our model returns the most relevant Subreddit ID’s based on the computation.

Once our application has the relevant Subreddit ID’s, it queries more subreddit information from our NoSQL Database and returns the Subreddit name, link, title, description, number of subscribers, active subscribers, and the subreddit score to the React app.

![alt text](https://github.com/BuildWeek-PostHere-Subreddit/MachineLearning/blob/master/Pics/api_logic.png "Architecture")
## Authors

#### - Matthew Sessions - Data Scientist
#### - Johana Luna - Data Scientist

## License
#### This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE.md file for details
