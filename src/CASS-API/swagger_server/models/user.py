# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, birth_date: str=None, last_name_1: str=None, last_name_2: str=None, nid: str=None, user_name: str=None, email: str=None, password: str=None, role: str=None):  # noqa: E501
        """User - a model defined in Swagger

        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param birth_date: The birth_date of this User.  # noqa: E501
        :type birth_date: str
        :param last_name_1: The last_name_1 of this User.  # noqa: E501
        :type last_name_1: str
        :param last_name_2: The last_name_2 of this User.  # noqa: E501
        :type last_name_2: str
        :param nid: The nid of this User.  # noqa: E501
        :type nid: str
        :param user_name: The user_name of this User.  # noqa: E501
        :type user_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param role: The role of this User.  # noqa: E501
        :type role: str
        """
        self.swagger_types = {
            'name': str,
            'birth_date': str,
            'last_name_1': str,
            'last_name_2': str,
            'nid': str,
            'user_name': str,
            'email': str,
            'password': str,
            'role': str
        }

        self.attribute_map = {
            'name': 'name',
            'birth_date': 'birth_date',
            'last_name_1': 'last_name_1',
            'last_name_2': 'last_name_2',
            'nid': 'nid',
            'user_name': 'user_name',
            'email': 'email',
            'password': 'password',
            'role': 'role'
        }
        self._name = name
        self._birth_date = birth_date
        self._last_name_1 = last_name_1
        self._last_name_2 = last_name_2
        self._nid = nid
        self._user_name = user_name
        self._email = email
        self._password = password
        self._role = role

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.


        :param name: The name of this User.
        :type name: str
        """

        self._name = name

    @property
    def birth_date(self) -> str:
        """Gets the birth_date of this User.


        :return: The birth_date of this User.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str):
        """Sets the birth_date of this User.


        :param birth_date: The birth_date of this User.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def last_name_1(self) -> str:
        """Gets the last_name_1 of this User.


        :return: The last_name_1 of this User.
        :rtype: str
        """
        return self._last_name_1

    @last_name_1.setter
    def last_name_1(self, last_name_1: str):
        """Sets the last_name_1 of this User.


        :param last_name_1: The last_name_1 of this User.
        :type last_name_1: str
        """

        self._last_name_1 = last_name_1

    @property
    def last_name_2(self) -> str:
        """Gets the last_name_2 of this User.


        :return: The last_name_2 of this User.
        :rtype: str
        """
        return self._last_name_2

    @last_name_2.setter
    def last_name_2(self, last_name_2: str):
        """Sets the last_name_2 of this User.


        :param last_name_2: The last_name_2 of this User.
        :type last_name_2: str
        """

        self._last_name_2 = last_name_2

    @property
    def nid(self) -> str:
        """Gets the nid of this User.


        :return: The nid of this User.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid: str):
        """Sets the nid of this User.


        :param nid: The nid of this User.
        :type nid: str
        """

        self._nid = nid

    @property
    def user_name(self) -> str:
        """Gets the user_name of this User.


        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        """Sets the user_name of this User.


        :param user_name: The user_name of this User.
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def role(self) -> str:
        """Gets the role of this User.


        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this User.


        :param role: The role of this User.
        :type role: str
        """

        self._role = role
