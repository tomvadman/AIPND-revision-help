#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Tommy Vadman
# DATE CREATED: 2019-09-23                                
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
    # Loop results_dic dictionary key:image_name, value: list_of_strings)
    for image_name, result_dic_list in results_dic.items():
        
        # Create imageUrl
        image_url = images_dir + "/" + image_name
        
        # Analyze picture with classifier and specified model.
        cf_label = classifier(image_url, model)
        
        # remove whitespace and make cf_label to lower.
        cf_label = cf_label.lower().strip()
        
        # save label to results_dic_list[2]
        result_dic_list.append(cf_label)
        
        # check if cf_label exist in result_dic list.
        # save cf_label_match_pet_image returned (int) to results_dic_list[3]
        cf_label_match_pet_image_labels = cf_label_exist_in_list(cf_label, result_dic_list)
        
        result_dic_list.append(cf_label_match_pet_image_labels)
        
    return results_dic
    
def cf_label_exist_in_list(cf_label, listOfStrings):
    """
    Check if cf_label (string) exist in list.
    Functions splits cf_label string with "," and returns 1 if match found.
    Parameters: 
      cf_label - a string from classifier output.
      listOfString - a list of strings from parsed petImage file location.
     Returns:
           (int) 
           1 if cf_label exist in listOfStrings.
           0 if cf_label not exist in listOfStrings.
    """
    
    cf_label_match = 0
    # Loop label split and make each word lower and remove whitespace.
    # Because we know that result_dic.value (list) is lower and includes no whitespaces.
    for label in cf_label.split(","):
        if(label.strip() in listOfStrings):
            cf_label_match = 1
            return cf_label_match

        return cf_label_match