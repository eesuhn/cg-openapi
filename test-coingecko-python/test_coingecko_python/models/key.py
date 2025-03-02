# coding: utf-8

"""
    CoinGecko API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Key(BaseModel):
    """
    Key
    """ # noqa: E501
    plan: Optional[StrictStr] = None
    rate_limit_request_per_minute: Optional[Union[StrictFloat, StrictInt]] = None
    monthly_call_credit: Optional[Union[StrictFloat, StrictInt]] = None
    current_total_monthly_calls: Optional[Union[StrictFloat, StrictInt]] = None
    current_remaining_monthly_calls: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["plan", "rate_limit_request_per_minute", "monthly_call_credit", "current_total_monthly_calls", "current_remaining_monthly_calls"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Key from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Key from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan": obj.get("plan"),
            "rate_limit_request_per_minute": obj.get("rate_limit_request_per_minute"),
            "monthly_call_credit": obj.get("monthly_call_credit"),
            "current_total_monthly_calls": obj.get("current_total_monthly_calls"),
            "current_remaining_monthly_calls": obj.get("current_remaining_monthly_calls")
        })
        return _obj


