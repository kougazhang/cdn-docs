## URL parameters key of current facilitates

- aliyun: [auth_key](https://help.aliyun.com/zh/cdn/user-guide/configure-url-signing?spm=a2c4g.11186623.0.0.2302a573ifTGfy)
- upyun: _upt
- tencent: [sign](https://cloud.tencent.com/document/product/228/41623)
- huawei_cloud: [auth_key](https://support.huaweicloud.com/usermanual-cdn/cdn_01_0040.html)
- qiniu: [sign](https://developer.qiniu.com/fusion/3841/timestamp-hotlinking-prevention-fusion)
- baidu: [auth_key](https://cloud.baidu.com/doc/CDN/s/ujwvyeo0t)
- 网宿: [key](https://www.wangsu.com/document/277/18463)
- volcano: [sign](https://www.volcengine.com/docs/6454/99849)

## Ctyun

ctyun: [ctyun](https://www.ctyun.cn/document/10015932/10104831)

### Requirements

1. 如果您的鉴权URL中含有中文或特殊字符，需先进行URL转码（即Encode）后使用。

**Auth type A:**

鉴权方式A访问URL构成：http://DomainName/Filename?auth_key=timestamp-rand-uid-md5hash。

CDN服务器拿到请求后，会按照如下步骤进行校验：

是否携带鉴权参数。如果没有携带鉴权参数，认为请求非法，返回HTTP 403错误。

时间校验：判断系统当前时间是否在区间[timestamp，timestamp+有效时间]内。超出该区间，认为过期失效并返回HTTP 403错误。

加密串校验：时间校验通过后，比对CDN服务器计算出来的md5hash值与访问请求中带的md5hash值是否相同，结果一致则认为鉴权通过并返回文件，否则鉴权失败返回HTTP 403错误。

2、该功能暂不支持客户自助配置，如需使用，请通过提交工单给天翼云客服，由其人工操作开启。提交工单时请附带如下信息：

- 参数	说明
- 加密参数	默认为auth_key，也可自定义。
- 加密 key	设定的鉴权密钥。
- 鉴权 URL 有效时长	判断时间戳是否过期。
- 加密元素分隔符	默认使用中划线（-），也可自定义。

**Auth type B:**

鉴权方式B访问URL构成：http://DomainName/timestamp/md5hash/FileName。

CDN服务器拿到请求后，会按照如下步骤进行校验：

- 时间校验：判断系统当前时间是否在区间[timestamp，timestamp+有效时间]内。超出该区间，认为过期失效并返回HTTP 403错误。
- 加密串校验：时间校验通过后，比对CDN服务器计算出来的md5hash值与访问请求中带的md5hash值是否相同，结果一致则认为鉴权通过并返回文件，否则鉴权失败返回HTTP 403错误。

提交工单时请附带如下信息：

- 参数	说明
- 加密key	设定的鉴权密钥。
- 鉴权URL有效时长	判断时间戳是否过期。
- 加密元素分隔符	默认无符号，也可自定义。

**Auth type C:**

鉴权方式C访问URL构成：http://DomainName/FileName?auth_key=md5hash&timestamp=timestamp。

CDN服务器拿到请求后，会按照如下步骤进行校验：

- 是否携带鉴权参数。如果没有携带鉴权参数，认为请求非法，返回HTTP 403错误。 
- 时间校验：判断系统当前时间是否在区间[timestamp，timestamp+有效时间]内。超出该区间，认为过期失效并返回HTTP 403错误。 
- 加密串校验：时间校验通过后，比对CDN服务器计算出来的md5hash值与访问请求中带的md5hash值是否相同，结果一致则认为鉴权通过并返回文件，否则鉴权失败返回HTTP 403错误。

提交工单时请附带如下信息：

- 参数	说明 
- 加密参数	默认为auth_key跟timestamp，也可自定义。 
- 加密key	设定的鉴权密钥。 
- 鉴权URL有效时长	判断时间戳是否过期。 
- 加密元素分隔符	默认无符号，也可自定义。

