#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <netinet/sctp.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP );
    const char* argument = {""};
    const char* with_sctp_option = "with_sctp";
    int ret = 0;
    int prot = 0;

    if (argc == 2) {
        argument = argv[1];
    }

    ret = sctp_getaddrlen(AF_INET);
    printf("sctp_getaddrlen: %d\n", ret);
    socklen_t len = sizeof(prot);
    getsockopt( fd, SOL_SOCKET, SO_PROTOCOL, &prot, &len );
    printf("getsockopt: %d\n", prot);

    if (strncmp(argument, "with_sctp", strlen(with_sctp_option)) == 0) {
        return !((prot == IPPROTO_SCTP) && (ret));
    } else {
        return !((prot == IPPROTO_TCP) && (ret));
    }
}
