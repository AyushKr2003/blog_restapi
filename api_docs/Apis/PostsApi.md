# PostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postsGet**](PostsApi.md#postsGet) | **GET** /posts | 
[**postsIdGet**](PostsApi.md#postsIdGet) | **GET** /posts/{id} | 
[**postsPost**](PostsApi.md#postsPost) | **POST** /posts | 


<a name="postsGet"></a>
# **postsGet**
> List postsGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../\Models/PlainPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postsIdGet"></a>
# **postsIdGet**
> Error postsIdGet(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  | [default to null]

### Return type

[**Error**](../\Models/Error.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postsPost"></a>
# **postsPost**
> PlainPost postsPost(plainPost)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plainPost** | [**PlainPost**](../\Models/PlainPost.md)|  |

### Return type

[**PlainPost**](../\Models/PlainPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

