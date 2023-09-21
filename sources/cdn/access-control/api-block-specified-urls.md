## 封禁

Refer: 

- [Ctyun Document](https://www.ctyun.cn/document/10015932/10035127)
- Ctyun offline document

### 封禁 API

Request:

- 需要封禁的 url, 单次 url 最多 1000 
- 需要封禁的 url, 需要支持正则匹配。
- 封禁类型：
  - 10（忽略 url 参数和协议） 
  - 12（按照完整的 url 进行全匹配） 
  - 14（基于缓存封解禁，即与提交的url相同缓存的文件都封禁） 
  - 不填默认屏蔽类型为14
- callback: 结果回调 url。当封禁任务完成(不论成功或失败)。主动 post 回调 url。

封禁的 URL 返回：403

Response: 

- 本次提交的任务 id, 可根据此 id 查询本次成功提交推送的 url/dir 状态。
- 本次成功提交的 url 数量
- 提交失败的 url 列表

### 封禁结果查询 API

是不是管控平台做？

### 实现思路

- 参考 URL 鉴权实现封禁功能：URL 鉴权是校验 token，封禁是对 URL 进行正则匹配。
  - 细节：URL parameters 是否要去掉？
- callback: 完成封禁操作后进行 callback。

## 解封

封禁的逆向操作。

