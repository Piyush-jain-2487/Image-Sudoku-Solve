# Digit Predictor
## Requirements:
  1. open-cv - 4.5.2
  2. numpy - 1.19.2
  3. keras - 2.5.0
  4. sklearn - 0.23.2

## Performance:
  - Takes 46 mins while training on the architecture I have created(you can have your own architecture. Please don't judge mine. I have created just for knowledge).
  - parameters in model: 361,490 and all are trainable.
  - testing outputs of single image in less than second.
  - Training accuracy: 98.5%
  - Validation accuracy: 99.4%
  - Testing accuracy: 99.8%

## Image Pre-processing:
  - initial step is always to reshape and resize the image in the input(during training) format.
  - converting RBG format to Gray scale so that we can have 0-1 valued matrix which shows white and black formatted image.
  - again normalizing image matrix by dividing it with 255 and then reshaping it in (n, 32, 32, 1)
  - converting image into DataGenerator object.

## Model architecture:
  - Obviously Sequential
  - 60 filters in (5,5)Conv2D(28, 28, 60)  -> 60 filters in (5,5)Conv2D(24, 24, 60)   -> (2,2)MaxPooling(12, 12, 60)  -> 30 filters in (3,3)Conv2D (10, 10, 30) -> 30 filters in (3,3)Conv2D(8, 8, 30) -> (2,2)MaxPooling(4, 4, 30) -> Dropout(4, 4, 30) -> Flatten -> Fully-connected


## Dataset:
  - Used own created dataset by downloading images over some sites.
  - after preprocessing distributed dataset in 3 parts:
    - Training : Testing : Validation = 64 : 20 : 16
  - With the randomness of 650 images
  
 ![image](https://user-images.githubusercontent.com/47841108/124878495-cc20ae80-dfe9-11eb-9315-553befdd1441.png)

## Saving model and Creating prediction on not familiar dataset:
  - Saved with name digit_predictor.h5
  - prediction required image to be pre-processed and it outputs a numerical value along with confidence.
