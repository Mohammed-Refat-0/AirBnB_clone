#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes_list = ['BaseModel', 'User', 'State',
                'City', 'Place', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, args):
        """exist the program upon reciving the command "quit"
        """
        return True

    def do_EOF(self, args):
        """exist the program upon recivig a EOF signal (ctrl+D)
        """
        return True

    def emptyline(self):
        """an empty line + ENTER dont execute anything
        """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if not args:
            print('** class name missing **')
            return
        argsl = args.split()
        class_name = argsl[0].strip()
        if class_name not in classes_list:
            print('** class doesn\'t exist **')
            return
        new_insstance = eval(class_name)()
        storage.save()
        print(new_insstance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print('** class name missing **')
            return

        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
            return

        class_name = args_list[0].strip()
        if class_name not in classes_list:
            print('** class doesn\'t exist **')
            return

        if len(args_list) < 2:
            print('** instance id missing **')
            return

        objs = storage.all()
        model = f"{class_name}.{args_list[1].strip()}"

        if model in objs:
            print(objs[model])
        else:
            print('** no instance found **')

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not args:
            print('** class name missing **')
            return

        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
            return

        class_name = args_list[0].strip()
        if class_name not in classes_list:
            print('** class doesn\'t exist **')
            return

        if len(args_list) < 2:
            print('** instance id missing **')
            return

        objs = storage.all()
        model = f"{class_name}.{args_list[1].strip()}"

        if model in objs:
            del objs[model]
            storage.save()
            return
        else:
            print('** no instance found **')

    def do_all(self, args):
        """ Prints all string representation of all instances based or not on the class name"""
        list = []
        objs = storage.all()
        if not args:
            for key, value in objs.items():
                list.append(value.__str__())
            print(list)
            return
        argsl = args.split()
        class_name = argsl[0].strip()
        if class_name not in classes_list:
            print('** class doesn\'t exist **')
            return
        for key, value in objs.items():
            if class_name == value.__class__.__name__:
                list.append(value.__str__())
        print(list)

    def do_update(sefl, args):
        """: Updates an instance based on the class name and id by adding or updating attribute"""
        if not args:
            print('** class name missing **')
            return

        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
            return

        class_name = args_list[0].strip()
        if class_name not in classes_list:
            print('** class doesn\'t exist **')
            return

        if len(args_list) < 2:
            print('** instance id missing **')
            return

        objs = storage.all()
        instance_id = args_list[1].strip()
        model = f"{class_name}.{instance_id}"

        if model not in objs:
            print('** no instance found **')
            return

        if len(args_list) < 3:
            print('** attribute name missing **')
            return

        if len(args_list) < 4:
            print('** value missing **')
            return

        attribute_name = args_list[2].strip()
        attribute_value = args_list[3]
        attribute_value = attribute_value.replace('"', ' ')
        attribute_value = attribute_value.strip()

        if attribute_name in objs[model].__dict__:
            objs[model].__dict__[attribute_name] = type(
                objs[model].__dict__[attribute_name])(attribute_value)
        else:
            setattr(objs[model], attribute_name, attribute_value)

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
