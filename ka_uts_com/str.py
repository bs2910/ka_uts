# coding=utf-8

from datetime import datetime
import re
import orjson
import traceback

from typing import Any, List, Dict

T_Arr = List[Any]
T_Dic = Dict[Any, Any]
T_AoA = List[T_Arr]

TN_Int = None | int
TN_Float = None | float
TN_Str = None | str
TN_AoA = None | T_AoA
TN_Arr = None | T_Arr
TN_Dic = None | T_Dic
TN_Datetime = None | datetime


class Str:
    """ Manage String Class
    """
    @staticmethod
    def sh_date(string: str, fmt: TN_Str = None) -> TN_Datetime:
        """ show string as date using the format string
        """
        try:
            if fmt is None:
                fmt = "%m/%d/%Y"
            _date: TN_Datetime = datetime.strptime(string, fmt)
            return _date
        except Exception:
            print(traceback.format_exc())
            return None

    @staticmethod
    def lchop(string: str, prefix: str) -> str:
        """ return substring of string which starts at the
            end of the contained prefix
        """
        if string.startswith(prefix):
            return string[len(prefix):]
        return string

    @staticmethod
    def rchop(string: str, suffix: str) -> str:
        """ return substring of string which ends at the
            beginning of the contained suffix
        """
        if suffix and string.endswith(suffix):
            return string[:-len(suffix)]
        return string

    @staticmethod
    def strip_multiple_chars(string: str, chars: str) -> str:
        """ replace multiple characters in string
        """
        return string.translate(str.maketrans("", "", chars))

    @staticmethod
    def is_odd(string: str) -> bool:
        """ check if string is odd number
        """
        if string.isnumeric():
            if int(string) % 2 == 0:
                return False
            return True
        else:
            return False

    @staticmethod
    def is_integer(string: str) -> bool:
        """ check if string is integer
        """
        if string[0] in ('-', '+'):
            return string[1:].isdigit()
        return string.isdigit()

    @staticmethod
    def is_boolean(string: str) -> bool:
        """ check if string is boolean
        """
        if string.strip().lower() in ['true', 'false']:
            return True
        return False

    @staticmethod
    def is_undefined(string: TN_Str) -> bool:
        """ check if string is undefined (None or empty)
        """
        if string is None or string == '':
            return True
        return False

    @staticmethod
    def nvl(string: TN_Str) -> TN_Str:
        """ nvl function similar to SQL NVL function
        """
        if string is None:
            return ''
        return string

    @staticmethod
    def strip_n(string: str) -> str:
        """ Replace new line characters by Blanks and strip Blanks
        """
        return string.replace('\n', ' ').strip()

    @staticmethod
    def remove(string: str, a_to_remove: T_Arr) -> str:
        """ remove all character of a list
        """
        for to_remove in a_to_remove:
            string = string.replace(to_remove, '')
        return string

    @staticmethod
    def sh_boolean(string: str) -> bool:
        """ Show string as boolean if string is a boolean
        """
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False
        else:
            raise ValueError

    @staticmethod
    def sh_float(string: str) -> TN_Float:
        """ Returns Float if string is of Type Float
            otherwise None
        """
        try:
            return float(string)
        except Exception:
            print(traceback.format_exc())
            return None

    @staticmethod
    def sh_int(string: str) -> TN_Int:
        """ Returns Int if string is of Type Int
            otherwise None
        """
        try:
            return int(string)
        except ValueError:
            return None

    @staticmethod
    def sh_dic(string: str) -> TN_Dic:
        """ Returns Dic if string is of Type Json-String
            otherwise None
        """
        try:
            return orjson.loads(string)
        except Exception:
            # print(f"string = {string}")
            print(traceback.format_exc())
            return None

    @staticmethod
    def sh_arr(string: str) -> TN_Arr:
        """ Show valid Array string as Array
        """
        try:
            return orjson.loads(string)
        except Exception:
            print(traceback.format_exc())
            return None

    @staticmethod
    def sh_aoa(string: str) -> TN_AoA:
        """ Show valid Array string as Array
        """
        try:
            return orjson.loads(string)
        except Exception:
            print(traceback.format_exc())
            return None

    @staticmethod
    def sh_first_item(string: str) -> Any:
        """ Show first substring of string
        """
        return string.split()[0]

    @classmethod
    def sh_a_int(cls, string: str, sep: str) -> T_Arr:
        """ Show first substring of string
        """
        # arr = string.split(sep)
        arr = re.split(sep, string)
        arr_new = []
        for item in arr:
            _item = item.strip()
            if not isinstance(_item, str):
                continue
            if not _item.isdigit():
                continue
            arr_new.append(cls.sh_int(_item))
        return arr_new

    @classmethod
    def sh_a_str(
            cls, string: str, sep: str, a_exclude: TN_Arr = None) -> Any:
        """ Show first substring of string
        """
        # arr = string.split(sep)
        arr = re.split(sep, string)

        if a_exclude is None:
            _arr = arr
        else:
            _arr = []
            for item in arr:
                _item = item.strip()
                if _item not in a_exclude:
                    _arr.append(_item)

        arr_new = []
        for item in _arr:
            if isinstance(item, str):
                arr_new.append(item.strip())
            elif isinstance(item, int):
                arr_new.append(str(item))
            else:
                arr_new.append(item)

        return arr_new

    @classmethod
    def sh_a_obj(
            cls, string: str, sep: str, a_exclude: TN_Arr = None) -> Any:
        """ Show first substring of string
        """
        # arr = string.split(sep)
        arr = re.split(sep, string)

        if a_exclude is None:
            _arr = arr
        else:
            _arr = []
            for item in arr:
                _item = item.strip()
                if _item not in a_exclude:
                    _arr.append(_item)

        arr_new: T_Arr = []
        for item in _arr:
            if isinstance(item, str):
                _item = item.strip()
                if _item.isdigit():
                    _item = cls.sh_int(_item)
                    arr_new.append(_item)
                else:
                    arr_new.append(_item)
            else:
                arr_new.append(item)

        return arr_new
