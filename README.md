skydrive-gae
============

A Google AppEngine application to fetch direct links of resources storing on Microsoft Skydrive.

Link format will be like:
> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/folder-name/file-name.mp3

You can use non-alphabet charaters at [folder-name] and [file-name], and url-encoded tyle is also supported.

For example:

> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/中文/文件.rar
> http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar

You maybe wish to used your domain name and simple url links.

Here is a sample of .htaccess for apache. Put it at any folder, let's call the folder `hikari` for demo.

    RewriteEngine On
    RewriteBase /
    RewriteRule ^(.*)$ http://your-app-id.appspot.com/cid-xxxxxxxxxxxxxxxx.office.live.com/self.aspx/.Public/$1

Now you can use your domain name and simple url link such as:

> http://your.domain.com/hikari/中文/文件.rar
> http://your.domain.com/hikari/%E4%B8%AD%E6%96%87/%E6%96%87%E4%BB%B6.rar
