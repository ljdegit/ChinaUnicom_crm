########################################################################################################################
## Django 自带模块导入
########################################################################################################################
from django import forms

########################################################################################################################
## 系统自带模块导入
########################################################################################################################


########################################################################################################################
## 自建模块导入
########################################################################################################################
from .models import *



########################################################################################################################
## 添加记录
########################################################################################################################
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = FaultRecord
        exclude = ['date']




