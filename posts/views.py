#  REST FRAMEWORK VIEWS
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# FUNCTION BASED METHODS
@api_view(http_method_names=["GET", "POST"])
def home(request:Request):
    
    # if it's a post request
    if(request.method =="POST"):
        data = request.data
        response = {
            "message":"hello world from the post request",
            "data": data
        }
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {
        "message":"hello world"
    }
    return Response(data=response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET","POST"])
def list_or_create_posts(request:Request):
    
    #---------------------------  TO CREATE A POST --------------------------------
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            response = {
                "successful": True,
                "response": "Success",
                "data": serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        
        response = {
            "successful": False,
            "response": "Error",
            "data": serializer.errors
        }
        return Response(data=response,status=status.HTTP_201_CREATED)
    #------------------------------------------------------------------------------
    
    #----------------------------TO GETALL POSTS---------------------------------
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts,many=True)
    
    response = {
        "successful": True,
        "response": "Success",
        "data": serializer.data
    }
    return Response(data=response,status=status.HTTP_200_OK)
    #------------------------------------------------------------------------------

    #----------------------------FIND SINGLE POSTS --------------------------------
@api_view(http_method_names=["GET"])
def get_single_post(request:Request, post_id: int) -> Response:
    post = get_object_or_404(Post, pk=post_id) 
    
    serializer = PostSerializer(instance=post)
    response = {
        "successful": True,
        "response": "Success",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK) 
#------------------------------------------------------------------------------


# ----------------------------UPDATE SINGLE POSTS ----------------------------
@api_view(http_method_names=["PUT"])
def update_post(request:Request, post_id: int) -> Response:
    post = get_object_or_404(Post, pk=post_id) 
    data = request.data
    serializer = PostSerializer(instance=post, data=data)
    
    if serializer.is_valid():
        serializer.save()
        response = {
            "successful": True,
            "response": "Success",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    response = {
        "successful": False,
        "response": "errors",
        "data": serializer.errors
    }
    return Response(data=response, status=status.HTTP_200_OK)
#------------------------------------------------------------------------------

# -------------------------DELETE POST------------------------------------------
@api_view(http_method_names=["DELETE"])
def delete_post(request:Request, post_id: int) -> Response:
    post = get_object_or_404(Post, pk=post_id) 
    post.delete()
    
    response = {
        "successful": True,
        "response": "Success",
        "data": "Post Deleted"
    }
    return Response(data=response, status=status.HTTP_204_NO_CONTENT)