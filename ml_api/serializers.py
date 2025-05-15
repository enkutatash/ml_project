from rest_framework import serializers

class PredictionNamedSerializer(serializers.Serializer):
    age = serializers.FloatField()
    study_hours_per_day = serializers.FloatField()
    social_media_hours = serializers.FloatField()
    netflix_hours = serializers.FloatField()
    attendance_percentage = serializers.FloatField()
    sleep_hours = serializers.FloatField()
    exercise_frequency = serializers.FloatField()
    mental_health_rating = serializers.FloatField()
    dq_e = serializers.IntegerField()
    pel_e = serializers.IntegerField()
    iq_e = serializers.IntegerField()
    gender_Male = serializers.IntegerField()
    gender_Other = serializers.IntegerField()
    part_time_job_Yes = serializers.IntegerField()
    extracurricular_participation_Yes = serializers.IntegerField()
    model = serializers.ChoiceField(choices=['linear', 'ridge', 'lasso', 'random_forest'])

    def get_feature_array(self):
        feature_names = [
            'age',
            'study_hours_per_day',
            'social_media_hours',
            'netflix_hours',
            'attendance_percentage',
            'sleep_hours',
            'exercise_frequency',
            'mental_health_rating',
            'dq_e',
            'pel_e',
            'iq_e',
            'gender_Male',
            'gender_Other',
            'part_time_job_Yes',
            'extracurricular_participation_Yes',
        ]
        return [self.validated_data[f] for f in feature_names]
