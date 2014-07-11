skydrive-gae
============

A Google AppEngine application to fetch direct links of resources storing on Microsoft Skydrive.

Instruction
--------------------

Link format will be like:
> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/folder-name/file-name.mp3

You can use non-alphabet charaters at [folder-name] and [file-name], and url-encoded style is also supported.

For example:

> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/中文/文件.rar
> 
> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar

You maybe wish to used your domain name and simple url links.

Here is a sample of .htaccess for apache. Put it at any folder, let's call the folder `hikari` for demo.

    RewriteEngine On
    RewriteBase /
    RewriteRule ^(.*)$ http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/$1

Now you can use your domain name and simple url link such as:

> http://your.domain.com/hikari/中文/文件.rar
> 
> http://your.domain.com/hikari/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar

----------------------------

中文版使用指南
----------------------------

skydrive-gae支持3种形式的链接。

形式1：
> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/folder-name/file-name.mp3

这种形式最为古老。后面的资源定位字符串在很久以前是能访问的，现在M$已经停止支持这种资源定位。

形式2：
> http://your-app-id.appspot.com/cid/xxxxxxxxxxxxxxxx/.Public/folder-name/file-name.mp3

形式2是形式1的简化形式，去掉冗余字符

形式3：
> http://your-app-id.appspot.com/resid/xxxxxxxxxxxxxxxx%21xxx

形式3只需resid，resid可以在skydrive上取得。

形式1和形式2的后半部分，是直观上的文件路径
> .Public/folder-name/file-name.mp3

对于古老的skydrive用户，公共文件夹一般是`.Public`，新用户一般是`Public`，但这个文件夹可以被重命名。
另外skydrive-gae同样支持根目录下用户自行添加的公共属性的文件夹，比如根目录下有一个test的公共属性文件夹，里面有一个test.docx文件：
> http://your-app-id.appspot.com/cid/xxxxxxxxxxxxxxxx/test/test.docx

文件路径支持中文字符，urlencode方式编码过的路径同样没有问题
> http://your-app-id.appspot.com/cid/xxxxxxxxxxxxxxxx/.Public/中文/文件.rar
> 
> http://your-app-id.appspot.com/cid/xxxxxxxxxxxxxxxx/.Public/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar

有童鞋可能希望使用自己的域名和更简短的链接形式，如果你使用apache服务器，可以参考下面的.htaccess文件。

Here is a sample of .htaccess for apache. Put it at any folder, let's call the folder `hikari` for demo.

    RewriteEngine On
    RewriteBase /
    RewriteRule ^(.*)$ http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/$1

Now you can use your domain name and simple url link such as:

> http://your.domain.com/hikari/中文/文件.rar
> 
> http://your.domain.com/hikari/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar
