from django.db import models
from django.db.models.fields import CharField


class Student(models.Model):
    student_id = models.IntegerField(db_column='STUDENT_ID', primary_key=True)  # Field name made lowercase.
    student_name = models.CharField(db_column='STUDENT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_marks = models.IntegerField(db_column='STUDENT_MARKS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'

class WithRelation(models.Model):
    dept_id = models.AutoField(db_column='DEPT_ID', primary_key=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column='STUDENT_ID', blank=True, null=True, related_name='with_relation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'with_relation'
