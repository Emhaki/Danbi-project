from rest_framework import serializers
from myapp.models import SubTask, Task

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        
        team_list = [team_name.strip() for team_name in data['team'].split(",")]
        if not team_list:
            raise serializers.ValidationError("업무 생성 시, 한 개 이상의 팀을 설정해야합니다.")
        
        predefined_teams = ['단비', '다래', '블라블라', '철로', '땅이', '해태', '수피']
        for team in team_list:
            if team not in predefined_teams:
                raise serializers.ValidationError(f"정해진 7개 팀 이외에는 다른 팀에 하위업무를 부여할 수 없습니다. 정해진 팀: {predefined_teams}")

        return data

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        
        if instance.subtasks.filter(is_complete=False).exists():
            instance.is_complete = False
        else:
            instance.is_complete = True
        
        instance.save()
        return instance
    
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)

        return task