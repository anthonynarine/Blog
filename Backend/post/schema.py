from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializers import PostSerializer

server_list_docs = extend_schema(
    responses=PostSerializer(many=True), 
    parameters=[
        OpenApiParameter(
        
        )
    ]
)