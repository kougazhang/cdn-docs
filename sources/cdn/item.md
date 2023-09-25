cdn的三大能力：静态加速、动态加速、安全防护

CNAME：CNAME就是记录一个域名的别名，比如我们给blog.example.com记录一条CNAME为blog.com，当我们对blog.example.com进行dns解析时，它实际上会去寻找example.com的A记录的ip地址。一个CNAME当然可以指向另一个CNAME，但是这样解析起来很低效。

为什么CDN通常会用到CNAME？CDN通常会给加速域名记录一条CNAME，用于解析到自家服务器的ip，这样对源站的所有请求都会来到cdn节点。解析到自家的cdn节点的第一阶段，一般都是cdn厂家的dns服务器，他们会根据你请求的位置，返回一个理论上访问速度最快的ip地址，通常不一定是物理距离上最近的，还要考虑拥塞等情况

静态资源：简单来说，静态资源就是文件，上幂等的，每次用户请求返还的内容都一样，图片、压缩文件、html、css等。cdn会把加速域名的静态文件都缓存到cdn节点上

动态资源：最简单的例子就是api请求，可能根据用户的不同，相同的请求会有不同的结果，这样的内容上不能缓存的。所以cdn的路由系统会进行动态选路，他们会用各个cdn节点当作中间桥梁，为用户选择出一条网络状况良好的链路。

动态内容用到的cdn产品一般是全站加速

DNS/域名解析：就是把域名解析成ip地址

SSL/TLS：建立在tcp协议之上的安全传输协议
- 建立会话
- 加密数据
- 校验网站证书

回源：cdn节点未缓存用户请求的资源货缓存到期，cdn节点会向源站获取资源并返还给用户

回源HOST：回源时实际请求的域名或ip，如果源站有多个域名或ip，可以指定回源时请求的域名或ip

回源协议：cdn节点访问源站的时候的协议，比如可以设置回源协议为http或https

Range回源

Range上http协议的一个请求头，可以指定需要请求资源的byte范围 Range: bytes=start-end
源站在收到CDN节点的回源请求时，根据HTTP请求头中的Range信息返回指定范围的内容数据给CDN节点，例如只返回某个文件的0-100Byte范围内的数据。

Referer防盗链：Referer防盗链，是基于HTTP请求头中Referer字段（例如，Referer黑白名单）来设置访问控制规则，实现对访客的身份识别和过滤，防止网站资源被非法盗用。配置Referer黑白名单后，CDN会根据名单识别请求身份，允许或拒绝访问请求。

Referer是http请求头的一部分，携带了http请求的来源地址信息（协议+域名+请求参数），可用于识别请求来源

The Referer header is sent with every HTTP request that the client makes, and its value is the URL of the page that the client was on before requesting the current resource. For example, if a user clicks on a link to a resource on a web page, the Referer
header in the request for that resource will contain the URL of the web page that the link was on.

缓存过期时间：cdn节点上资源过期的时间，过期后cdn节点就会删除该缓存

QUIC：基于UDP的传输层协议，能保障网络安全性，同时有更低的连接和传输耗时

SNI（Server Name Indication）是为了解决一个服务器使用多个域名和证书的TLS扩展，主要解决一台服务器只能使用一个证书的缺点。开启SNI后，允许客户端在发起SSL握手请求时就提交请求的域名信息，负载均衡收到SSL请求后，会根据域名去查找证书，如果找到域名对应的证书，则返回该证书；如果没有找到域名对应的证书，则返回缺省证书。负载均衡在配置HTTPS监听器支持此功能，即支持绑定多个证书。

刷新：删除cdn节点上过期的缓存文件

目录刷新：会将节点上的文件资源过期，会同源站对比Last-Modified时间，比如节点上的目录文件的Last-Modified为：Mon, 26 Dec 2018 11:11:00 GMT ，源站文件的Last-Modified为Mon, 28 Dec 2018 11:11:00 GMT.则此时源站会告诉节点：你的文件比我的文件老，我已经更新文件了，快来取最新的资源吧，此时会将源站新的资源更新到节点上，否则，源站返回304，告诉节点，你节点上的资源已经和我源站上的资源是一致，为最新的了，无需更新。

url刷新：直接将节点上缓存的资源删除.

预热：预热可理解为由 CDN 主动模拟用户发起首次请求，需要提交具体资源的URL地址，因此无法支持目录预热。预热操作会将源站内容主动拉取到 CDN 的中间层节点，预热到中间层节点不会产生计费流量。若您需要将内容预热到 CDN 的边缘节点。

DDoS：分布式拒绝服务攻击（Distributed Denial of Service，简称DDoS）是指攻击的发出点是分布在不同地方，且所请求的服务往往要消耗大量的系统资源，造成目标主机无法为用户提供正常服务。

CC攻击：攻击者借助代理服务器生成指向受害主机的合法请求，实现DDoS和伪装就叫：CC(Challenge Collapsar)，CC主要是攻击页面，属于应用层攻击。