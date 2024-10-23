# UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userGet**](UsersApi.md#userGet) | **GET** /user | 
[**userIdDelete**](UsersApi.md#userIdDelete) | **DELETE** /user/{id} | 
[**userIdGet**](UsersApi.md#userIdGet) | **GET** /user/{id} | 
[**userIdPut**](UsersApi.md#userIdPut) | **PUT** /user/{id} | 
[**userLoginPost**](UsersApi.md#userLoginPost) | **POST** /user/login | 
[**userLogoutPost**](UsersApi.md#userLogoutPost) | **POST** /user/logout | 
[**userRefreshPost**](UsersApi.md#userRefreshPost) | **POST** /user/refresh | 
[**userSignupPost**](UsersApi.md#userSignupPost) | **POST** /user/signup | 


<a name="userGet"></a>
# **userGet**
> List userGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../\Models/User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userIdDelete"></a>
# **userIdDelete**
> Error userIdDelete(id)



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

<a name="userIdGet"></a>
# **userIdGet**
> Error userIdGet(id)



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

<a name="userIdPut"></a>
# **userIdPut**
> Error userIdPut(id)



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

<a name="userLoginPost"></a>
# **userLoginPost**
> Error userLoginPost(userLogin)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userLogin** | [**UserLogin**](../\Models/UserLogin.md)|  |

### Return type

[**Error**](../\Models/Error.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="userLogoutPost"></a>
# **userLogoutPost**
> Error userLogoutPost()



### Parameters
This endpoint does not need any parameter.

### Return type

[**Error**](../\Models/Error.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userRefreshPost"></a>
# **userRefreshPost**
> Error userRefreshPost()



### Parameters
This endpoint does not need any parameter.

### Return type

[**Error**](../\Models/Error.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userSignupPost"></a>
# **userSignupPost**
> User userSignupPost(user)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](../\Models/User.md)|  |

### Return type

[**User**](../\Models/User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

