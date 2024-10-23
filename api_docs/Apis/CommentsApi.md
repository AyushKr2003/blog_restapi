# CommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commentsGet**](CommentsApi.md#commentsGet) | **GET** /comments | 
[**commentsIdDelete**](CommentsApi.md#commentsIdDelete) | **DELETE** /comments/{id} | 
[**commentsIdGet**](CommentsApi.md#commentsIdGet) | **GET** /comments/{id} | 
[**commentsIdPut**](CommentsApi.md#commentsIdPut) | **PUT** /comments/{id} | 
[**commentsPost**](CommentsApi.md#commentsPost) | **POST** /comments | 


<a name="commentsGet"></a>
# **commentsGet**
> List commentsGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../\Models/PlainComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="commentsIdDelete"></a>
# **commentsIdDelete**
> commentsIdDelete(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="commentsIdGet"></a>
# **commentsIdGet**
> PlainComment commentsIdGet(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  | [default to null]

### Return type

[**PlainComment**](../\Models/PlainComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="commentsIdPut"></a>
# **commentsIdPut**
> PlainComment commentsIdPut(id, plainComment)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  | [default to null]
 **plainComment** | [**PlainComment**](../\Models/PlainComment.md)|  |

### Return type

[**PlainComment**](../\Models/PlainComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="commentsPost"></a>
# **commentsPost**
> PlainComment commentsPost(plainComment)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plainComment** | [**PlainComment**](../\Models/PlainComment.md)|  |

### Return type

[**PlainComment**](../\Models/PlainComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

