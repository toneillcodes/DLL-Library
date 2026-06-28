# Binary Specification: Windows.Networking.HostName.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Networking.HostName.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8e97abb7eb7f7ea5ab1aba1a5e43e56f715b3755946c1bf3465c4da1c8671905`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateHostNameFromSockAddr` | `0x3060` | 45 | UnwindData |  |
| 4 | `CreateNetworkAdapterFromGuid` | `0x3510` | 10,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllMain` | `0x5FA0` | 112 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x6720` | 417 | UnwindData |  |
| 9 | `DllGetClassObject` | `0x7100` | 161 | UnwindData |  |
| 8 | `DllGetActivationFactory` | `0x7A50` | 83 | UnwindData |  |
| 5 | `GetAllHostNames` | `0x7CA0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateHostNameFromString` | `0x7ED0` | 50,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x14510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x14540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateEndpointPairFromSockAddrs` | `0x14580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSortedEndpointPairs` | `0x14590` | 0 | Indeterminate |  |
