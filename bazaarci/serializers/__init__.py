def apply_serializer(class_or_instance, function_name, function):
        setattr(class_or_instance, function_name, function)
