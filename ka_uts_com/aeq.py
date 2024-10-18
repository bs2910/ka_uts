# coding=utf-8

# import orjson
# import traceback

from ka_uts_com.date import Date
from ka_uts_com.str import Str

from typing import Any, Dict, List

TN_Date = None | Any

T_Arr = List[Any]
T_Dic = Dict[Any, Any]

TN_Arr = None | T_Arr
TN_Dic = None | T_Dic
TN_Str = None | str


class Aeq:
    """ Dictionary of Equates
    """
    @classmethod
    def sh_value(cls, key: str, value: Any, d_valid_parms: TN_Dic) -> Any:

        # print(f"key = {key}, type(key) = {type(key)}")
        # print(f"value = {value}, type(value) = {type(value)}")
        if not d_valid_parms:
            return value
        _type: TN_Str = d_valid_parms.get(key)
        # print(f"_type = {_type}")
        if not _type:
            return value
        if isinstance(_type, str):
            match _type:
                case 'int':
                    value = int(value)
                case 'bool':
                    value = Str.sh_boolean(value)
                case 'dict':
                    value = Str.sh_dic(value)
                case 'list':
                    value = Str.sh_arr(value)
                case '%Y-%m-%d':
                    value = Date.sh(value, _type)
                case '_':
                    match _type[0]:
                        case '[', '{':
                            _obj = Str.sh_dic(_type)
                            if value not in _obj:
                                msg = (f"parameter={key} value={value} is invalid; "
                                       f"valid values are={_obj}")
                                raise Exception(msg)

        # print(f"value = {value}, type(value) = {type(value)}")
        return value

    @classmethod
    def sh_d_eq(cls, a_s_eq: T_Arr, d_valid_parms: TN_Dic) -> T_Dic:

        d_eq = {}
        for s_eq in a_s_eq[1:]:
            key, value = s_eq.split('=')

            if d_valid_parms is not None:
                if key not in d_valid_parms:
                    msg = (f"Wrong parameter: {key}; "
                           f"valid parameters are: {d_valid_parms}")
                    raise Exception(msg)
                value = cls.sh_value(key, value, d_valid_parms)
                d_eq[key] = value
            else:
                d_eq[key] = value
        return d_eq
