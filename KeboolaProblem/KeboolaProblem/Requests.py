import requests
import csv
resp = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
if resp.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    questions = resp.json()['questions'] #hold all questions
    responses = resp.json()['responses'] #hold all responses
    fields=[] #array to hold all quesion ids
    for question in questions:
        fields.append(question['id'])
    filePath = input('Please enter the path of the CSV file that you want to store data in:')
    
    temp = {} #temp dic to store corresponding answer to question
    with open(filePath, 'w', encoding='utf-8') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        for response in responses:
            answers = response['answers']
            if answers != {}:
                for question in questions:
                    questionId = question['id']
                    if questionId in answers.keys():
                        temp[questionId] = answers[questionId]
                    else:
                        temp[questionId] = 'NaN'
                writer.writerow(temp)
