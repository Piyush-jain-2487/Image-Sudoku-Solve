#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, numpy as np
import cv2
from .Utilis import *
from .sudoku import *

def run_sudoku(pathImage):
    #######################
    height = 450
    width = 450
    #######################

    #######################################
    # prepare Image #
    img = cv2.imread(pathImage)
    img = cv2.resize(img, (width, height))  
    imgBlank = np.zeros((height, width, 3), np.uint8)  
    imgThreshold = preProcess(img)
    #######################################

    #########################################################################################
    #find Contours
    imgContours = img.copy()
    imgBigContour = img.copy()
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)
    biggest, maxArea = biggestContour(contours)
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (width, height))
        imgDetectedDigits = imgBlank.copy()
        imgWarpColored = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
        #########################################################################################

        ######################################################################
        # Splitting whole sudoku in boxes for digit prediction
        model = initializePredectionModel()
        imgSolvedigits = imgBlank.copy()
        boxes = splitBoxes(imgWarpColored)
        # cv2.namedWindow("Images", cv2.WINDOW_NORMAL)
        # cv2.imshow('Images', boxes[6])
        # cv2.waitKey(0)
        numbers = getPredection(boxes, model)
        imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers, color=(255,0,255))
        numbers = np.asarray(numbers)
        posArray = np.where(numbers > 0, 0, 1)
        ######################################################################

        #############################
        #solving sudoku
        board = np.array_split(numbers,9)
        try:
            solver(board)
        except:
            pass
        #############################

        ######################################################
        #Draw Board with only solution
        flatList = []
        for sublist in board:
            for item in sublist:
                flatList.append(item)
        solvedNumbers = flatList*posArray
        imgSolvedigits = displayNumbers(imgSolvedigits, solvedNumbers)
        ######################################################

        ###################################################################
        #Overlay input sudoku and its solution on same image
        pts2 = np.float32(biggest)
        pts1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgInvWarpColored = imgBlank.copy()
        imgInvWarpColored = cv2.warpPerspective(imgSolvedigits, matrix, (width, height))
        inv_perspective = cv2.addWeighted(imgInvWarpColored, 1, img, 0.4, 1)
        imgDetectedDigits = drawGrid(imgDetectedDigits)
        imgSolvedigits = drawGrid(imgSolvedigits)
        ###################################################################

        ###################################################################
        #Show in window
        # imgArray = ([img,imgBigContour,imgDetectedDigits,inv_perspective])
        # stack = stackImages(imgArray,1)
        # cv2.namedWindow("Stacked Images", cv2.WINDOW_NORMAL)
        # cv2.imshow('Stacked Images', stack)
        # cv2.waitKey(0)
        return inv_perspective
        ###################################################################

    else:
        return "No Sudoku Found!"

