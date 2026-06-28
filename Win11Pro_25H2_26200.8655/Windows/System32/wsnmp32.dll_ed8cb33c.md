# Binary Specification: wsnmp32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wsnmp32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed8cb33c920e643628cac35e37f24009f6ba99b285f13033637e5a5b292f10bb`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 222 | `SnmpCancelMsg` | `0x1010` | 307 | UnwindData |  |
| 204 | `SnmpSendMsg` | `0x1A00` | 2,984 | UnwindData |  |
| 302 | `SnmpFreeEntity` | `0x3740` | 89 | UnwindData |  |
| 402 | `SnmpFreeContext` | `0x38B0` | 93 | UnwindData |  |
| 205 | `SnmpRecvMsg` | `0x39F0` | 2,113 | UnwindData |  |
| 600 | `SnmpCreateVbl` | `0x4240` | 468 | UnwindData |  |
| 500 | `SnmpCreatePdu` | `0x4420` | 580 | UnwindData |  |
| 601 | `SnmpDuplicateVbl` | `0x4670` | 455 | UnwindData |  |
| 400 | `SnmpStrToContext` | `0x4840` | 989 | UnwindData |  |
| 501 | `SnmpGetPduData` | `0x4C30` | 591 | UnwindData |  |
| 300 | `SnmpStrToEntity` | `0x4E90` | 1,434 | UnwindData |  |
| 203 | `SnmpClose` | `0x5610` | 96 | UnwindData |  |
| 604 | `SnmpGetVb` | `0x5B90` | 953 | UnwindData |  |
| 605 | `SnmpSetVb` | `0x5FF0` | 572 | UnwindData |  |
| 603 | `SnmpCountVbl` | `0x64E0` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `SnmpFreeVbl` | `0x76C0` | 96 | UnwindData |  |
| 903 | `SnmpStrToOid` | `0x8080` | 576 | UnwindData |  |
| 504 | `SnmpFreePdu` | `0x8550` | 89 | UnwindData |  |
| 900 | `SnmpFreeDescriptor` | `0x8B90` | 131 | UnwindData |  |
| 107 | `SnmpSetRetry` | `0x8C20` | 91 | UnwindData |  |
| 105 | `SnmpSetTimeout` | `0x8D00` | 91 | UnwindData |  |
| 301 | `SnmpEntityToStr` | `0x8DE0` | 489 | UnwindData |  |
| 292 | `SnmpCleanupEx` | `0x9040` | 133 | UnwindData |  |
| 906 | `SnmpOidCompare` | `0x9570` | 304 | UnwindData |  |
| 401 | `SnmpContextToStr` | `0x9700` | 402 | UnwindData |  |
| 291 | `SnmpStartupEx` | `0x98A0` | 265 | UnwindData |  |
| 220 | `SnmpCreateSession` | `0x99B0` | 468 | UnwindData |  |
| 101 | `SnmpSetTranslateMode` | `0x9D60` | 112 | UnwindData |  |
| 103 | `SnmpSetRetransmitMode` | `0x9DE0` | 101 | UnwindData |  |
| 202 | `SnmpOpen` | `0x9EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `SnmpStartup` | `0x9EE0` | 231 | UnwindData |  |
| 201 | `SnmpCleanup` | `0x9FD0` | 133 | UnwindData |  |
| 221 | `SnmpListen` | `0xB6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `SnmpListenEx` | `0xB700` | 896 | UnwindData |  |
| 206 | `SnmpRegister` | `0xBA90` | 1,718 | UnwindData |  |
| 102 | `SnmpGetRetransmitMode` | `0xC150` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `SnmpGetRetry` | `0xC190` | 126 | UnwindData |  |
| 104 | `SnmpGetTimeout` | `0xC220` | 126 | UnwindData |  |
| 100 | `SnmpGetTranslateMode` | `0xC2B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `SnmpGetVendorInfo` | `0xC2F0` | 154 | UnwindData |  |
| 320 | `SnmpSetPort` | `0xC390` | 193 | UnwindData |  |
| 503 | `SnmpDuplicatePdu` | `0xD3F0` | 324 | UnwindData |  |
| 502 | `SnmpSetPduData` | `0xD540` | 413 | UnwindData |  |
| 902 | `SnmpDecodeMsg` | `0xD6F0` | 622 | UnwindData |  |
| 901 | `SnmpEncodeMsg` | `0xD970` | 523 | UnwindData |  |
| 999 | `SnmpGetLastError` | `0xDB90` | 69 | UnwindData |  |
| 905 | `SnmpOidCopy` | `0xDC70` | 168 | UnwindData |  |
| 904 | `SnmpOidToStr` | `0xDD20` | 285 | UnwindData |  |
| 606 | `SnmpDeleteVb` | `0xDEE0` | 265 | UnwindData |  |
| 108 | `SnmpConveyAgentAddress` | `0xDFF0` | 104 | UnwindData |  |
| 109 | `SnmpSetAgentAddress` | `0xE060` | 181 | UnwindData |  |
