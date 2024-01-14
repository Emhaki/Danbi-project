
from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from myapp.models import SubTask, Task
from myapp.serializers import SubTaskSerializer, TaskSerializer, TeamSerializer
from myapp.models import Team

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def create(self, request, *args, **kwargs):
        
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        
        predefined_teams = ['단비', '다래', '블라블라', '철로', '땅이', '해태', '수피']

        
        teams = serializer.validated_data.get('teams', [])
        for team in teams:
            if team.name not in predefined_teams:
                raise serializers.ValidationError(f"정해진 7개 팀 이외에는 다른 팀에 하위업무를 부여할 수 없습니다. 정해진 팀: {predefined_teams}")

        serializer.save()

        # try:
        #     task = Task.objects.latest('created_at')
        # except task is None:
        #     raise serializers.ValidationError(f"Task 값이 없습니다.")
        # print(task)
        subtask_serializer = SubTaskSerializer(data=serializer.data)
        subtask_serializer.is_valid(raise_exception=True)
        subtask_serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer