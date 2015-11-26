from django.db import models
# from administration.models import University


class FeatureGroup(models.Model):
    feature_name = models.CharField(max_length=150)

    def __str__(self):
        return self.feature_name


# class SubFeature(models.Model):
#     feature_group = models.ForeignKey(FeatureGroup, related_name='sub_feature_feature_group')
#     sub_feature_name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.sub_feature_name
#
#
# class Topic(models.Model):
#     org = models.ForeignKey(University, related_name='university', editable=False)
#     feature_group = models.ForeignKey(FeatureGroup, related_name='topic_feature_group')
#     sub_feature = models.ForeignKey(SubFeature, related_name='topic_sub_feature')
#     topic_subject = models.CharField(max_length=225)
#     created_date = models.DateTimeField(auto_now_add=True, editable=False)
#     modified_date = models.DateTimeField(auto_now=True, editable=False)
#
#     def __str__(self):
#         return self.topic_subject
