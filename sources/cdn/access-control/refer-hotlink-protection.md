## Introduce

Refer: https://www.ctyun.cn/document/10015932/10088464

Referer防盗链，是基于HTTP请求头中Referer字段（例如，Referer黑白名单）来设置访问控制规则，实现对访客的身份识别和过滤，防止网站资源被非法盗用。
配置Referer黑白名单后，CDN会根据名单识别请求身份，允许或拒绝访问请求。允许访问请求，CDN会返回资源链接；拒绝访问请求，CDN会返回403响应码。

## Requirements

- 是否允许空 referer 访问；取值"on", "off"
- 支持 IP, 正则，端口
- 支持黑白名单
- 黑白名单只允许存在一个，若同时存在只处理黑名单