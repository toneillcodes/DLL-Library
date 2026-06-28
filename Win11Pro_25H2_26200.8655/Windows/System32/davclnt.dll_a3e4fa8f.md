# Binary Specification: davclnt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\davclnt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a3e4fa8f038c77c8751f4c14d147903f0e02edf169534932e2b996a2b860e6d0`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `NPEnumResource` | `0x1010` | 4,994 | UnwindData |  |
| 24 | `NPOpenEnum` | `0x2430` | 13 | UnwindData |  |
| 19 | `NPGetConnection` | `0x31F0` | 1,339 | UnwindData |  |
| 7 | `DavSetCookieW` | `0x3740` | 830 | UnwindData |  |
| 20 | `NPGetResourceInformation` | `0x42F0` | 2,018 | UnwindData |  |
| 22 | `NPGetUniversalName` | `0x4AE0` | 1,489 | UnwindData |  |
| 15 | `NPCloseEnum` | `0x70E0` | 159 | UnwindData |  |
| 18 | `NPGetCaps` | `0x74C0` | 208 | UnwindData |  |
| 8 | `DavUnregisterAuthCallback` | `0x76A0` | 121 | UnwindData |  |
| 6 | `DavRegisterAuthCallback` | `0x7720` | 371 | UnwindData |  |
| 13 | `NPAddConnection3` | `0x7F20` | 8,966 | UnwindData |  |
| 11 | `DllMain` | `0xA320` | 407 | UnwindData |  |
| 1 | `DavCancelConnectionsToServer` | `0xBF00` | 921 | UnwindData |  |
| 2 | `DavFreeUsedDiskSpace` | `0xCBE0` | 244 | UnwindData |  |
| 3 | `DavGetDiskSpaceUsage` | `0xD2C0` | 411 | UnwindData |  |
| 4 | `DavGetTheLockOwnerOfTheFile` | `0xD620` | 531 | UnwindData |  |
| 5 | `DavInvalidateCache` | `0xDA20` | 607 | UnwindData |  |
| 12 | `NPAddConnection` | `0x10060` | 91 | UnwindData |  |
| 14 | `NPCancelConnection` | `0x100D0` | 979 | UnwindData |  |
| 17 | `NPFormatNetworkName` | `0x104B0` | 357 | UnwindData |  |
| 21 | `NPGetResourceParent` | `0x10620` | 1,422 | UnwindData |  |
| 23 | `NPGetUser` | `0x10BC0` | 1,395 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x127D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllGetClassObject` | `0x127F0` | 0 | Indeterminate |  |
