from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParentalRating")


@_attrs_define
class ParentalRating:
    """Class ParentalRating.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        value (Union[Unset, int]): Gets or sets the value.
    """

    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        value = d.pop("Value", UNSET)

        parental_rating = cls(
            name=name,
            value=value,
        )

        return parental_rating
