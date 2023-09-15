from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    series_id: str,
    *,
    user_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    season: Union[Unset, None, int] = UNSET,
    season_id: Union[Unset, None, str] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    start_item_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    json_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(fields, Unset):
        if fields is None:
            json_fields = None
        else:
            json_fields = []
            for fields_item_data in fields:
                fields_item = fields_item_data.value

                json_fields.append(fields_item)

    params["fields"] = json_fields

    params["season"] = season

    params["seasonId"] = season_id

    params["isMissing"] = is_missing

    params["adjacentTo"] = adjacent_to

    params["startItemId"] = start_item_id

    params["startIndex"] = start_index

    params["limit"] = limit

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        if enable_image_types is None:
            json_enable_image_types = None
        else:
            json_enable_image_types = []
            for enable_image_types_item_data in enable_image_types:
                enable_image_types_item = enable_image_types_item_data.value

                json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    params["sortBy"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Shows/{seriesId}/Episodes".format(
            seriesId=series_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    season: Union[Unset, None, int] = UNSET,
    season_id: Union[Unset, None, str] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    start_item_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Gets episodes for a tv season.

    Args:
        series_id (str):
        user_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        season (Union[Unset, None, int]):
        season_id (Union[Unset, None, str]):
        is_missing (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        start_item_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        season=season,
        season_id=season_id,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        start_item_id=start_item_id,
        start_index=start_index,
        limit=limit,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    season: Union[Unset, None, int] = UNSET,
    season_id: Union[Unset, None, str] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    start_item_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Gets episodes for a tv season.

    Args:
        series_id (str):
        user_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        season (Union[Unset, None, int]):
        season_id (Union[Unset, None, str]):
        is_missing (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        start_item_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return sync_detailed(
        series_id=series_id,
        client=client,
        user_id=user_id,
        fields=fields,
        season=season,
        season_id=season_id,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        start_item_id=start_item_id,
        start_index=start_index,
        limit=limit,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    season: Union[Unset, None, int] = UNSET,
    season_id: Union[Unset, None, str] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    start_item_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Gets episodes for a tv season.

    Args:
        series_id (str):
        user_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        season (Union[Unset, None, int]):
        season_id (Union[Unset, None, str]):
        is_missing (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        start_item_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        season=season,
        season_id=season_id,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        start_item_id=start_item_id,
        start_index=start_index,
        limit=limit,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    season: Union[Unset, None, int] = UNSET,
    season_id: Union[Unset, None, str] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    start_item_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Gets episodes for a tv season.

    Args:
        series_id (str):
        user_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        season (Union[Unset, None, int]):
        season_id (Union[Unset, None, str]):
        is_missing (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        start_item_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            series_id=series_id,
            client=client,
            user_id=user_id,
            fields=fields,
            season=season,
            season_id=season_id,
            is_missing=is_missing,
            adjacent_to=adjacent_to,
            start_item_id=start_item_id,
            start_index=start_index,
            limit=limit,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            sort_by=sort_by,
        )
    ).parsed
