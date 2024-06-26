from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from ..models.general_command_type import GeneralCommandType
from ..types import UNSET, Unset
from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.general_command_arguments import GeneralCommandArguments


T = TypeVar("T", bound="GeneralCommand")


@_attrs_define
class GeneralCommand:
    """
    Attributes:
        name (Union[Unset, GeneralCommandType]): This exists simply to identify a set of known commands.
        controlling_user_id (Union[Unset, str]):
        arguments (Union[Unset, GeneralCommandArguments]):
    """

    name: Union[Unset, GeneralCommandType] = UNSET
    controlling_user_id: Union[Unset, str] = UNSET
    arguments: Union[Unset, "GeneralCommandArguments"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.general_command_arguments import GeneralCommandArguments

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        controlling_user_id = self.controlling_user_id

        arguments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id
        if arguments is not UNSET:
            field_dict["Arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.general_command_arguments import GeneralCommandArguments

        d = src_dict.copy()
        _name = d.pop("Name", UNSET)
        name: Union[Unset, GeneralCommandType]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GeneralCommandType(_name)

        controlling_user_id = d.pop("ControllingUserId", UNSET)

        _arguments = d.pop("Arguments", UNSET)
        arguments: Union[Unset, GeneralCommandArguments]
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = GeneralCommandArguments.from_dict(_arguments)

        general_command = cls(
            name=name,
            controlling_user_id=controlling_user_id,
            arguments=arguments,
        )

        return general_command
