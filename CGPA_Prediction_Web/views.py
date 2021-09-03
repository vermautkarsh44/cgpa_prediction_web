# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:58:25 2021

@author: DELL
"""


from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(socialmedia,prog_skills,physicalactivity,attendance,attention,reference,daily_study,exam_study, doubt_clearance, S1, S2, S3):
    import pickle
    model = pickle.load(open("cgpa_prediction_ml_model.sav", "rb"))
    '''scaled = pickle.load(open("scaler.sav", "rb"))'''
    label_encode=pickle.load(open("label encoder.sav","rb"))
    attendance=label_encode.fit_transform([attendance])
    prediction = model.predict([[socialmedia,prog_skills,physicalactivity,attendance,attention,reference,daily_study,exam_study, doubt_clearance, S1, S2, S3]])
    prediction= prediction[0]
    return prediction
    
''' if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"'''
        

# our result page view
def result(request):
    socialmedia = int(request.GET['smedia'])
    prog_skills = int(request.GET['prog'])
    physicalactivity = int(request.GET['pactivity'])
    attendance = request.GET['attendance']
    attention = int(request.GET['attention'])
    reference = int(request.GET['reference'])
    daily_study = int(request.GET['dailystudy'])
    exam_study = int(request.GET['examstudy'])
    doubt_clearance = int(request.GET['doubtclear'])
    S1 = int(request.GET['S1'])
    S2 = int(request.GET['S2'])
    S3 = int(request.GET['S3'])
    #return prediction
    
    result = getPredictions(socialmedia,prog_skills,physicalactivity,attendance,attention,reference,daily_study,exam_study, doubt_clearance, S1, S2, S3)

    return render(request, 'result.html', {'result':result})