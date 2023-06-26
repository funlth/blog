# from django.shortcuts import render
#
# # Create your views here.
# # chat/views.py
# from django.shortcuts import render
#
# def index(request):
#     return render(request, 'chat/index.html', {})
#
# def room(request, room_name):
#     return render(request, 'chat/home.html', {
#         'room_name': room_name
#     })
#
#
# import nltk
# import random
#
# from django.shortcuts import render
# from django.http import JsonResponse
#
# # load the dataset
# from nltk.corpus import movie_reviews
#
# # extract features from the dataset and identify the category to which this feature belongs
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
#
# # shuffle the documents
# random.shuffle(documents)
#
# # extract features from the dataset
# all_words = []
# for w in movie_reviews.words():
#     all_words.append(w.lower())
#
# # compute the frequency distribution of the words in the dataset
# all_words = nltk.FreqDist(all_words)
#
# # obtain the 2000 most frequently occurring words in the dataset
# word_features = list(all_words.keys())[:2000]
#
#
# # extract features from a document
# def document_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#     return features
#
#
# # extract the featureset from the dataset
# featuresets = [(document_features(d), c) for (d, c) in documents]
#
# # split the dataset into training and testing datasets
# train_set, test_set = featuresets[100:], featuresets[:100]
#
# # train a naive bayes classifier on the training dataset with the high information gain feature selector
# classifier = nltk.NaiveBayesClassifier.train(train_set)
#
#
# # render chatbot interface
# def chatRobot(request):
#     # get the user's message
#     msg = request.GET.get('msg', '')
#
#     # if message is not empty
#     if msg != '':
#         # extract the feature of the user's message
#         msg_feature = document_features(msg.split())
#
#         # use the trained classifier to predict the category of the user's message
#         result_label = classifier.classify(msg_feature)
#
#         # generate the response based on the predicted category
#         if result_label == 'pos':
#             response_msg = "你说的真好！"
#         else:
#             response_msg = "抱歉，我不明白你的意思。"
#
#         # package the response and send it back to client
#         data = {
#             'response': response_msg
#         }
#         return JsonResponse(data)
#
#     # if message is empty
#     return render(request, "chat/index_robot.html")



from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Room, ChatMessage


def room(request, room_name):
    room, _ = Room.objects.get_or_create(name=room_name)
    messages = ChatMessage.objects.filter(room=room).order_by('created_time')
    context = {
        'room_name': room_name,
        'messages': messages,
    }
    return render(request, 'chat/room.html', context)


@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        room_name = request.POST.get('room')
        user_name = request.POST.get('user')
        content = request.POST.get('content')
        if not room_name or not user_name or not content:
            return JsonResponse({'success': False})
        room, _ = Room.objects.get_or_create(name=room_name)
        message = ChatMessage(room=room, user=user_name, content=content)
        message.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})