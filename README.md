NGINX configuration
```nginx
server {
	listen 80;
	server_name YOUR.DOMAIN.TLD;

	location /screenshots {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header Host $http_host;
		proxy_redirect off;
		proxy_pass http://127.0.0.1:YOURSERVERPORT;
	}
}
```
ShareX Configuration
<img src="https://github.com/Airiuwu/ShareX-Uploader/blob/main/assets/unknown.png?raw=true"/>
