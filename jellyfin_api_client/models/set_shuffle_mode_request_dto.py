from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..models.group_shuffle_mode import GroupShuffleMode
from ..types import UNSET, Unset


T = TypeVar("T", bound="SetShuffleModeRequestDto")


@_attrs_define
class SetShuffleModeRequestDto:
    """Class SetShuffleModeRequestDto.

    Attributes:
        mode (Union[Unset, GroupShuffleMode]): Enum GroupShuffleMode.
    """

    mode: Union[Unset, GroupShuffleMode] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _mode = d.pop("Mode", UNSET)
        mode: Union[Unset, GroupShuffleMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupShuffleMode(_mode)

        set_shuffle_mode_request_dto = cls(
            mode=mode,
        )

        return set_shuffle_mode_request_dto
