#!/usr/bin/python3

"""
A console application
"""


import cmd
import models
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
	"""
	A console application class
	"""

	prompt = "(hbnb) "
	command_list = ["BaseModel", "User", "State", "City"]

	def emptyline(self):
		"""
		Handles the empty line prompt
		"""
		return

	def do_quit(self, line):
		"""
		Quit command to exit the program
		"""
		return True

	def help_quit(self):
		"""
		Quit command to exit the program (help)
		"""
		print("{}".format("Quit command to exit the program\n"))

	def do_EOF(self, line):
		"""
		Quit command on End of File
		"""
		return True

	def do_create(self, line):
		"""
		Creates a new instance of BaseModel
		"""
		command = self.parseline(line)[0]
		if command is None:
			print("** class name missing **")
		elif command not in self.command_list:
			print("** class doesn't exist **")
		else:
			new_obj = eval(command)()
			new_obj.save()
			print(new_obj.id)

	def help_create(self):
		"""
		Creates a new instance of `BaseModel` (help)
		"""
		print("{}".format("Creates a new instance of BaseModel\n"))

	def do_show(self, line):
		"""
		Prints the string representation of an instance
		based on the class name and id
		"""
		class_name = self.parseline(line)[0]
		class_id = self.parseline(line)[1]
		if class_name is None:
			print("** class name missing **")
		elif class_name not in self.command_list:
			print("** class doesn't exist **")
		elif class_id is None or class_id == "":
			print("** instance id missing **")
		else:
			new_inst = models.storage.all().get(class_name + "." + class_id)
			if new_inst is None:
				print("** no instance found **")
			else:
				print(new_inst)

	def help_show(self):
		"""
		Prints the string representation of an instance
		based on the class name and id
		"""
		print("{}".format("Prints the string representation based on class\n"))

	def do_destroy(self, line):
		"""
		Deletes an instance based on the class name and id
		"""
		class_name = self.parseline(line)[0]
		class_id = self.parseline(line)[1]
		if class_name is None:
			print("** class name missing **")
		elif class_name not in self.command_list:
			print("** class doesn't exist **")
		elif class_id is None or class_id == "":
			print("** instance id missing **")
		else:
			key = class_name + "." + class_id
			new_inst = models.storage.all().get(key)
			if new_inst is None:
				print("** no instance found **")
			else:
				del models.storage.all()[key]
				models.storage.save()

	def help_destroy(self):
		"""
		Deletes an instance based on the class name and id (help)
		"""
		print("{}".format("Deletes instance based on the class name and id\n"))
	
	def do_all(self, line):
		"""
		Prints all string representation of instances based on the class name.
		"""
		class_name = self.parseline(line)[0]
		objs = models.storage.all()
		if class_name is None:
			print([str(objs[obj]) for obj in objs])
		elif class_name in self.command_list:
			keys = objs.keys()
			print([str(objs[key]) for key in keys if key.startswith(class_name)])
		else:
			print("** class doesn't exist **")

	def help_all(self):
		"""
		Prints all string representation based or not on the class name(help)
		"""
		print("Prints string representation based or not on the class name\n")

if __name__ == '__main__':
	HBNBCommand().cmdloop()
