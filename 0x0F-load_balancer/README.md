# 0x0F. Load balancer

In this project, I continued to build up the configuration of the web server
issued in project 0x0B. I was issued two additional servers, one to replicate
the Nginx configuration of my original server, and another to set up an HAproxy
load balancer on to manage both web servers.

## Resource

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP Header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Tasks

- [0. Double the number of webservers](./0-custom_http_response_header)
- [1. Install your load balancer](./1-install_load_balancer)
- [2. Add a custom HTTP header with Puppet](./2-puppet_custom_http_response_header.pp)


---

## Author
* **Hicham Essaket** - [essaket](https://github.com/essaket)
