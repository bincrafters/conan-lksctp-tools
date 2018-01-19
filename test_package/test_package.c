#include <stdio.h>
#include <sys/socket.h>
#include <netinet/sctp.h>

int main()
{
    int ret = sctp_getaddrlen(AF_INET);
    printf("%d\n", ret);
    return ret > 0;
}
