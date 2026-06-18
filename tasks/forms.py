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







# class StyleMixin:
#     default='w-full p-2 border border-gray-300 rounded-lg focus:border-rose-600 focus:outline-none'

#     def apply(self):
#         for name,field in self.fields.items():
#             if isinstance(field.widget,forms.TextInput):
#                 field.widget.attrs.update({
#                     'class': self.default,
#                 })
#             elif isinstance(field.widget,forms.Textarea):
#                 field.widget.attrs.update({
#                     'class':self.default,
#                     'placeholder':"Enter Description",
#                 })
class StyleMixin:
    
    input_class = (
    "w-full px-4 py-3 "
    "bg-white border border-gray-300 rounded-xl "
    "shadow-sm "
    "placeholder:text-gray-400 "
    "focus:outline-none focus:ring-2 focus:ring-rose-500 focus:border-rose-500 "
    "transition-all duration-200")

    placeholders = {
        "username": "Enter username",
        "email": "Enter email address",
        "password": "Enter password",
        "password1": "Create password",
        "confirm_password": "Confirm password",
        "first_name": "First name",
        "last_name": "Last name",
        "title": "Enter title",
        "description": "Enter description",
    }

    

    def style_fields(self):
        for name, field in self.fields.items():

            field.widget.attrs.setdefault("class", "")
            field.widget.attrs["class"] += f" {self.input_class}"

            
            placeholder = self.placeholders.get(
                name,
                f"Enter {field.label.lower()}" if field.label else ""
            )

            field.widget.attrs.setdefault(
                "placeholder",
                placeholder
            )

            if isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.setdefault(
                    "autocomplete",
                    "email"
                )

            elif isinstance(field.widget, forms.PasswordInput):
                field.widget.attrs.setdefault(
                    "autocomplete",
                    "current-password"
                )

            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.setdefault("rows", 4)

            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = (
                    "h-4 w-4 rounded border-gray-300"
                )
                def __init__(self,*args,**kwargs):
                    super().__init__(*args,**kwargs)   
                    self.apply()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()



class TaskModelForm(StyleMixin,forms.ModelForm):
    class Meta:
        model=Task
        fields=['project','title','description','due_date','assign_to']

        widgets={
            'project':forms.Select(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
            'due_date':forms.SelectDateWidget(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
            'assign_to':forms.CheckboxSelectMultiple(attrs={'class':'p-1 border border-gray-300 rounded-lg'}),
        }


    


class TaskDetailModelForm(StyleMixin,forms.ModelForm):
    class Meta:
        model=TaskDetail
        fields=['priority','notes']
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)   
    #     self.apply()
    
