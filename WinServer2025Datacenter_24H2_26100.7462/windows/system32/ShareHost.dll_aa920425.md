# Binary Specification: ShareHost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ShareHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aa920425a4d0390fb458acaf3f99ee720373ca2abbd70421ac591b85ee3c039e`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3A70` | 104 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x6860` | 15,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetActivationFactory` | `0xA4D0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xA510` | 111 | UnwindData |  |
| 5 | `ResolveConnectedSharePlatformToken` | `0x2A920` | 77 | UnwindData |  |
