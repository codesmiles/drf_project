from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics,mixins
from rest_framework.decorators import APIView
from .models import Comment
from .serializers import CommentSerializer

from django.shortcuts import get_object_or_404, get_list_or_404

# # CLASS BASED METHODS
# class CommentListCreateView(APIView):
#     serializer_class = CommentSerializer
    
#     def get(self, request: Request, *args, **kwargs) -> Response:
#         comments = Comment.objects.all() # or get_list_or_404
#         serializer = self.serializer_class(instance=comments, many=True)
#         response = {
#             "successful": True,
#             "response": "comments",
#             "data": serializer.data
#             }
#         return Response(response, status=status.HTTP_200_OK)
    
#     def post(self, request: Request, *args, **kwargs) -> Response:
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "successful": True,
#                 "response": "comment Created",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         response = {
#             "successful": False,
#             "response": "errors",
#             "data": serializer.errors
#         }
#         return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    
   
   
# class CommentsRetrieveUpdateAndDeleteView(APIView):
#     serializer_class = CommentSerializer
#     response = {
#         "successful": True,
#         "response": "comment",
#         "data": None,
#         }
     
#     def get(self, request: Request, comment_id, *args, **kwargs) -> Response:
#         comments = get_object_or_404(Comment, pk=comment_id)
#         serializer = self.serializer_class(instance=comments)
#         self.response["data"] = serializer.data
#         return Response(data=self.response, status=status.HTTP_200_OK)
    
#     def put(self, request: Request, comment_id, *args, **kwargs) -> Response:
#         comments = get_object_or_404(Comment, pk=comment_id)
#         serializer = self.serializer_class(instance=comments, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             self.response["comments"] = serializer.data
#             return Response(data=self.response, status=status.HTTP_200_OK)
        
#         self.response["successful"] = False
#         self.response["data"] = serializer.errors
#         return Response(data=self.response, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request: Request, comment_id, *args, **kwargs) -> Response:
#         comments = get_object_or_404(Comment, pk=comment_id)
#         comments.delete()
#         return Response(data=self.response, status=status.HTTP_204_NO_CONTENT)
   

# GENERICS AND MIXINS
class CommentListCreateView(generics.GenericAPIView):
    serializer_class = CommentSerializer
    response = {
        "successful": True,
        "response": "comment",
        "data": None,
        }
    
    
    
class CommentsRetrieveUpdateAndDeleteView(APIView):
    serializer_class = CommentSerializer
    response = {
        "successful": True,
        "response": "comment",
        "data": None,
        }
      