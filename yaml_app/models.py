from django.db import models
import mptt

class YamlElement(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200,null=True,blank=True)
    value_type = models.CharField(max_length=10,null=True,blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    @classmethod
    def create(cls, key, value=None, parent=None):
        return cls(key=key, value=value, value_type=str(type(value)), parent=parent)

    def __str__(self):
        return self.key

mptt.register(YamlElement, level_attr = 'mptt_level', order_insertion_by = ['key'])

class YamlModel(models.Model):
    model_name = models.CharField(max_length=50)
    elements = models.ForeignKey(YamlElement,on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

def save_model_elements(yaml_dict,parent=None):
    if type(yaml_dict)==dict:
        for key in yaml_dict:
            if type(yaml_dict[key])!=dict and type(yaml_dict[key])!=list:
                element = YamlElement.create(key=key,value=yaml_dict[key],parent=parent)
                #print("Element with key {} and value {}. Parent: {}".format(key,yaml_dict[key],parent))
                element.save()
            else:
                element = YamlElement.create(key=key,parent=parent)
                #print("Element with key {} and parent {}".format(key,parent))
                element.save()

                if parent is None:
                    # Root element
                    yaml_model = YamlModel(model_name=key, elements=element)
                    #print("Create model with {} name. Head: {}".format(key, element))
                    yaml_model.save()

                save_model_elements(yaml_dict[key],element)

    elif type(yaml_dict)==list:
        for element in yaml_dict:
            if type(element)!=dict and type(element)!=list:
                element = YamlElement.create(key=element,parent=parent)
                #print("{} in list with parent {}.".format(element,parent))
                element.save()
            elif type(element)==dict:
                element = YamlElement(key="dict",parent=parent)
                #print("Dict created below {}.".format(parent))
                element.save()
            elif type(element)==list:
                element = YamlElement(key="list",parent=parent)
                #print("List created below {}.".format(parent))
                element.save()
    else:
        print("Fault")
