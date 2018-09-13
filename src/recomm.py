#http://surpriselib.com/
#https://medium.com/p/d2736d2e92a8
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Predicting
# Retrieve the trainset.
trainset = data.build_full_trainset()
algo.fit(trainset)

# Predict a certain item
userid = str(196)
itemid = str(302)
actual_rating = 4
print(algo.predict(userid, itemid, actual_rating))

exit(0)

