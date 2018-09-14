# Investigation on using neural networks for deconvoluion of arrival time spectrometry data.

For detailed information about the project and data see [this repository](https://github.com/simoskalfas/CIVU). 


In parallel to making the package above, I attempted to use some neural networks to solve the same problem. The functional part of this code is the regression neural network in the top directory. Although incomlete, this network does show some convergence in cross-evaluation but none when tested on real data.


An incomplete regression neural network (RNN) is also contained. However, the training data generation has not been optimised yet. The use of an RNN for this data will be interesting since the continuous variable, which is time in most applications (ex. speech recognition) is now replaced with voltage. Processing the whole three-dimentional data set is something that is missing from the rest of my attempts on this project and the attempts of the rest of the community alike.


I also used this project to expand my coding skills (beside machine learning) by using an object-oriented style, ipython notebooks and Python 3.5.
For more details on the code see docstrings inside. This project is not intended for practical use (yet).