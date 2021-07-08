# Image-Sudoku-Solve

## Requirements:
  1. open-cv - 4.5.2
  2. numpy - 1.19.2
  3. keras - 2.5.0
  4. sklearn - 0.23.2
  5. django - 2.2.5

## steps:
  - created sudoku code with np-hard backtracking recursive method.
  - created sudoku box detecting and predicting digits model, so that we can know where we need to fill the output of sudoku solution.
    - used open-cv for whole image_sudoku process.
    - First we find contours of that inage to get sudoku box, which is easy due to open-cv.
    - then splitting whole sudoku(inside the contours) in boxes for digit prediction using digit_predictor.h5 model which was pre-requisite and you can find model definition in Digit Predictor folder.
    - storing numbers which are detected in some list and creating an array form board which we will input in solver() which is defined is Sudoku as discussed above.
    - Output will be in same format as input, so we are getting list as output and then overlapping that output values on input image of sudoku.
  - Then the last but not least, deployment. Created project using django to make it with some user interface as input image is uploaded and then showing output image in front of input image. 

## Performance:
  - loading takes time after upload due to image processing & prediction and getting sudoku solution.
  - result 100% solved image with correct solution.
  - It won't work for image other than sudoku(still working on validation part).
  - tried to delete input and output image after processing is over, so that it can read next image with same name as renamed in django.

## Files worked on:
  - sudoku.py
  - Image_Sudoku.py along with Utiis.py
  - models.py
  - form.py
  - views.py
  - urls.py
  - index.html
