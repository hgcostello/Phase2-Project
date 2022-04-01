# Seller Assistance in King County
## Mattie Gittings and Henry Costello 
## DS Bootcamp: Phase 2


## Business Problem 
### In this project we decided to take a look at ways that we could optimize the way in which current homeowners in King County, Washington are able to determine the estimated market value of their house. We pulled data from the KC House Data file as well as from the Housing Price Index. Using both of these data sources we were able to create a model for predicting the estimated price for a house in Kings County. This would be beneficial for King County residents who are considering selling their houses to be able to get a good sense of how much their house would be worth. 



## Housing Price Index (HPI) 
### One of the factors that we considered when looking at price was the Housing Price Index. This is a "broad meansure of the movement of single-family property prices in the United States" (Investopedia). This metric is provided by the Federal Housing Finance Agency (FHFA) and can be mapped to individual housing units. 

![alt text](https://github.com/hgcostello/Phase2-Project/blob/MattieGittings_Work/7b89d8d5e15e7d4a58c60a4f8e8d08ef.png)

## Model 
### In creating our model we looked through the data files and decided on which predictors would be best to output the most accurate estimate. After analyzing the data we decided on the predictors of Bedrooms, Bathrooms, Year Built, On the Waterfront, Square-Footage of the house, Square-Footage of the Lot, Condition of the home. With these variables we were able to achieve a R**2 value of 0.72. This means that 72% of the model is a good fit. As we can see below, when practically applying the model it performs well relative to actual values. We have images showing the Zillow estimate for the value of a home. 

![alt text](https://github.com/hgcostello/Phase2-Project/blob/MattieGittings_Work/Screen%20Shot%202022-04-01%20at%2012.49.44%20PM.png)
### When we compare this with the model we have built we can see that the difference is marginal. 

![alt text](https://github.com/hgcostello/Phase2-Project/blob/MattieGittings_Work/Screen%20Shot%202022-04-01%20at%2012.38.42.jpeg)
## Conclusion 
 ### While our model does provide the price with relative accuracy there are many more things we could do to be able to make our model even more accurate.  To begin with we could expand the data set that we are using. The KC House Data file only contains sale information from 2014-2015, to have a more accurate model we would need to have more up to date information. As well we would like to include more factors to determine a more accurate price. This could include incorporating whether a property is located on the waterfront or not, or wherter a propoerty is an apartment building etc. 
