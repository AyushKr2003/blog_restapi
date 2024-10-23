# CategoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoryGet**](CategoryApi.md#categoryGet) | **GET** /category | 
[**categoryIdDelete**](CategoryApi.md#categoryIdDelete) | **DELETE** /category/{id} | 
[**categoryIdGet**](CategoryApi.md#categoryIdGet) | **GET** /category/{id} | 
[**categoryIdPut**](CategoryApi.md#categoryIdPut) | **PUT** /category/{id} | 
[**categoryPost**](CategoryApi.md#categoryPost) | **POST** /category | 


<a name="categoryGet"></a>
# **categoryGet**
> List categoryGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../\Models/CategorySchemas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="categoryIdDelete"></a>
# **categoryIdDelete**
> Error categoryIdDelete(id)



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

<a name="categoryIdGet"></a>
# **categoryIdGet**
> Error categoryIdGet(id)



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

<a name="categoryIdPut"></a>
# **categoryIdPut**
> CategorySchemas categoryIdPut(id, categorySchemas)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  | [default to null]
 **categorySchemas** | [**CategorySchemas**](../\Models/CategorySchemas.md)|  |

### Return type

[**CategorySchemas**](../\Models/CategorySchemas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="categoryPost"></a>
# **categoryPost**
> CategorySchemas categoryPost(categorySchemas)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorySchemas** | [**CategorySchemas**](../\Models/CategorySchemas.md)|  |

### Return type

[**CategorySchemas**](../\Models/CategorySchemas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

