# Binary Specification: Windows.Networking.HostName.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Networking.HostName.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `293afe270a4aaff066e249ef474ad0c98b9ca989937b642927acc2b25f5d6ce3`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateHostNameFromSockAddr` | `0x3010` | 45 | UnwindData |  |
| 4 | `CreateNetworkAdapterFromGuid` | `0x34B0` | 10,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllMain` | `0x5F40` | 112 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x66C0` | 417 | UnwindData |  |
| 9 | `DllGetClassObject` | `0x70A0` | 161 | UnwindData |  |
| 8 | `DllGetActivationFactory` | `0x79F0` | 83 | UnwindData |  |
| 5 | `GetAllHostNames` | `0x7C40` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateHostNameFromString` | `0x7E70` | 36,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x10DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x10E10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateEndpointPairFromSockAddrs` | `0x10E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSortedEndpointPairs` | `0x10E60` | 0 | Indeterminate |  |
