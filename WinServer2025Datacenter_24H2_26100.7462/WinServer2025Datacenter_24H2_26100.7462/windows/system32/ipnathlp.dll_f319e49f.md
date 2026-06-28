# Binary Specification: ipnathlp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ipnathlp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f319e49f05479f7d04fa611eb963dd2a0a00e30c298169d92c9bf49e68dc2f93`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `NhReleaseBuffer` | `0x7970` | 158 | UnwindData |  |
| 3 | `NhAcquireVariableLengthBuffer` | `0x1E060` | 375 | UnwindData |  |
| 12 | `NhWriteDatagramSocket` | `0x20C90` | 673 | UnwindData |  |
| 9 | `NhReadDatagramSocket` | `0x241A0` | 947 | UnwindData |  |
| 6 | `NhDeleteSocket` | `0x32CA0` | 250 | UnwindData |  |
| 4 | `NhCreateDatagramSocket` | `0x348E0` | 76 | UnwindData |  |
| 2 | `NhAcquireFixedLengthBuffer` | `0x35850` | 88 | UnwindData |  |
| 17 | `NatCancelDynamicRedirect` | `0x378C0` | 130 | UnwindData |  |
| 19 | `NatCreateDynamicFullRedirect` | `0x38540` | 583 | UnwindData |  |
| 15 | `SvchostPushServiceGlobals` | `0x478A0` | 135 | UnwindData |  |
| 18 | `NatCancelRedirect` | `0x48510` | 334 | UnwindData |  |
| 7 | `NhInitializeBufferManagement` | `0x503A0` | 157 | UnwindData |  |
| 8 | `NhInitializeTraceManagement` | `0x55310` | 110 | UnwindData |  |
| 14 | `RegisterProtocol` | `0x56130` | 667 | UnwindData |  |
| 1 | `NhAcceptStreamSocket` | `0x57050` | 1,210 | UnwindData |  |
| 5 | `NhCreateStreamSocket` | `0x577F0` | 878 | UnwindData |  |
| 10 | `NhReadStreamSocket` | `0x57B70` | 837 | UnwindData |  |
| 13 | `NhWriteStreamSocket` | `0x57EC0` | 593 | UnwindData |  |
| 16 | `NatAcquirePortReservation` | `0x583F0` | 215 | UnwindData |  |
| 24 | `NatInitializePortReservation` | `0x587F0` | 403 | UnwindData |  |
| 29 | `NatReleasePortReservation` | `0x58990` | 236 | UnwindData |  |
| 30 | `NatShutdownPortReservation` | `0x58A90` | 108 | UnwindData |  |
| 20 | `NatCreateDynamicRedirect` | `0x58B10` | 101 | UnwindData |  |
| 21 | `NatCreateDynamicRedirectEx` | `0x58B80` | 108 | UnwindData |  |
| 22 | `NatCreateRedirect` | `0x58C00` | 150 | UnwindData |  |
| 23 | `NatCreateRedirectEx` | `0x58CA0` | 595 | UnwindData |  |
| 25 | `NatInitializeTranslator` | `0x59010` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `NatLookupAndQueryInformationSessionMapping` | `0x59190` | 499 | UnwindData |  |
| 27 | `NatQueryInformationRedirect` | `0x59390` | 692 | UnwindData |  |
| 28 | `NatQueryInformationRedirectHandle` | `0x59650` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `NatShutdownTranslator` | `0x59710` | 113,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ServiceMain` | `0x75400` | 251 | UnwindData |  |
