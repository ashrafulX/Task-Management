from django import forms
from tasks.models import Task,TaskDetail


# class TaskForm(forms.Form):
#     task_title=forms.CharField(max_length=100,label="Task Title")
#     description=forms.CharField(label="Task descritpion",widget=forms.Textarea)
#     due_date=forms.DateField(widget=forms.SelectDateWidget,label="Due Date")
#     assigned_to=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Assigned To")

#     def __init__(self,*args,**kwargs):
#         emp=kwargs.pop('employees',None)
#         # print(emp)
#         super().__init__(*args,**kwargs)
#         self.fields['assigned_to'].choices=[(e.id, e.name) for e in emp]

class StyleMixin:
    default='w-full p-2 border border-gray-300 rounded-lg focus:border-rose-600 focus:outline-none'

    def apply(self):
        for name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default,
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default,
                    'placeholder':"Enter Description",
                })

class TaskModelForm(StyleMixin,forms.ModelForm):
    class Meta:
        model=Task
        fields=['project','title','description','due_date','assign_to']

        widgets={
            'project':forms.Select(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
            'due_date':forms.SelectDateWidget(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
            'assign_to':forms.CheckboxSelectMultiple(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
        }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        self.apply()


class TaskDetailModelForm(StyleMixin,forms.ModelForm):
    class Meta:
        model=TaskDetail
        fields=['priority','notes']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        self.apply()
    