# Binary Specification: httpprxc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\httpprxc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ecc8cedb24d016908cc48899438eeee017c7b6a36ff9d71e24ffc26a6b7da0f8`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ProxyHelperClientAllocateMemory` | `0x20F0` | 74 | UnwindData |  |
| 2 | `ProxyHelperClientConnectToServer` | `0x2140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ProxyHelperClientDisconnectFromServer` | `0x2160` | 32 | UnwindData |  |
| 4 | `ProxyHelperClientFreeMemory` | `0x22C0` | 46 | UnwindData |  |
| 5 | `ProxyHelperClientGetAllProxiesForUrl` | `0x2300` | 838 | UnwindData |  |
| 6 | `ProxyHelperClientGetProxyCredentials` | `0x2650` | 309 | UnwindData |  |
| 7 | `ProxyHelperClientGetProxyForUrl` | `0x2790` | 844 | UnwindData |  |
| 8 | `ProxyHelperClientInitialize` | `0x2AF0` | 69 | UnwindData |  |
| 9 | `ProxyHelperClientRegisterForEventNotification` | `0x2B40` | 991 | UnwindData |  |
| 10 | `ProxyHelperClientUninitialize` | `0x2F30` | 121 | UnwindData |  |
| 11 | `ProxyHelperClientUnregisterEventNotification` | `0x2FB0` | 477 | UnwindData |  |
