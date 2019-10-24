# Comparing-Physical-Attractiveness-of-Employees-Across-Companies

For whatever unjustified reason, I subscribed to LinkedIn Premium. In order to squeeze some value out of that, I used it to scrape people's profile pictures (LinkedIn limit-rates how many profiles you can browse), grouped by company in order to find out which company has the most attractive employees! 

I trained a neural network using Tensorflow/Keras and transfer learning from ImageNet to predict the physical attractiveness of a person. The training data was obtained from here https://chicagofaces.org/default/, and my "test" data was the linkedin pictures that I scraped. 

I also let the model rate my face as well, and I was placed in the 55 percentile! XD 
