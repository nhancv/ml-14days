# Machine Learning Practitioner in 14 Days

```
Day 1: Download and Install Python and SciPy Ecosystem (today).
Day 2: Get Around In Python, NumPy, Matplotlib and Pandas.
Day 3: Load Data and Standard Machine Learning Datasets.
Day 4: Understand Data with Descriptive Statistics.
Day 5: Understand Data with Visualization.
Day 6: Prepare For Modeling by Pre-Processing Data.
Day 7: Algorithm Evaluation With Resampling Methods.
Day 8: Algorithm Evaluation Metrics.
Day 9: Spot-Check Machine Learning Algorithms.
Day 10: Model Comparison and Selection.
Day 11: Improve Accuracy with Algorithm Tuning.
Day 12: Improve Accuracy with Ensemble Predictions.
Day 13: Finalize And Save Your Model.
Day 14: Hello World End-to-End Project.

MachineLearningMastery.com
```



### Install python3 env
```
export ML_ROOT="/Volumes/Soft/_Program_Files/python/ml"
alias ml.setup="virtualenv --system-site-packages -p python3 $ML_ROOT && ml.active"
alias ml.destroy="rm -rf $ML_ROOT"
alias ml.active="source $ML_ROOT/bin/activate"
```

### Install libs
```
pip install numpy scipy matplotlib pandas statsmodels scikit-learn
```

### Test lib installed successfully (versions.py)
```
# scipy
import scipy
print('scipy: %s' % scipy.__version__)
# numpy
import numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
import pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
import statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)
```

