The main protoype of our model is in the file predictor.ipynb. 
To run, it requires having the gensim package for python and the Google News corpus to train on. 
The files k_mediods.ipynb and model.ipynb are a less cleaned up version of our code that contributed to creating this model.

In model.ipynb we got the similarities of the 9.5 million queries (removing those that were not in the vocabulary of the corpus).
We then used the k_mediods file to determine a clustering of these into 30 categories. Not all categories were valid in our opintion so we weeded some out. We took the categories and created our protoype with them.
We used the medioid (center/average) word from each cluster to compare to inputs into our model. The closest comparison would determine the categorization and the output.
The output is a label that we assigned to best encompass the cluster.