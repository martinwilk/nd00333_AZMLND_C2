*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Operationalizing Machine Learning in Microsoft Azure

This is the second project of the Machine Learning Engineer with Microsoft Azure nanodegree. During this project a classification model is trained using AutoML. The best model is deployed as a Azure Container Instance and the REST endpoint of the deployed model is used to classify new instances. To automate the process of retraining the model, a pipeline is created and published. Using the REST endpoint of this pipeline, everyone with the authentication key is allowed to trigger a new run, for example if new data is available.

This project uses the Bankmarketing dataset (1). This dataset contains personal information from customers of a Portuguese banking institution like the age, the job and information to the last contact to the bank and if the client has subscribed a term deposit. So the banking company wants to find out which customers should be contacted via phone and informed about the term deposit offer.

The dataset I use is imbalanced, because only 10% of the customers subscribed to the term deposit. Because of that I will use the AUC_weighted metric to evaluate model performance. Another way to deal with the imbalanced dataset is over- or undersampling the data, which I will describe in more detail in the Further Improvements section.


## Architectural Diagram
*TODO*: Provide an architectural diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model".

## Key Steps
*TODO*: Write a short description of the key steps. Remember to include all the screenshots required to demonstrate key steps.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Further Improvements
- use rebalanced dataset
- try enabling Deep Learning in AutoML Run settings
- use parameters like blocked models / allowed models
- try feature engineering (build new features)
- use manual settings for feature selection


## Resources
(1) Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
